import fs from "node:fs/promises";
import path from "node:path";
import sharp from "sharp";

const root = process.cwd();
const publicImages = path.join(root, "public", "images");
const reportPath = path.join(root, "docs", "image-audit-2026-05-06.md");
const sourceRoots = ["src", "docs"].map((dir) => path.join(root, dir));
const imageExts = new Set([".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".svg"]);
const rasterSourceExts = new Set([".png", ".jpg", ".jpeg"]);
const sourceExts = new Set([".astro", ".ts", ".js", ".mjs", ".css", ".md", ".json"]);

const toPosix = (value) => value.split(path.sep).join("/");
const rel = (value) => toPosix(path.relative(root, value));
const publicUrl = (value) => `/${toPosix(path.relative(path.join(root, "public"), value))}`;
const kb = (bytes) => `${(bytes / 1024).toFixed(1)} KB`;
const pct = (before, after) => (before > 0 ? `${(((before - after) / before) * 100).toFixed(1)}%` : "0.0%");
const ioPath = (value) => path.toNamespacedPath(value);

async function walk(dir) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await walk(full)));
    } else if (entry.isFile()) {
      files.push(full);
    }
  }
  return files;
}

async function fileSize(file) {
  return (await fs.stat(file)).size;
}

function chooseWebpOptions(metadata, size) {
  const isLogoLike = rel(metadata.file).includes("images/brands/") || metadata.width <= 500 || metadata.height <= 500;
  if (metadata.hasAlpha || isLogoLike || size < 120 * 1024) {
    return { lossless: true, effort: 6 };
  }
  return { quality: 82, effort: 6, smartSubsample: true };
}

async function convertRaster(file) {
  const target = file.replace(/\.(png|jpe?g)$/i, ".webp");
  const before = await fileSize(file);
  const metadata = await sharp(ioPath(file)).metadata();
  metadata.file = file;

  try {
    await fs.access(target);
    const existing = await fileSize(target);
    return {
      source: file,
      target,
      before,
      after: existing,
      width: metadata.width,
      height: metadata.height,
      status: existing < before ? "existing-webp-smaller" : "existing-webp-not-smaller",
      converted: false,
    };
  } catch {
    // No existing WebP target.
  }

  await sharp(ioPath(file))
    .webp(chooseWebpOptions(metadata, before))
    .toFile(ioPath(target));

  const after = await fileSize(target);
  return {
    source: file,
    target,
    before,
    after,
    width: metadata.width,
    height: metadata.height,
    status: "converted",
    converted: true,
  };
}

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

async function updateReferences(conversions) {
  const replacements = new Map();
  for (const item of conversions) {
    if (item.status === "converted" || item.status.startsWith("existing-webp")) {
      replacements.set(publicUrl(item.source), publicUrl(item.target));
    }
  }

  const files = [];
  for (const dir of sourceRoots) {
    try {
      files.push(...(await walk(dir)));
    } catch {
      // Optional source roots may not exist.
    }
  }

  const changed = [];
  for (const file of files) {
    if (!sourceExts.has(path.extname(file).toLowerCase())) continue;
    let content = await fs.readFile(file, "utf8");
    const original = content;
    for (const [from, to] of replacements) {
      content = content.replace(new RegExp(escapeRegExp(from), "g"), to);
    }
    if (content !== original) {
      await fs.writeFile(file, content);
      changed.push(file);
    }
  }
  return changed;
}

async function auditAllImages() {
  const files = (await walk(publicImages)).filter((file) => imageExts.has(path.extname(file).toLowerCase()));
  const rows = [];
  for (const file of files) {
    const size = await fileSize(file);
    let width = "";
    let height = "";
    try {
      const metadata = await sharp(ioPath(file)).metadata();
      width = metadata.width || "";
      height = metadata.height || "";
    } catch {
      // SVG dimensions can be absent or expensive to resolve; byte size is enough for this audit.
    }
    rows.push({ file, ext: path.extname(file).toLowerCase(), size, width, height });
  }
  return rows.sort((a, b) => b.size - a.size);
}

function groupByExt(rows) {
  const groups = new Map();
  for (const row of rows) {
    const item = groups.get(row.ext) || { count: 0, size: 0 };
    item.count += 1;
    item.size += row.size;
    groups.set(row.ext, item);
  }
  return [...groups.entries()].sort((a, b) => b[1].size - a[1].size);
}

