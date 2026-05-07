# CertiRun Style Application Report - 2026-05-07

## Scope

This record documents the first selective application of CertiRun design language to CertiSpares.

Local source references:

- `C:\Users\caope\certirun-site`
- `C:\Users\caope\certispares-site`

No online CertiRun pages were used as comparison sources for this implementation pass.

## Design Direction

The chosen direction is not to make CertiSpares a full CertiRun copy. CertiSpares keeps its commercial vehicle sourcing identity, industry photography, truck-parts RFQ positioning, and dark hero language. The applied changes import CertiRun's more disciplined B2B design system qualities:

- clearer typography
- less decorative card styling
- more restrained navy/white/gray color hierarchy
- tighter radius rules
- lighter shadows
- stronger section and workflow structure

## Applied Changes

### 1. Typography

CertiSpares now loads and uses the CertiRun typography pair:

- Body: `Inter`
- Headings, labels, badges, and key titles: `Work Sans`

Implementation file:

- `src/layouts/BaseLayout.astro`

Rationale:

This gives CertiSpares a more controlled B2B interface feeling while keeping the current English content and sourcing positioning intact.

### 2. Design Tokens

The global token set was expanded with CertiRun-style primitives:

- navy brand anchor: `#0A2540`
- CertiSpares action blue retained as secondary accent: `#3957E9`
- neutral backgrounds: `#F7F9FC`, `#EEF5FC`
- border: `#DFE6E9`
- lighter surface shadows
- spacing tokens from `--space-1` through `--space-20`
- radius tokens: `--radius-card`, `--radius-sm`, `--radius-md`, `--radius-pill`

Implementation file:

- `src/layouts/BaseLayout.astro`

Rationale:

CertiRun has a clearer system-level foundation. This pass gives CertiSpares the same kind of reusable design vocabulary for later page-by-page refinement.

### 3. Buttons

Button styling changed from brighter gradient-led treatment to a more restrained hierarchy:

- primary: deep navy
- secondary: CertiSpares blue
- outline/default: light gray surface
- radius tightened to `8px`
- hover remains subtle with small vertical movement

Implementation file:

- `src/layouts/BaseLayout.astro`

Rationale:

The primary CTA now feels more like a serious sourcing/operations action. The bright blue remains available for high-emphasis conversion moments without dominating every control.

### 4. Cards

Global card treatment was adjusted toward CertiRun's card discipline:

- radius standardized around `8px`
- lighter shadows
- clearer borders
- hover state uses subtle lift and border emphasis
- card headings now use `Work Sans`

Implementation files:

- `src/layouts/BaseLayout.astro`
- `src/pages/index.astro`

Rationale:

CertiSpares had many card surfaces with heavier shadow and rounder styling. This pass makes cards quieter and easier to scan, especially on RFQ, workflow, and content sections.

### 5. Header and Footer

Header:

- retained dark/navy CertiSpares identity
- shifted the base navy toward CertiRun's `#0A2540`
- simplified active underline to a clean white rule

Footer:

- moved from dark footer to light neutral footer
- social icons now use white surfaces and navy icons
- footer links use thin bottom rules and quieter text hierarchy

Implementation file:

- `src/layouts/BaseLayout.astro`

Rationale:

The header can stay brand-heavy because CertiSpares relies on visual trust and RFQ conversion. The footer benefits from CertiRun's cleaner utility style.

### 6. Homepage Refinement

Homepage changes focused on visual language rather than content replacement:

- hero side card radius reduced to `8px`
- hero side card now has a CertiRun-style left emphasis border
- secondary hero button changed to a translucent dark-surface outline
- KPI cards tightened to `8px`
- section titles use the new heading font and stronger spacing
- brand marquee cards and inner surfaces reduced to `8px`
- strategy cards use image + structured body layout
- workflow cards now use a four-step RFQ-to-shipment model with left accent border and circular step markers
- chips and tags changed from pill-heavy styling to `8px` operational labels

Implementation file:

- `src/pages/index.astro`

Rationale:

The homepage keeps CertiSpares' truck-parts and sourcing imagery, while its service and process sections now feel closer to CertiRun's operational, structured B2B language.

## What Was Intentionally Not Changed

- No full conversion to CertiRun's white split hero was done.
- No broad rewrite of all interior pages was attempted in this pass.
- Existing commercial vehicle photos and RFQ content were preserved.
- The dark CertiSpares header identity was retained.
- Existing uncommitted image conversion work in the repository was not reverted or reorganized.

## Recommended Next Pass

1. Apply the same card and section system to `capabilities`, `how-it-works`, `sourcing`, and `product`.
2. Create reusable Astro UI components similar to CertiRun's `Badge`, `Card`, `HeadingBlock`, and `Section`.
3. Replace repeated page-local CSS with shared design primitives.
4. Audit all product and brand detail pages for large radius, heavy shadow, and inconsistent blue usage.
5. Decide whether the header should stay dark navy or later move to a white CertiRun-style header.

## Verification

Build verification was run after this pass with:

```bash
npm run build
```

Result:

- First run failed because Astro telemetry attempted to create a config directory outside the workspace sandbox.
- Re-run with `ASTRO_TELEMETRY_DISABLED=1` completed successfully.
- Astro built 73 static pages.

## Follow-up Pass: Hero Consistency

Date: 2026-05-07

Scope scanned:

- `src/pages/about.astro`
- `src/pages/blog.astro`
- `src/pages/blog/[slug].astro`
- `src/pages/capabilities.astro`
- `src/pages/cases.astro`
- `src/pages/contact.astro`
- `src/pages/how-it-works.astro`
- `src/pages/index.astro`
- `src/pages/product.astro`
- `src/pages/sourcing.astro`
- `src/components/BrandInquiryPage.astro`
- `src/components/PartInquiryPage.astro`

Findings:

- The site had multiple hero patterns: dark `pageHero`, image-based `.hero`, homepage carousel hero, and product/detail component heroes.
- Several hero sections used different padding, heading sizes, background treatments, and panel radii.
- Some `pageHero` sections were being wrapped by a large glass container, making them feel like a different page family.

Changes applied:

- Added a shared non-home hero rule in `src/layouts/BaseLayout.astro`.
- Standardized non-home hero spacing, title scale, eyebrow style, lead copy color, dark overlay, and panel treatment.
- Removed the old `pageHero .container` glass-card treatment so page heroes read as a full-width hero band.
- Kept the homepage carousel hero as a deliberate exception by adding `homeHero` in `src/pages/index.astro`.
- Standardized hero panels and supporting hero notes to `8px` radius with a restrained left emphasis border.

Verification:

```bash
ASTRO_TELEMETRY_DISABLED=1 npm run build
```

Result:

- Astro built 73 static pages successfully.
