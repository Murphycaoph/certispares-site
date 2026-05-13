# CertiSpares Blog Rebuild Handoff - 2026-05-13

## Workspace

- Main project path: `E:\codex\certispares-site`
- Do not continue from the old C-drive project copy.
- Current local dev URL used today: `http://127.0.0.1:4325/blog`
- Build command used repeatedly: `npm.cmd run build`
- Content sync command used after Markdown rewrites: `npx.cmd astro sync --force`

## Standing Content Rules

- CertiSpares is RFQ-first, not a public SKU catalogue.
- Do not claim fake stock, fake price, fake lead time, fake certifications, fake authorization, or exact fitment.
- Brand names, OE numbers, models, and cross references are inquiry identification inputs only.
- Final matching must be confirmed by OE reference, VIN/model data, dimensions, photos, and applicable specifications.
- Blog articles should support sourcing pages, product/system pages, and RFQ/contact conversion.
- Current writing target set by user: about 2000+ words per deep article.
- Style target: short, direct buyer language; less AI narration; more tables, checklists, examples, and RFQ wording.

## Work Completed Today

### Initial GSC Priority Rewrites

Rebuilt 5 priority articles with data tables, sources, RFQ checklists, FAQ, and stronger internal links:

- `src/content/blog/truck-brake-pads-vs-brake-linings-whats-the-difference.md`
- `src/content/blog/how-air-brake-chambers-work-in-heavy-trucks.md`
- `src/content/blog/wheel-hub-heavy-truck-structure-function.md`
- `src/content/blog/how-china-industrial-clusters-shape-auto-parts-supply-chains.md`
- `src/content/blog/payment-terms-auto-parts-trade-tt-lc-explained.md`

Also updated:

- `src/pages/blog/[slug].astro`

Template changes included stronger table styling, code/flowchart panels, blockquote styling, checklist blocks, related cards, and CTA polish.

### Batch 1 - Brake Drum Cluster

Rebuilt 4 articles:

- `src/content/blog/brake-drum-vs-disc-heavy-trucks.md`
- `src/content/blog/truck-brake-drum-lifespan-replacement.md`
- `src/content/blog/truck-brake-drum-manufacturing-process.md`
- `src/content/blog/how-to-choose-brake-drum-suppliers-china.md`

These were expanded with comparison tables, lifecycle logic, manufacturing flow, supplier scorecards, RFQ checklists, FAQ, and source notes.

### Batch 2 - Supplier Risk / QC Cluster

Rebuilt and then expanded after user feedback:

- `src/content/blog/5-risks-sourcing-truck-parts-china.md`
- `src/content/blog/how-to-audit-a-truck-parts-factory-in-china.md`
- `src/content/blog/why-quality-control-matters-commercial-vehicle-parts.md`
- `src/content/blog/oem-vs-aftermarket-truck-parts-in-china-what-global-buyers-should-know.md`
- `src/content/blog/how-to-reduce-sourcing-risk-auto-parts-china.md`

Final approximate word counts:

- `5-risks-sourcing-truck-parts-china.md`: 1615
- `how-to-audit-a-truck-parts-factory-in-china.md`: 1533
- `why-quality-control-matters-commercial-vehicle-parts.md`: 1561
- `oem-vs-aftermarket-truck-parts-in-china-what-global-buyers-should-know.md`: 1615
- `how-to-reduce-sourcing-risk-auto-parts-china.md`: 1891

Note: these are deeper than before but still below the later 2000-word standard, except close to it.

### Batch 3 - Commercial Terms / Quote Decision Cluster

User set a 2000-word standard. Rebuilt 5 articles to meet it:

- `src/content/blog/exw-fob-cif-auto-parts-buyers.md`: 2025
- `src/content/blog/minimum-order-quantity-moq-explained-for-auto-parts-buyers.md`: 2139
- `src/content/blog/how-to-compare-auto-parts-quotations-from-chinese-suppliers.md`: 2061
- `src/content/blog/why-price-alone-should-not-determine-your-auto-parts-supplier.md`: 2104
- `src/content/blog/7-questions-to-ask-before-choosing-an-auto-parts-supplier.md`: 2012

Added Incoterms decision matrices, MOQ negotiation examples, landed-cost logic, supplier scorecards, RFQ/inspection/payment prompts, FAQ, and sources.

### Batch 4 - Brake Drum Testing / Material / Dispute Prevention Cluster

Rebuilt 5 articles to meet 2000-word standard:

