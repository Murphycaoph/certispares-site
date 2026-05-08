# CertiSpares Project Context

This file is the standing context document for CertiSpares execution work. Read it before making content, routing, SEO, schema, design, or implementation decisions in this repository.

Source context: `C:/Users/caope/Desktop/总纲/deep-research-report-certispares.md`

## Core Positioning

CertiSpares is an RFQ-first commercial vehicle aftermarket sourcing site.

It is:

- an inquiry-based sourcing entry point for commercial vehicle aftermarket buyers
- an independent sourcing, supplier comparison, QC, documentation, and export coordination service
- focused on helping importers, distributors, wholesalers, and fleet maintenance buyers prepare and submit structured RFQs
- stronger in heavy-duty commercial vehicle systems, with room for selected light-commercial coverage

It is not:

- a public SKU database
- a full online product catalogue
- an OEM-authorized dealer site unless explicit authorization is stated
- a factory or manufacturer
- a generic company brochure
- a place to publish fake stock, fake price, fake lead time, fake certificates, or fake fitment claims

The site should sell the sourcing workflow, not pretend to own an exhaustive parts catalogue.

## Strategic Direction

The next phase should formalize the logic already visible on the live site. Do not redesign the business model from scratch.

For the current page-by-page visual rebuild approach, use `docs/page-rebuild-design-logic-2026-05-08.md`. That document defines how to turn text-heavy pages into image-rich, interactive, RFQ-oriented pages while preserving the strategic rules in this context file.

The main task is to make the RFQ-first architecture clearer, more indexable, and more conversion-oriented by standardizing:

- public paths
- page intent
- internal linking
- RFQ context inheritance
- OE / VIN / fitment risk language
- schema usage
- content clusters

The goal is not to create more pages for their own sake. The goal is to make each page answer one clear buyer intent and move the user toward a qualified RFQ.

## Public Information Architecture

Use four primary public paths as the target architecture:

```text
/brands/
/systems/
/products/
/rfq/
```

Current live pages may still exist under paths such as `/product/brand/` or `/product/part/`. When working on new architecture, research files, content collections, internal links, or routing plans, organize the logic around the four target paths above.

If public URLs are migrated later, keep the canonical path, sitemap, internal links, and canonical tags consistent.

## Page Intent

Each page type must carry one primary job.

| Page type | Primary intent | Must do | Must not do |
|---|---|---|---|
| Brand page | Platform-led RFQ entry | Explain common systems, required inputs, mismatch risks, related system links, and RFQ CTA | Publish broad unverified exact-fitment lists |
| System page | Category-led RFQ entry | Explain common parts, match-critical fields, what to send, related brands, and RFQ CTA | Claim broad compatibility across all models |
| Product family page | Part-family long-tail leaf page | Explain core variables, naming confusion, required specs, related systems/brands, FAQ, and RFQ CTA | Become an SKU database with fake stock, price, or lead time |
| RFQ page | Structured submission | Collect OE/part number, VIN/model, specs, photos/files, quantity, destination, packaging notes, and source context | Use only a weak name/email/message form |

## Brand Priority

Use this priority matrix unless later RFQ data proves a better order.

| Priority | Brands | Role | Rule |
|---|---|---|---|
| P0 | Sinotruk, HOWO, Shacman, Foton, Dongfeng, FAW, JAC | Core brand RFQ entries | Build first and deepest |
| P1 | JMC, DFSK, Wuling | Secondary brand entries | Keep as coverage signals until RFQ depth supports expansion |
| P2 | MAN, Volvo Truck, Mercedes-Benz Truck | Controlled aftermarket inquiry entries | Do not imply official authorization or dealer replacement |

Treat `Sinotruk` as an OEM umbrella page. Treat `HOWO` as a platform or family page under that umbrella logic. Do not let `Sinotruk parts` and `HOWO parts` compete as careless flat duplicates.

## System Architecture

Use a two-level system model.

Public navigation may show five major hubs:

- Brake
- Engine
- Transmission
- Chassis
- Electrical

The content layer may keep more specific leaf systems when they match buyer RFQ behavior, including:

- Air system
- Suspension
- Steering
- Axle and wheel-end
- Cooling
- Rubber and bushing

Large systems should work as hubs. Specific systems should work as RFQ-oriented leaves.

## Product Page Depth

Product pages should be product-family leaf pages, not SKU detail pages.

For example, `/products/brake-chamber/` should explain:

- common names
- system context
- common mismatch risks
- required buyer inputs
- dimensions or specs that affect matching
- related systems and brands
- RFQ CTA

It should not claim live inventory, prices, lead times, or exact application coverage unless those claims are verified and visible.

## RFQ Input Standard

RFQ flows should standardize and preserve source context from the page where the buyer entered.

Minimum useful RFQ inputs:

