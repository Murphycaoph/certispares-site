# Product Entry Page Strategy

Purpose: define how product-family pages should work without becoming risky SKU catalogue pages.

## Product Page Role

Product pages are product-family leaf pages.

They answer this buyer question:

"I know the type of part I need. What details should I provide so CertiSpares can discuss matching, sourcing, and quotation?"

Product pages should support long-tail search intent while staying conservative about exact fitment.

## Product Page Boundary

Product pages may explain:

- common names
- related systems
- common vehicle or application context
- key variables
- dimensions and specs that affect matching
- naming confusion
- buyer input checklist
- related brands and systems
- RFQ next step

Product pages must not become:

- SKU databases
- inventory pages
- price pages
- lead-time promise pages
- official fitment pages
- copied catalogue pages

## Product-Family Template

Recommended sections:

1. Product-family overview
2. Where this part is used
3. Key variables and matching inputs
4. Common naming or cross-reference confusion
5. What to send for RFQ
6. Related systems
7. Related brands
8. FAQ
9. RFQ CTA
10. Fitment disclaimer

## Required Frontmatter Fields

Use these fields as the default model when building a content collection:

```yaml
title:
slug:
description:
pageType: product-family
primarySystem:
relatedSystems:
relatedBrands:
commonNames:
requiredInputs:
matchCriticalFields:
commonMismatchRisks:
rfqContext:
seo:
  title:
  description:
schema:
  type: WebPage
```

Add product-related schema only if the visible page content is specific, accurate, and non-misleading.

## Required Inputs

Product-family pages should ask for:

- OE number or part number, if available
- vehicle model or VIN
- dimensions where relevant
- photos
- quantity
- destination
- old supplier reference, if available
- packaging or labeling notes
- system-specific details such as voltage, connector type, bushing size, spline details, or load spec

## Product Schema Rule

Default to WebPage, BreadcrumbList, and FAQPage where appropriate.

Do not add Product schema if the page lacks:

- one clearly defined product family
- visible and accurate product-family information
- non-misleading descriptions

Never add fake:

- price
- stock availability
- aggregate rating
- offer
- brand authorization
- exact fitment

## Copy Rules

Use:

- "commonly requested for"
- "often checked by"
- "send details for matching"
- "subject to OE/VIN/model/spec confirmation"

Avoid:

- "fits all"
- "guaranteed replacement"
- "direct official replacement"
- "in stock"
- "best price"
- "for all models"

## Acceptance Criteria

A product-family page is ready if:

- it targets one part-family intent
- it explains match-critical variables
- it asks for enough RFQ inputs
- it links to parent system, related brands, and RFQ
- it avoids SKU, stock, price, lead time, and exact-fitment overclaims
