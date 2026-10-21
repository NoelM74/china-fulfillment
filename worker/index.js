/*
 * China Fulfillment — PFC Open Platform proxy Worker.
 *
 * Runs ONLY for /api/* (see run_worker_first in wrangler.jsonc). Every other
 * path is served straight from static assets, exactly as before this file existed.
 *
 * Why a Worker: the PFC Open Platform (oms.pfcexpress.com) is a plain-http SOAP/ASMX
 * service that needs a secret key. A static page cannot call it (mixed content, CORS,
 * and the key would be exposed). This Worker holds the key server-side and hands the
 * browser clean JSON.
 *
 * Secrets (set with:  wrangler secret put <NAME> ):
 *   PFC_SECRET_KEY    PFC API identifier (the "secretkey")      — required
 *   PFC_CUSTOMER_ID   PFC customer id, e.g. 80000               — required
 * Optional config (wrangler.jsonc "vars", or secrets):
 *   PFC_API_BASE      upstream base; default below
 *   RATE_FX_USD       RMB->USD multiplier to add a usd field (e.g. "0.141"); omit for RMB only
 *
 * The client NEVER supplies the key. Any secretkey in the query string is ignored.
 */

const DEFAULT_BASE = "http://oms.pfcexpress.com/webservice/APIWebService.asmx";

const JSON_HEADERS = {
  "content-type": "application/json; charset=utf-8",
  "cache-control": "no-store",
  "x-content-type-options": "nosniff",
};

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), { status, headers: JSON_HEADERS });
}

function cfg(env) {
  return {
    base: (env.PFC_API_BASE || DEFAULT_BASE).replace(/\/+$/, ""),
    key: env.PFC_SECRET_KEY || "",
    customer: env.PFC_CUSTOMER_ID || "",
    fx: parseFloat(env.RATE_FX_USD || "") || 0,
    get configured() { return Boolean(this.key && this.customer); },
  };
}

// --- ASMX helpers -----------------------------------------------------------
// ASMX string methods return the payload wrapped as <string xmlns="...">...</string>,
// with the inner JSON XML-escaped. Unwrap and unescape it.
function decodeXml(s) {
  return s
    .replace(/&lt;/g, "<").replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"').replace(/&#0?39;/g, "'").replace(/&apos;/g, "'")
    .replace(/&amp;/g, "&");
}
function unwrapAsmx(text) {
  const t = (text || "").trim();
  const m = t.match(/<string[^>]*>([\s\S]*?)<\/string>/i);
  if (m) return decodeXml(m[1]).trim();
  if (t.startsWith("<")) {
    const m2 = t.match(/^<[^>]+>([\s\S]*)<\/[^>]+>\s*$/);
    if (m2) return decodeXml(m2[1]).trim();
  }
  return t;
}
async function callPfc(c, method, params) {
  const qs = new URLSearchParams(params).toString();
  const url = `${c.base}/${method}?${qs}`;
  let r;
  try {
    r = await fetch(url, { method: "GET", headers: { accept: "application/json, text/xml, */*" } });
  } catch (e) {
    const err = new Error("upstream_unreachable"); err.status = 502; throw err;
  }
  const body = await r.text();
  if (!r.ok) { const err = new Error("upstream_error"); err.status = 502; err.upstream = r.status; throw err; }
  return unwrapAsmx(body);
}
function parseLoose(s) { try { return JSON.parse(s); } catch { return null; } }
function looksHtml(s) { return /^\s*<(?:!doctype|html|\?xml[^>]*>\s*<(?:!doctype|html))/i.test(s || ""); }
// Upstream must return a JSON array. Anything else (an HTML error page, a SOAP
// fault) is an upstream problem, not an empty result — surface it as 502 so the
// page shows "unavailable" rather than rendering a 404 page as data.
function expectArray(raw, method) {
  const v = parseLoose(raw);
  if (Array.isArray(v)) return v;
  const err = new Error("upstream_bad_response"); err.status = 502; err.method = method; throw err;
}

// --- validation -------------------------------------------------------------
const reCountry = /^[A-Za-z0-9]{1,6}$/;
const reTrack = /^[A-Za-z0-9,\-]{3,64}$/;
function num(v, min, max) {
  const n = parseFloat(v);
  if (!isFinite(n) || n < min || n > max) return null;
  return n;
}

// --- routes -----------------------------------------------------------------
async function health(c) {
  return json({ ok: true, configured: c.configured, base: c.base, currency: c.fx ? "RMB+USD" : "RMB" });
}

async function countries(c) {
  if (!c.configured) return json({ error: "not_configured" }, 503);
  const raw = await callPfc(c, "getCountry", { secretkey: c.key });
  const arr = expectArray(raw, "getCountry");
  const list = arr.map((x) => ({
    code: x.Base_placeId ?? x.base_placeId ?? "",
    name: x.EnName ?? x.enname ?? "",
    short: x.ShortName ?? x.shortname ?? "",
  })).filter((x) => x.code && x.name)
     .sort((a, b) => a.name.localeCompare(b.name));
  return json({ countries: list });
}