- OE number or part number, if available
- VIN or vehicle model
- model year, market, or configuration when relevant
- photos or file upload
- specs or dimensions where needed
- quantity
- destination country or port
- packaging or labeling notes
- old supplier reference, if available
- source page or inquiry context

Brand, system, product, and blog pages should pass context into the RFQ path where practical so the buyer does not need to repeat what they were viewing.

## OE, Part Number, Cross Reference, and Fitment Policy

OE numbers, part numbers, vehicle models, brand names, and cross references may be used on CertiSpares, but only as inquiry identification and matching inputs.

They must not be written as automatic fitment conclusions.

Do:

- say OE/part numbers help identify the inquiry
- say final matching depends on OE/VIN/model/spec confirmation
- ask users to provide photos, dimensions, connector type, voltage, load spec, bushing size, or other match-critical details where relevant
- describe CertiSpares as independent sourcing and RFQ support unless explicit authorization exists

Do not:

- claim exact fitment without confirmation
- imply official OEM authorization
- position CertiSpares as a replacement for official dealer or service networks
- publish unverified compatibility tables
- write phrases like "fits all", "guaranteed compatible", or "official replacement" unless legally and technically verified

Reusable site disclaimer:

> Brand names, OE numbers, vehicle models, and cross references on this site are used for inquiry identification and matching discussion only. Final fitment and quotation scope must be confirmed by OE reference, VIN, model/year/market data, dimensions, connector type, and other applicable technical specifications. CertiSpares is an independent sourcing and RFQ support service unless explicit authorization is stated.

## Structured Data Policy

Structured data must describe visible on-page content and must not mislead search engines or users.

Rules:

- Do not use Product markup on brand hubs.
- Do not use Product markup on system hubs.
- Product-family leaf pages may use product-related schema only when visible page data is specific, accurate, and non-misleading.
- Do not include fake offers, prices, availability, ratings, or inventory.
- Prefer BreadcrumbList, FAQPage, Organization, and WebPage where appropriate.
- Enriched search should be considered mainly for leaf pages, not listing or hub pages.

## Blog and Internal Linking

The blog is not an independent media product. It is an explanation layer for landing pages, sourcing methodology pages, and RFQ conversion.

Content roles:

- Product Insight articles should support system pages and product-family pages.
- Sourcing Knowledge and China Supply Chain articles should support Sourcing, Capabilities, How It Works, and RFQ pages.
- Brand or platform guides should support a specific brand page only when there is real RFQ depth.

Internal linking rules:

- Product education articles should link to at least one system page, one product-family page when available, and one RFQ CTA.
- Sourcing methodology articles should link to Sourcing, Capabilities, How It Works, and RFQ.
- Brand articles should link to the relevant brand page and related system pages.
- Anchor text should be meaningful and specific.
- Important pages should be reachable through normal crawlable `<a href>` links.

If an article cannot naturally send users to a brand page, system page, product-family page, or RFQ form, it is probably not a priority article for CertiSpares.

## Execution Documents To Create

The deep research should be converted into execution documents under an appropriate research or docs folder. These are not the only possible documents, but they are the first required set:

| File | Purpose |
|---|---|
| `certispares-positioning.md` | Define what the site is and is not |
| `certispares-site-map.md` | Define page hierarchy and path relationships |
| `brand-page-strategy.md` | Define brand priority, page roles, inputs, and risk copy |
| `system-page-strategy.md` | Define system hubs, leaf systems, match-critical fields, and CTAs |
| `product-entry-page-strategy.md` | Define product-family leaf page depth and SKU boundaries |
| `rfq-flow-strategy.md` | Define RFQ fields, prefill behavior, attachments, and CTA routing |
| `oe-number-policy.md` | Define OE, part number, and cross-reference language |
| `fitment-disclaimer-policy.md` | Define fitment disclaimers and exact-fit limits by page type |
| `certispares-blog-clusters.md` | Define topic clusters, link targets, and article priorities |
| `certispares-internal-linking-plan.md` | Define home-hub-leaf-RFQ and blog-to-landing-page linking |
| `docs/page-rebuild-design-logic-2026-05-08.md` | Define the current page-by-page visual rebuild method for reducing text density, adding images, interaction, and clearer RFQ paths |

## Acceptance Criteria

Any CertiSpares SEO, content, routing, or page-template task should be checked against these questions:

1. Can a user understand within 10 seconds that CertiSpares is an inquiry-based sourcing site, not a catalogue?
2. Do brand, system, product, and RFQ pages each have a single clear user intent?
3. Does OE/fitment language stay in the safe zone of matching input plus confirmation, instead of becoming a promise?
4. Does the page naturally move users toward a qualified RFQ?
5. Does the content avoid fake stock, fake price, fake lead time, fake certificates, fake authorization, and fake fitment?
6. Are internal links crawlable, meaningful, and aligned with the page's role?
7. Is schema limited to accurate, visible, non-misleading page content?

When in doubt, keep the site RFQ-first, independent, specific, and conservative about fitment.
