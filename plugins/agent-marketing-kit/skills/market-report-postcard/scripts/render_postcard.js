// Renders the market report postcard to a print-ready PDF and PNG previews.
//
// Usage:
//   NODE_PATH=$(npm root -g) node render_postcard.js <data.json> <out_dir> [fonts_dir]
//
//   data.json  the postcard data (shape in SKILL.md). Image fields are local file
//              paths, relative to data.json or absolute.
//   out_dir    gets <name>.pdf (2 pages, 8.75 x 5.75 in = 8.5 x 5.5 trim + 0.125 bleed),
//              <name>-front.png, <name>-back.png (what it will look like, trimmed)
//              and <name>-guides.png (both sides with trim, safe area and mail zones).
//   fonts_dir  folder with node_modules/@fontsource/<family> installed (npm i
//              @fontsource/bodoni-moda @fontsource/montserrat ...). Also where the
//              qrcode package lives if a QR link is used (npm i qrcode).
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path");
const [dataFile, outArg, fontsArg] = process.argv.slice(2);
const out = outArg && path.resolve(outArg), fontsDir = fontsArg && path.resolve(fontsArg);
if (!out) { console.error("usage: render_postcard.js <data.json> <out_dir> [fonts_dir]"); process.exit(2); }
const D = JSON.parse(fs.readFileSync(dataFile, "utf8"));
const base = path.dirname(path.resolve(dataFile));
const tpl = path.join(__dirname, "..", "assets", "postcard.html");
fs.mkdirSync(out, { recursive: true });
const name = D.fileName || "Market-Report-Postcard";

for (const k of ["frontPhoto", "headshot", "logoOnDark", "logoOnLight", "brokerLogo", "lockupOnDark", "lockupOnLight"]) {
  if (!D[k]) continue;
  const p = path.isAbsolute(D[k]) ? D[k] : path.join(base, D[k]);
  if (!fs.existsSync(p)) { console.error("Missing image for " + k + ": " + p); process.exit(1); }
  D[k] = "file://" + p;
}

function fontCSS() {
  if (!fontsDir) return "";
  let css = "";
  for (const fam of [D.fonts?.serif || "Bodoni Moda", D.fonts?.sans || "Montserrat"]) {
    const slug = fam.toLowerCase().replace(/\s+/g, "-"), dir = path.join(fontsDir, "node_modules/@fontsource", slug, "files");
    if (!fs.existsSync(dir)) { console.warn("font not installed: " + fam + " (npm i @fontsource/" + slug + ")"); continue; }
    for (const w of [300, 400, 500, 600, 700]) for (const st of ["normal", "italic"]) {
      const f = path.join(dir, `${slug}-latin-${w}-${st}.woff2`);
      if (fs.existsSync(f)) css += `@font-face{font-family:'${fam}';font-weight:${w};font-style:${st};src:url(file://${f})}`;
    }
  }
  return css;
}

(async () => {
  if (D.qrUrl) {
    let QR; try { QR = require(path.join(fontsDir || ".", "node_modules", "qrcode")); } catch { QR = require("qrcode"); }
    D.qrSvg = await QR.toString(D.qrUrl, { type: "svg", margin: 0, errorCorrectionLevel: "M", color: { dark: "#000000", light: "#ffffff" } });
  }
  const html = fs.readFileSync(tpl, "utf8").replace("<style>", `<style>${fontCSS()}`);
  const b = await chromium.launch();
  const page = await b.newPage({ viewport: { width: 840, height: 552 }, deviceScaleFactor: 2 });
  const tmp = path.join(out, ".postcard-render.html");
  const render = async (guides) => {
    fs.writeFileSync(tmp, html.replace("<div id=\"root\"></div>", `<div id="root"></div><script>window.POSTCARD=${JSON.stringify({ ...D, guides }).replace(/</g, "\\u003c")};</script>`));
    await page.goto("file://" + tmp); await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(200);
    const broken = await page.evaluate(() => [...document.images].filter((i) => !(i.complete && i.naturalWidth)).map((i) => i.src));
    if (broken.length) console.warn("Images that didn't load:", broken.join(", "));
  };
  await render(false);
  await page.pdf({ path: path.join(out, name + ".pdf"), width: "8.75in", height: "5.75in", printBackground: true, pageRanges: "1-2" });
  // Previews at the trim size (bleed cropped off), 96 css px per inch x2.
  await page.setViewportSize({ width: 840, height: 1104 });
  const pages = await page.$$(".page");
  const sides = ["front", "back"];
  for (let i = 0; i < 2; i++) {
    const bb = await pages[i].boundingBox();
    await page.screenshot({ path: path.join(out, `${name}-${sides[i]}.png`), clip: { x: bb.x + 12, y: bb.y + 12, width: bb.width - 24, height: bb.height - 24 } });
  }
  await render(true);
  await page.setViewportSize({ width: 840, height: 1104 });
  await page.screenshot({ path: path.join(out, `${name}-guides.png`), fullPage: true });
  await b.close(); fs.unlinkSync(tmp);
  console.log("wrote " + path.join(out, name + ".pdf") + " and previews");
})();
