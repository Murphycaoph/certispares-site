# Image Audit - 2026-05-06

## Summary

- Audited 266 image assets under `public/images`, total 54207.3 KB.
- Found 0 PNG/JPG/JPEG source files. 0 new WebP files were generated in this run, and 0 raster paths have WebP equivalents available for source references.
- Referenced raster-to-WebP candidates shrink from 0.0 KB to 0.0 KB, saving 0.0 KB (0.0%).
- 13 image assets are 500 KB or larger; these are the main load-speed risk on slower mobile networks.

## Size By Format

| Format | Files | Total |
| --- | --- | --- |
| .webp | 251 | 54175.5 KB |
| .svg | 15 | 31.8 KB |

## Largest Assets

| File | Dimensions | Size |
| --- | --- | --- |
| `public/images/Suspension.webp` | 2730x1535 | 3060.6 KB |
| `public/images/social/container-consolidation-series/01-traditional-buying-friction.webp` | 6000x4000 | 2816.2 KB |
| `public/images/sourcing/traditional-buying-friction.webp` | 6000x4000 | 2816.2 KB |
| `public/images/Brake-System.webp` | 2048x2048 | 2448.5 KB |
| `public/images/Engine-Parts.webp` | 2730x1535 | 2248.8 KB |
| `public/images/sourcing/comparison-logic-team.webp` | 5200x3467 | 2104.6 KB |
| `public/images/social/container-consolidation-series/03-balanced-sku-sourcing.webp` | 5790x3860 | 1887.8 KB |
| `public/images/sourcing/balanced-sku-inventory.webp` | 5790x3860 | 1887.8 KB |
| `public/images/insights-hero-collage.webp` | 2560x420 | 845.8 KB |
| `public/images/platform-downloads/banded/Suspension heavy truck 3.webp` | 1200x900 | 516.4 KB |
| `public/images/platform-downloads/official-batch-3/Suspension Hendrickson Airtek NXT Crane.webp` | 1200x900 | 516.4 KB |
| `public/images/platform-library/suspension/fallback/Suspension heavy truck 3.webp` | 1200x900 | 516.4 KB |
| `public/images/platform-library/suspension/hendrickson/Suspension Hendrickson Airtek NXT Crane.webp` | 1200x900 | 516.4 KB |
| `public/images/platform-downloads/banded/Axle heavy truck 3.webp` | 1188x950 | 481.6 KB |
| `public/images/platform-downloads/official-batch-4/Axle Hendrickson TRLAXLE.webp` | 1188x950 | 481.6 KB |
| `public/images/platform-library/axle/fallback/Axle heavy truck 3.webp` | 1188x950 | 481.6 KB |
| `public/images/platform-library/axle/hendrickson/Axle Hendrickson TRLAXLE.webp` | 1188x950 | 481.6 KB |
| `public/images/platform-downloads/banded/Axle light truck 1.webp` | 2232x1932 | 473.1 KB |
| `public/images/platform-fallbacks/Axle light truck 1.webp` | 2232x1932 | 473.1 KB |
| `public/images/platform-library/axle/fallback/Axle light truck 1.webp` | 2232x1932 | 473.1 KB |
| `public/images/china-industrial-warehouse.webp` | 1909x1272 | 465.4 KB |
| `public/images/social/container-consolidation-series/04-cost-and-inventory-efficiency.webp` | 1600x2400 | 454.7 KB |
| `public/images/sourcing/advantage-warehouse-shelves.webp` | 1600x2400 | 454.7 KB |
| `public/images/sourcing/friction-container-yard.webp` | 1600x1066 | 393.8 KB |
| `public/images/logistics-container-export-port.webp` | 2000x1124 | 382.2 KB |
| `public/images/platform-downloads/banded/Axle medium truck 1.webp` | 1200x727 | 373.2 KB |
| `public/images/platform-downloads/official-batch-3/Axle Hendrickson Composilite EXS20.webp` | 1200x727 | 373.2 KB |
| `public/images/platform-fallbacks/Axle medium truck 1.webp` | 1200x727 | 373.2 KB |
| `public/images/platform-library/axle/fallback/Axle medium truck 1.webp` | 1200x727 | 373.2 KB |
| `public/images/platform-library/axle/hendrickson/Axle Hendrickson Composilite EXS20.webp` | 1200x727 | 373.2 KB |

## Raster Conversion Results

| Source | WebP | Before | After | Saved | Status |
| --- | --- | --- | --- | --- | --- |

## Updated References

- No source references needed updating.

## Non-Image Performance Opportunities

| Area | Current Finding | Impact | Suggested Optimization |
| --- | --- | --- | --- |
| CSS delivery | `astro.config.mjs` uses `build.inlineStylesheets: "always"`, so every generated HTML page carries its own CSS. | HTML is larger and repeat visitors cannot reuse a shared cached stylesheet across pages. | Consider changing to external hashed CSS for shared styles, especially once visual layout stabilizes. |
| Third-party analytics | Google Analytics `gtag.js` is loaded on all 72 generated pages from `BaseLayout.astro`. | Adds DNS/TLS/third-party JS work on every first page load. | Delay analytics until after page load/idle, or load only after consent/interaction if business tracking allows. |
| Inline JavaScript | The built site contains 161 `<script>` tags across 72 pages, mostly inline navigation and page interaction scripts. | Repeated inline scripts cannot be cached as shared assets and add parse work per page. | Move common scripts such as the mobile drawer into a small shared module, and keep page scripts only where needed. |
| Cache headers | `netlify.toml` currently only defines build and publish settings. | Static assets may not get an explicit long-lived immutable cache policy. | Add Netlify headers for `/images/*.webp`, `/images/*.svg`, and hashed framework assets with `Cache-Control: public, max-age=31536000, immutable`. |
| HTML size | Largest generated HTML pages are about 48-63 KB, led by blog archive and tag pages. | This is not severe, but it adds transfer and parse cost, especially with inline CSS. | After moving shared CSS/JS out of HTML, reassess whether archive/tag pages need pagination or smaller embedded data. |
| LCP image discovery | Several hero images are CSS backgrounds; only the homepage explicitly preloads its main hero image. | Browser discovery of CSS background LCP images can be later than `<img>` or explicit preload. | For high-traffic hero pages, add targeted image preloads or convert hero backgrounds to real `<img>` elements with `fetchpriority="high"`. |

## Notes

- PNG/JPG/JPEG source files have been removed after successful WebP conversion, so the deployed image payload is not carrying duplicate raster originals.
- SVG files were kept as SVG because they are small vector logos/diagrams and converting them to WebP would remove scalability while usually increasing risk without a speed benefit.