async function rate(c, url) {
  if (!c.configured) return json({ error: "not_configured" }, 503);
  const p = url.searchParams;
  const country = p.get("country") || "";
  if (!reCountry.test(country)) return json({ error: "bad_country" }, 400);
  const weight = num(p.get("weight"), 0.001, 2000);
  if (weight === null) return json({ error: "bad_weight" }, 400);
  const l = num(p.get("l") || "0", 0, 400) || 0;
  const w = num(p.get("w") || "0", 0, 400) || 0;
  const h = num(p.get("h") || "0", 0, 400) || 0;
  const volume = +(l * w * h).toFixed(3); // cm^3; server derives volumetric weight

  const raw = await callPfc(c, "getFeeByCWV", {
    country, weight: String(weight), volume: String(volume),
    customerid: c.customer, secretkey: c.key,
  });
  const arr = expectArray(raw, "getFeeByCWV");
  const services = arr.map((x) => {
    const total = parseFloat(x.MinSaleAmountTotal ?? x.minsaleamounttotal ?? "0") || 0;
    const o = {
      code: x.ChannelCode ?? x.channelcode ?? "",
      name: x.CHEnName ?? x.chenname ?? x.ChannelCode ?? "",
      cn: x.CHCnName ?? x.chcnname ?? "",
      days: x.RefTime ?? x.reftime ?? "",
      total: +total.toFixed(2),
    };
    if (c.fx) o.usd = +(total * c.fx).toFixed(2);
    return o;
  }).filter((s) => s.total > 0)
    .sort((a, b) => a.total - b.total);

  return json({
    query: { country, weight, l, w, h, volume },
    currency: "RMB",
    fx_usd: c.fx || null,
    services,
  });
}

async function track(c, url) {
  const no = (url.searchParams.get("no") || "").trim();
  if (!reTrack.test(no)) return json({ error: "bad_number" }, 400);
  // Gate on configuration so preview shows the sample and we never hit the
  // upstream before the endpoint shape is confirmed with a real key.
  if (!c.configured) return json({ error: "not_configured" }, 503);

  // Timeline: getOrder_Track takes just the number (no key per PFC docs).
  let events = [];
  const raw = await callPfc(c, "getOrder_Track", { OrderNo: no });
  if (looksHtml(raw)) { const e = new Error("upstream_bad_response"); e.status = 502; throw e; }
  const parsed = parseLoose(raw);
  if (Array.isArray(parsed)) {
    events = parsed.map((e) => ({
      description: e.Description ?? e.description ?? e.Content ?? e.content ?? "",
      time: e.Time ?? e.time ?? e.AcceptTime ?? "",
    }));
  } else if (raw) {
    // Fall back to "DESCRIPTION  YYYY-MM-DD HH:MM:SS" lines, but only keep lines
    // that actually carry a timestamp, so stray markup can't become an event.
    events = raw.split(/\r?\n/).map((ln) => ln.trim()).filter(Boolean).map((ln) => {
      const m = ln.match(/^(.*?)\s*(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s*$/);
      return m ? { description: m[1].trim(), time: m[2] } : null;
    }).filter(Boolean);
  }
  events = events.filter((e) => e.description);

  // Optional header (status / destination / channel) via getPackage — needs key.
  let header = null;
  if (c.configured) {
    try {
      const raw = await callPfc(c, "getPackage", { orderNo: no, customerid: c.customer, secretkey: c.key });
      const arr = parseLoose(raw);
      const r0 = Array.isArray(arr) ? arr[0] : arr;
      if (r0) header = {
        orderNo: r0.OrderNo ?? r0.orderNo ?? "",
        trackingNo: r0.TrackingNo ?? r0.trackingNo ?? "",
        status: r0.OrderStatus2 ?? r0.orderStatus2 ?? "",
        destination: r0.EnName ?? r0.enName ?? "",
        channel: r0.ChannelCode ?? r0.channelCode ?? "",
      };
    } catch { /* header is best-effort */ }
  }

  return json({ number: no, header, events });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (!url.pathname.startsWith("/api/")) {
      return env.ASSETS ? env.ASSETS.fetch(request) : new Response("Not found", { status: 404 });
    }
    if (request.method !== "GET" && request.method !== "HEAD") {
      return json({ error: "method_not_allowed" }, 405);
    }
    const c = cfg(env);
    try {
      switch (url.pathname) {
        case "/api/health":    return await health(c);
        case "/api/countries": return await countries(c);
        case "/api/rate":      return await rate(c, url);
        case "/api/track":     return await track(c, url);
        default:               return json({ error: "not_found" }, 404);
      }
    } catch (e) {
      return json({ error: e.message || "server_error", upstream: e.upstream }, e.status || 500);
    }
  },
};
