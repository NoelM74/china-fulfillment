import { chromium } from "/opt/node22/lib/node_modules/playwright/index.mjs";
const D = process.argv[2];
const names = ["infographic-sea-freight-fba-timeline","infographic-lcl-vs-fcl-break-even","infographic-china-europe-four-modes","infographic-ieepa-refund-who-gets-paid"];
const exe = process.env.CHROMIUM_PATH || "/opt/pw-browsers/chromium-1194/chrome-linux/chrome";
const b = await chromium.launch({executablePath: exe});
const pg = await b.newPage({viewport:{width:1200,height:1500},deviceScaleFactor:1});
for (const n of names) {
  await pg.goto("file://"+D+"/"+n+".html",{waitUntil:"load"});
  await pg.evaluate(() => document.fonts.ready);
  const fam = await pg.evaluate(() => document.fonts.check("800 40px Outfit"));
  const over = await pg.evaluate(() => { const w=document.querySelector('.wrap'); return w.scrollHeight>1500 || document.documentElement.scrollWidth>1200; });
  await pg.screenshot({path:D+"/"+n+".png",clip:{x:0,y:0,width:1200,height:1500}});
  console.log(n,"font:",fam,"overflow:",over);
}
await b.close();
