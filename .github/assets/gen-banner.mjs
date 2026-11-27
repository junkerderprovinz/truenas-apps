/**
 * The store banner, in the layout of the GitHub style guide: the TrueNAS mark on the
 * left (largest ink 400px, ink-left x=165, centred on y=250), the name to its
 * right in Bree Serif Regular at a cap height of 110, since the TrueNAS wordmark is part
 * of an image, and one Bree Light claim below it. Light and dark variants for the README's
 * <picture>; the single-colour mark takes the text colour of each.
 *
 * Text is rendered at the origin and placed with a transform, because
 * opentype.js emits NaN control points for some glyphs at large offsets.
 * Deps (global): opentype.js, @resvg/resvg-js, and the house fonts as TTF in
 * HOUSE_FONTS (default %LOCALAPPDATA%\halleluja-fonts).
 * Run: node .github/assets/gen-banner.mjs
 */
import { readFileSync, writeFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { tmpdir } from "node:os";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";

const require = createRequire(import.meta.url);
const groot = execSync("npm root -g").toString().trim();
const opentype = require(`${groot}/opentype.js`);
const { Resvg } = require(`${groot}/@resvg/resvg-js`);
const DIR = dirname(fileURLToPath(import.meta.url));

const NAME = "TrueNAS";
const CLAIM = "One paste, one app.";

const MARK = {
  vb: "0 0 24 24",
  content: `<path fill="COLOR" d="M24 10.049v5.114l-10.949 6.324v-5.114L24 10.049zm-24 0v5.114l10.956 6.324v-5.114L0 10.049zm12.004-.605l-4.433 2.559 4.433 2.559 4.429-2.559-4.429-2.559zm10.952-1.207l-9.905-5.723v5.118l5.473 3.164 4.432-2.559zm-12-.605V2.513L1.044 8.236l4.432 2.555 5.48-3.159z"/>`,
};

const W = 1600, H = 500, LOGO_INK = 400, LOGO_X = 165, GAP_LOGO_TEXT = 70, GAP_NAME_CLAIM = 16, CLAIM_SIZE = 44;
const TARGET_CAP = 110;
const THEMES = [
  { suf: "", bg: "#ffffff", name: "#1f2328", claim: "#5a5d5e" },
  { suf: "-dark", bg: "#0d1117", name: "#e6edf3", claim: "#9aa4ad" },
];

// The house typeface is licensed, so it is read from a local folder and never committed.
const fonts = process.env.HOUSE_FONTS ?? join(process.env.LOCALAPPDATA ?? tmpdir(), "halleluja-fonts");
const bree = opentype.parse(readFileSync(join(fonts, "bree-serif-regular.ttf")).buffer);
const claimFont = opentype.parse(readFileSync(join(fonts, "bree-light.ttf")).buffer);
const bbox = (vb, content) =>
  new Resvg(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="${vb}">${content}</svg>`, { fitTo: { mode: "original" } }).getBBox();

const mb = bbox(MARK.vb, MARK.content.replace(/COLOR/g, "#000"));
const sM = LOGO_INK / Math.max(mb.width, mb.height);
const markTX = LOGO_X - mb.x * sM, markTY = H / 2 - (mb.height * sM) / 2 - mb.y * sM;
const textX = LOGO_X + mb.width * sM + GAP_LOGO_TEXT;

const capRatio = bbox("0 0 600 400", `<path d="${bree.getPath("H", 0, 300, 200).toPathData(2)}"/>`).height / 200;
const nameSize = TARGET_CAP / capRatio;
const nb = bbox("0 0 2000 800", `<path d="${bree.getPath(NAME, 0, 500, nameSize).toPathData(2)}"/>`);
const nameH = nb.height;
const nameD = bree.getPath(NAME, 0, 0, nameSize).toPathData(2);

const claimScale = CLAIM_SIZE / claimFont.unitsPerEm;
const claimAsc = claimFont.ascender * claimScale, claimDesc = -claimFont.descender * claimScale;
const top = H / 2 - (nameH + GAP_NAME_CLAIM + claimAsc + claimDesc) / 2;
const claimBaseline = Math.round(top + nameH + GAP_NAME_CLAIM + claimAsc);
const claimD = claimFont.getPath(CLAIM, 0, 0, CLAIM_SIZE, { kerning: false }).toPathData(2);
if (claimD.includes("NaN")) throw new Error("claim path has NaN points");

for (const t of THEMES) {
  const svg = `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="${NAME}: ${CLAIM}">
  <rect width="${W}" height="${H}" fill="${t.bg}"/>
  <g transform="translate(${markTX.toFixed(2)},${markTY.toFixed(2)}) scale(${sM.toFixed(5)})">${MARK.content.replace(/COLOR/g, t.name)}</g>
  <g transform="translate(${textX.toFixed(2)},${(top - (nb.y - 500)).toFixed(2)})"><path d="${nameD}" fill="${t.name}"/></g>
  <g transform="translate(${textX.toFixed(2)},${claimBaseline})"><path d="${claimD}" fill="${t.claim}"/></g>
</svg>
`;
  writeFileSync(join(DIR, `banner${t.suf}.svg`), svg);
  writeFileSync(join(DIR, `banner${t.suf}.png`), new Resvg(svg, { background: t.bg, fitTo: { mode: "original" } }).render().asPng());
}
console.log(`truenas-apps banner: name at x ${textX.toFixed(0)}, right margin ${(W - textX - nb.width).toFixed(0)}`);