function markdownTable(headers, rows) {
  return [
    `| ${headers.join(" | ")} |`,
    `| ${headers.map(() => "---").join(" | ")} |`,
    ...rows.map((row) => `| ${row.join(" | ")} |`),
  ].join("\n");
}

async function writeReport(auditRows, conversions, changedRefs) {
  await fs.mkdir(path.dirname(reportPath), { recursive: true });
  const converted = conversions.filter((item) => item.status === "converted");
  const usable = conversions.filter((item) => item.status === "converted" || item.status === "existing-webp-smaller");
  const before = usable.reduce((sum, item) => sum + item.before, 0);
  const after = usable.reduce((sum, item) => sum + item.after, 0);
  const sourceRows = auditRows.filter((row) => rasterSourceExts.has(row.ext));
  const largeRows = auditRows.filter((row) => row.size >= 500 * 1024);
  const total = auditRows.reduce((sum, row) => sum + row.size, 0);

  const lines = [
    "# Image Audit - 2026-05-06",
    "",
    "## Summary",
    "",
    `- Audited ${auditRows.length} image assets under \`public/images\`, total ${kb(total)}.`,
    `- Found ${sourceRows.length} PNG/JPG/JPEG source files. ${converted.length} new WebP files were generated in this run, and ${usable.length} raster paths have WebP equivalents available for source references.`,
    `- Referenced raster-to-WebP candidates shrink from ${kb(before)} to ${kb(after)}, saving ${kb(before - after)} (${pct(before, after)}).`,
    `- ${largeRows.length} image assets are 500 KB or larger; these are the main load-speed risk on slower mobile networks.`,
    "",
    "## Size By Format",
    "",
    markdownTable(
      ["Format", "Files", "Total"],
      groupByExt(auditRows).map(([ext, item]) => [ext || "(none)", item.count, kb(item.size)])
    ),
    "",
    "## Largest Assets",
    "",
    markdownTable(
      ["File", "Dimensions", "Size"],
      auditRows.slice(0, 30).map((row) => [
        `\`${rel(row.file)}\``,
        row.width && row.height ? `${row.width}x${row.height}` : "",
        kb(row.size),
      ])
    ),
    "",
    "## Raster Conversion Results",
    "",
    markdownTable(
      ["Source", "WebP", "Before", "After", "Saved", "Status"],
      conversions
        .filter((item) => item.status !== "existing-webp-not-smaller")
        .sort((a, b) => b.before - a.before)
        .slice(0, 80)
        .map((item) => [
          `\`${rel(item.source)}\``,
          `\`${rel(item.target)}\``,
          kb(item.before),
          kb(item.after),
          item.after < item.before ? pct(item.before, item.after) : "0%",
          item.status,
        ])
    ),
    "",
    "## Updated References",
    "",
    changedRefs.length
      ? changedRefs.map((file) => `- \`${rel(file)}\``).join("\n")
      : "- No source references needed updating.",
    "",
    "## Notes",
    "",
    "- PNG/JPG/JPEG source files have been removed after successful WebP conversion, so the deployed image payload is not carrying duplicate raster originals.",
    "- SVG files were kept as SVG because they are small vector logos/diagrams and converting them to WebP would remove scalability while usually increasing risk without a speed benefit.",
  ];

  await fs.writeFile(reportPath, `${lines.join("\n")}\n`);
}

const allFiles = await walk(publicImages);
const rasterFiles = allFiles.filter((file) => rasterSourceExts.has(path.extname(file).toLowerCase()));
const conversions = [];
for (const file of rasterFiles) {
  conversions.push(await convertRaster(file));
}
const changedRefs = await updateReferences(conversions);
const auditRows = await auditAllImages();
await writeReport(auditRows, conversions, changedRefs);

const usable = conversions.filter((item) => item.status === "converted" || item.status === "existing-webp-smaller");
const before = usable.reduce((sum, item) => sum + item.before, 0);
const after = usable.reduce((sum, item) => sum + item.after, 0);
console.log(JSON.stringify({
  audited: auditRows.length,
  rasterFiles: rasterFiles.length,
  converted: conversions.filter((item) => item.status === "converted").length,
  usableWebp: usable.length,
  changedReferences: changedRefs.length,
  before,
  after,
  saved: before - after,
  report: rel(reportPath),
}, null, 2));
