# CertiSpares Insights Image Rebuild Brief - 2026-05-08

This brief defines the image set for rebuilding the current `/blog/` page into a Sourcing Insights / RFQ knowledge base experience.

Use it before generating images, sourcing web images, or replacing local assets. The goal is to avoid repeated generic photos and build a consistent industrial sourcing visual system.

## Page Role

The Insights page should feel like a practical sourcing knowledge center, not a traditional blog.

Primary buyer question:

> What practical knowledge helps me submit, clarify, compare, and control a commercial vehicle parts RFQ?

The images must support this RFQ-first role. They should show sourcing situations, document handling, parts checking, supplier comparison, packing, and logistics control.

## Visual Direction

Use this common style across all generated or sourced images:

- industrial documentary photography
- commercial vehicle aftermarket sourcing context
- deep navy, steel gray, white, and cool warehouse lighting
- real parts, cartons, pallets, spreadsheets, checklists, measuring tools, and loading scenes
- mostly no people; hands are acceptable when they show inspection, writing, labeling, or measuring
- clean compositions with clear subject recognition at card size
- realistic but polished, suitable for a B2B sourcing site
- no visible brand logos, license plates, supplier names, QR codes, real certificate numbers, or personal data

Avoid:

- generic lifestyle business photos
- smiling office teams or handshake imagery
- exaggerated sci-fi or SaaS dashboard visuals
- fake inventory abundance
- claims implied by visuals, such as authorized dealer status, certified stock, guaranteed fitment, or ready-to-ship warehouse scale
- heavily blurred, dark, abstract, or atmospheric images where the buyer cannot identify the sourcing scenario

## Asset Path Plan

Target folder:

```text
public/images/insights/
```

Preferred production format:

```text
.webp
```

Recommended sizes:

- Hero: 2400 x 1200
- Topic cards: 1200 x 800
- Problem cards: 1000 x 700
- Article cards: 1200 x 800
- Platform overview: 1600 x 900
- Small system icons or thumbnails: 800 x 800 if photographic, SVG if icon-based

## Required First Batch

The first rebuild should use 16 core images.

| ID | File name | Page use | Image content | Notes |
|---|---|---|---|---|
| INS-hero-01 | `insights-hero-sourcing-yard.webp` | Hero background | Evening or night commercial vehicle parts warehouse with loading bay, pallets, cartons, and a container truck in a cool blue-gray industrial scene | Should feel like sourcing operations, not a logistics ad. Keep enough dark negative space for white hero text. |
| INS-topic-01 | `insights-topic-rfq-clarification.webp` | RFQ Clarification topic card | RFQ sheet, parts reference photos, OE/part number notes, caliper, and pen on an industrial desk | Show incomplete-but-usable RFQ inputs. Do not show real OE numbers or sensitive documents. |
| INS-topic-02 | `insights-topic-supplier-comparison.webp` | Supplier Comparison topic card | Similar commercial vehicle parts on an inspection table with a quotation comparison sheet nearby | Must imply same-basis comparison, not price-only shopping. |
| INS-topic-03 | `insights-topic-qc-inspection.webp` | QC & Inspection topic card | Caliper measuring a metal truck part, with inspection checklist and neutral workshop background | Make the measurement action clear at thumbnail size. |
| INS-topic-04 | `insights-topic-consolidation-logistics.webp` | Consolidation & Logistics topic card | Mixed cartons and pallets staged near a container, with a simple loading plan sheet | Show coordination and mixed-SKU consolidation without implying huge stock ownership. |
| INS-topic-05 | `insights-topic-packing-documents.webp` | Packing & Documents topic card | Cartons with neutral labels, packing list, document folder, carton mark stickers, and shipping paperwork | Labels should be generic and non-identifying. |
| INS-topic-06 | `insights-topic-aftermarket-replenishment.webp` | Aftermarket Replenishment topic card | Assorted truck parts grouped by type beside a replenishment spreadsheet or printed list | Must show mixed fast-moving / slow-moving replenishment logic. |
| INS-problem-01 | `insights-problem-wrong-quotation.webp` | RFQ problem card | Two visually similar parts with different dimensions, one marked with a neutral warning tag | Visual message: unclear references can lead to wrong quotation. |
| INS-problem-02 | `insights-problem-mixed-specifications.webp` | RFQ problem card | Different specs, dimensions, and part samples spread around a comparison sheet | Visual message: comparisons fail when specs are mixed. |
| INS-problem-03 | `insights-problem-supplier-gap.webp` | RFQ problem card | A long replenishment list with several rows marked pending or missing, next to grouped parts | Visual message: one supplier may not cover the whole list. |
| INS-problem-04 | `insights-problem-packing-inconsistency.webp` | RFQ problem card | Inconsistent carton sizes or neutral label placement being checked against a packing note | Visual message: packing problems appear late without checkpoints. |
| INS-article-01 | `insights-article-brake-chamber-rfq.webp` | Article card | Brake chambers or air brake components on a clean inspection bench with caliper and spec notes | For article: "Why Brake Chamber RFQs Often Need More Details". |
| INS-article-02 | `insights-article-beyond-unit-price.webp` | Article card | Spreadsheet with MOQ, lead time, packing, document readiness columns beside sample parts | For article: "Comparing Suppliers Beyond Unit Price". |
| INS-article-03 | `insights-article-container-planning.webp` | Article card | Warehouse loading area with cartons, pallets, CBM notes, and container planning sheet | For article: "How Container Planning Affects Landed Cost". |
| INS-article-04 | `insights-article-packing-list-carton-marks.webp` | Article card | Packing list, carton mark labels, carton number stickers, and shipment document folder | For article: "Packing List & Carton Marks: Small Details, Big Impact". |
| INS-platform-01 | `insights-platform-sourcing-overview.webp` | Browse by Truck Platform support image | Neutral commercial vehicle silhouettes, parts notes, and platform sourcing checklist, without brand logos | Use as a general visual bridge to HOWO, Shacman, Dongfeng, Foton, JAC links. |

