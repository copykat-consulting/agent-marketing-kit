// Renders a Claude Design canvas's artboards to 1080 x 1350 JPGs for scheduling.
//
// Usage:
//   NODE_PATH=$(npm root -g) node render_designs.js <project_dir> <images_dir> <assets.json> <out_dir> [fonts_dir]
//
//   project_dir  folder holding the canvas's *.dc.html artboards (read from the
//                Design artifact's published "project/" files)
//   images_dir   the original photo and logo files that were uploaded to the canvas
//   assets.json  the canvas's asset listing as {"<32-hex blob id>": "<sha256 hex>"}
//                (from an "assets" listing of the Design artifact); each blob is
//                matched to a local file by its sha256
//   out_dir      where the JPGs go, named Post-01.jpg, Post-02-1.jpg (carousel slide 1), ...
//   fonts_dir    optional: a folder with node_modules/@fontsource/<family>/files/*.woff2
//                (npm i @fontsource/<family>), since the workspace usually can't reach
//                Google Fonts. Families are read from each artboard's Google Fonts link.
//
// Artboard file names map to post numbers: P07.dc.html -> Post-07.jpg, P15-3.dc.html ->
// Post-15-3.jpg. An artboard named Main.dc.html is treated as Post 1 unless
// MAIN_AS=<name> is set (e.g. MAIN_AS=P01).
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path"), crypto = require("crypto");
const [project, images, assetsFile, out, fontsDir] = process.argv.slice(2);
if (!out) { console.error("usage: render_designs.js <project_dir> <images_dir> <assets.json> <out_dir> [fonts_dir]"); process.exit(2); }
fs.mkdirSync(out, { recursive: true });

const bySha = {};
for (const f of fs.readdirSync(images)) {
  const p = path.join(images, f); if (!fs.statSync(p).isFile()) continue;
  bySha[crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex")] = p;
}
const assets = JSON.parse(fs.readFileSync(assetsFile, "utf8"));
const blobFile = (id) => { const sha = assets[id]; const p = sha && Object.entries(bySha).find(([h]) => h.startsWith(sha) || sha.startsWith(h))?.[1]; return p || null; };

function fontCSS(html) {
  if (!fontsDir) return "";
  const fams = [...html.matchAll(/family=([^:&"']+)/g)].map((m) => decodeURIComponent(m[1].replace(/\+/g, " ")));
  let css = "";
  for (const fam of new Set(fams)) {
    const slug = fam.toLowerCase().replace(/\s+/g, "-"), dir = path.join(fontsDir, "node_modules/@fontsource", slug, "files");
    if (!fs.existsSync(dir)) { console.warn("font not installed:", fam, "(npm i @fontsource/" + slug + ")"); continue; }
    for (const w of [300, 400, 500, 600, 700]) for (const st of ["normal", "italic"]) {
      const f = path.join(dir, `${slug}-latin-${w}-${st}.woff2`);
      if (fs.existsSync(f)) css += `@font-face{font-family:'${fam}';font-weight:${w};font-style:${st};src:url(file://${f})}`;
    }
  }
  return css;
}

(async () => {
  const b = await chromium.launch(); const page = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  const work = fs.mkdtempSync(path.join(require("os").tmpdir(), "dc-render-"));
  const missing = new Set(); let n = 0;
  for (const f of fs.readdirSync(project).filter((x) => x.endsWith(".dc.html")).sort()) {
    const html = fs.readFileSync(path.join(project, f), "utf8");
    if (!html.includes("</helmet>") || !html.includes("</x-dc>")) { console.warn("skip (not an artboard):", f); continue; }
    const body = html.split("</helmet>")[1].split("</x-dc>")[0].replace(/\/_blob\/([0-9a-f]{32})/g, (m, id) => {
      const p = blobFile(id); if (!p) { missing.add(id); return m; } return "file://" + p;
    });
    const w = +(html.match(/"width":(\d+)/) || [])[1] || 1080, h = +(html.match(/"height":(\d+)/) || [])[1] || 1350;
    const base = f === "Main.dc.html" ? (process.env.MAIN_AS || "P01") : f.replace(".dc.html", "");
    const name = base.replace(/^P(\d+)/, (m, d) => "Post-" + d.padStart(2, "0"));
    const tmp = path.join(work, name + ".html");
    fs.writeFileSync(tmp, `<!doctype html><html><head><meta charset=utf-8><style>${fontCSS(html)}body{margin:0}</style></head><body>${body}</body></html>`);
    await page.setViewportSize({ width: w, height: h });
    await page.goto("file://" + tmp); await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(150);
    const broken = await page.evaluate(() => [...document.images].filter((i) => !(i.complete && i.naturalWidth)).length);
    if (broken) console.warn(name + ": " + broken + " image(s) did not load");
    await page.screenshot({ path: path.join(out, name + ".jpg"), type: "jpeg", quality: 90, clip: { x: 0, y: 0, width: w, height: h } });
    n++;
  }
  await b.close();
  if (missing.size) console.warn("No local file matched these canvas images:", [...missing].join(", "));
  console.log(`rendered ${n} artboards to ${out}`);
})();
