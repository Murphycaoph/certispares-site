# CertiSpares Site Map

Purpose: define the target public information architecture and page relationships for CertiSpares.

## Target Public Paths

Use these four primary paths as the architecture target:

```text
/brands/
/systems/
/products/
/rfq/
```

Supporting pages remain important:

```text
/
/sourcing/
/capabilities/
/how-it-works/
/insights/
/about/
/contact/
```

If the live site keeps existing paths such as `/product/brand/` or `/product/part/`, treat them as current implementation paths. The strategic content model should still be organized around `/brands/`, `/systems/`, `/products/`, and `/rfq/`.

## Page Hierarchy

```text
Home
├─ Brands
│  ├─ Brand pages
│  └─ Related system links
├─ Systems
│  ├─ System hub pages
│  └─ System leaf pages
├─ Products
│  └─ Product-family leaf pages
├─ RFQ
├─ Sourcing
├─ Capabilities
├─ How It Works
├─ Insights
└─ About / Contact
```

## Conversion Flow

Every major path should end in a qualified RFQ.

```text
Home -> Brand/System/Product -> RFQ
Blog -> Brand/System/Product -> RFQ
Sourcing/Capabilities/How It Works -> RFQ
```

## URL Roles

| URL type | Role |
|---|---|
| `/brands/` | Brand/platform entry hub |
| `/brands/{brand}/` | Brand-led RFQ entry |
| `/systems/` | Major system hub |
| `/systems/{system}/` | Category-led RFQ entry |
| `/products/` | Product-family index |
| `/products/{product-family}/` | Long-tail product-family RFQ leaf |
| `/rfq/` | Structured inquiry submission |
| `/insights/{article}/` | Education and internal-link support |

## Canonical Rules

When equivalent pages exist under older paths:

- choose one canonical public path
- keep internal links pointed to the canonical path
- keep sitemap entries canonical
- use canonical tags consistently
- redirect old paths when migration is ready

Do not split the same search intent across multiple equivalent pages.

## Navigation Rules

Primary navigation should avoid making `Product` look like a full catalogue.

Better labels:

- Brands
- Systems
- Products
- RFQ
- Sourcing
- Capabilities
- Insights

If `Product` is kept, clarify that it means entry paths or product families, not an exhaustive catalogue.

## Internal Linking Model

Home should link to:

- Brands hub
- Systems hub
- RFQ
- Sourcing
- Capabilities
- selected high-priority pages

Brand pages should link to:

- relevant system pages
- relevant product-family pages where available
- RFQ

System pages should link to:

- relevant brand pages
- product-family pages
- RFQ

Product-family pages should link to:

- parent system
- related brands
- RFQ

Blog posts should link to:

- one relevant landing page
- one deeper leaf page if available
- RFQ or a sourcing method page

## Acceptance Criteria

The site map is working if:

- brand, system, product, and RFQ paths are clearly distinct
- no page type tries to answer every intent
- important pages are reachable through crawlable links
- canonical paths are consistent
- internal links naturally move visitors toward RFQ