## Optional Second Batch

These can be created after the first layout is approved.

| ID | File name | Page use | Image content |
|---|---|---|---|
| INS-system-01 | `insights-system-brake.webp` | Part system tile | Brake disc, chamber, pad, or valve detail on a clean light industrial surface |
| INS-system-02 | `insights-system-engine.webp` | Part system tile | Engine components or filters arranged with a spec sheet |
| INS-system-03 | `insights-system-suspension.webp` | Part system tile | Suspension parts such as shock absorber, bushing, or spring detail |
| INS-system-04 | `insights-system-cooling.webp` | Part system tile | Radiator, hose, or cooling component detail |
| INS-system-05 | `insights-system-rubber.webp` | Part system tile | Rubber bushings, mounts, or seals with caliper |
| INS-system-06 | `insights-system-air-system.webp` | Part system tile | Air valve, fittings, or pneumatic hose components |

For the first page rebuild, system entries can use clean icons instead of photos. Use this optional batch only if photographic system tiles are needed.

## Prompt Building Rules

When generating images, every prompt should include:

- commercial vehicle aftermarket sourcing
- industrial warehouse or inspection bench context
- realistic documentary photography
- cool navy and steel gray color grading
- no visible logos, no license plates, no readable brand names
- no people except hands if needed
- no fake prices, no stock signs, no certificates

Example base prompt structure:

```text
Realistic industrial documentary photograph for a B2B commercial vehicle parts sourcing website. [specific scene]. Cool navy and steel gray warehouse lighting, clean professional composition, no visible brand logos, no license plates, no readable company names, no people except hands if necessary, no fake prices or certificates.
```

## Cropping Guidance

Hero:

- key subject should sit center-right or far-right
- left side should support dark overlay and large headline text
- avoid important details at extreme top where navigation overlaps

Topic and article cards:

- subject should be recognizable in a 16:9 or 3:2 crop
- leave mild negative space for image overlays or tags
- avoid tiny document text that becomes messy at small size

Problem cards:

- use simple, legible scenes
- one clear problem per image
- avoid clutter unless the clutter itself represents mixed specifications

## Acceptance Checklist

Before using an image on the page:

1. Does it make the sourcing or RFQ situation concrete?
2. Can the buyer understand the image at card size?
3. Does it avoid fake stock, fake price, fake lead time, fake authorization, and fake fitment?
4. Does it avoid visible logos, plate numbers, real documents, or private data?
5. Does it match the deep navy / white / steel gray industrial visual system?
6. Does it reduce repeated imagery across the page?
7. Does it move the Insights page away from a traditional blog feel?