- `src/content/blog/how-truck-brake-drums-are-tested.md`: 2019
- `src/content/blog/how-to-inspect-truck-brake-drums-before-shipment.md`: 2000
- `src/content/blog/metallurgy-and-material-control-in-heavy-truck-parts.md`: 2003
- `src/content/blog/how-steel-supply-affects-truck-parts-manufacturing.md`: 2007
- `src/content/blog/how-to-avoid-quality-disputes-when-importing-auto-parts.md`: 2003

Added testing matrices, AQL/sampling logic, defect classification, inspection release notes, material-control workflows, steel-price/grade availability logic, claim evidence templates, and dispute prevention scorecards.

## Sources Used Repeatedly

- CVSA 2024 Brake Safety Week Results: `https://cvsa.org/news/2024-bsw-results/`
- CVSA 2025 International Roadcheck Results: `https://cvsa.org/news/2025-roadcheck-results/`
- eCFR 49 CFR 393.47: `https://ecfr.io/Title-49/Section-393.47`
- ISO 2859-1:2026: `https://www.iso.org/standard/85464.html`
- ICC Incoterms Rules: `https://iccwbo.org/business-solutions/incoterms-rules/`
- International Trade Administration Trade Finance Guide: `https://www.trade.gov/report/trade-finance-guide`
- ITA Letter of Credit page: `https://www.trade.gov/letter-credit`
- World Steel Association automotive steel applications: `https://worldsteel.org/steel-topics/steel-markets/automotive/`
- NSF IATF 16949 overview: `https://www.nsf.org/management-systems/quality-management/iatf-16949-2016`
- OICA 2024 Production Statistics: `https://www.oica.net/2024-production-statistics/`

## Current Git/Build State

- No commit/stage was made today.
- There are many modified blog Markdown files plus `src/pages/blog/[slug].astro`.
- Final build after Batch 4 passed:
  - `npm.cmd run build`
  - output: 73 pages built
- Route checked after Batch 4:
  - `http://127.0.0.1:4325/blog/how-truck-brake-drums-are-tested/`
  - returned `200 OK`

## Remaining Work

At the last full inventory before later batches, there were 41 blog posts total.

Already rebuilt today:

- Initial 5 priority posts
- Brake drum batch: 4
- Risk/QC batch: 5
- Commercial batch: 5
- Testing/material/dispute batch: 5

Total touched blog posts today: 24.

Remaining likely thin posts to prioritize next:

- `src/content/blog/key-components-heavy-truck-suspension-system.md`
- `src/content/blog/common-suspension-failures-heavy-trucks.md`
- `src/content/blog/leaf-springs-in-heavy-trucks-function-failure-and-replacement.md`
- `src/content/blog/torque-rods-in-commercial-vehicles-what-buyers-should-know.md`
- `src/content/blog/stabilizer-bars-in-heavy-trucks-structure-and-purpose.md`
- `src/content/blog/truck-parts-manufacturing-regions-china.md`
- `src/content/blog/why-north-china-strong-heavy-duty-truck-components.md`
- `src/content/blog/why-location-matters-auto-parts-sourcing.md`
- `src/content/blog/how-chinese-auto-parts-industrial-clusters-work.md`
- `src/content/blog/bth-industrial-belt-auto-parts-sourcing.md`
- `src/content/blog/hebei-commercial-vehicle-parts-industry-guide.md`
- `src/content/blog/trading-company-vs-manufacturer-in-china.md`
- `src/content/blog/how-to-build-a-reliable-supplier-network-in-china.md`
- `src/content/blog/common-wear-parts-commercial-vehicles-replacement-cycle.md`
- `src/content/blog/why-inland-logistics-matters-in-heavy-cargo-trade.md`

Suggested next batch:

Suspension product cluster:

- `key-components-heavy-truck-suspension-system.md`
- `common-suspension-failures-heavy-trucks.md`
- `leaf-springs-in-heavy-trucks-function-failure-and-replacement.md`
- `torque-rods-in-commercial-vehicles-what-buyers-should-know.md`
- `stabilizer-bars-in-heavy-trucks-structure-and-purpose.md`

Target each article at 2000+ words with tables, inspection points, RFQ fields, failure signals, sourcing risks, FAQ, and links to `/product/part/suspension-parts/`, `/sourcing`, `/capabilities`, and `/contact`.

## Tomorrow Startup Checklist

1. Open `E:\codex\certispares-site`.
2. Run `git status --short`.
3. Run a fresh word-count inventory for `src/content/blog/*.md`.
4. Continue with the suspension cluster unless the user redirects.
5. Keep 2000+ words per article.
6. After each batch run:
   - `npx.cmd astro sync --force`
   - `npm.cmd run build`
   - one local `curl.exe -I` route check.
