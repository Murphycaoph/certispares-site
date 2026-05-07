# CertiSpares Internal Linking Plan

Purpose: define internal linking rules that connect education, landing pages, and RFQ conversion.

## Linking Principle

Every important page should know where it sends the user next.

The internal linking system should help both users and search engines understand:

- brand entry paths
- system entry paths
- product-family leaf pages
- RFQ submission path
- sourcing and capability explanations

Use normal crawlable `<a href>` links for important navigation and contextual links.

## Primary Link Flow

```text
Home -> Brands -> Brand page -> System/Product -> RFQ
Home -> Systems -> System page -> Product/Brand -> RFQ
Home -> Products -> Product-family page -> RFQ
Insights -> Brand/System/Product/Sourcing -> RFQ
Sourcing/Capabilities/How It Works -> RFQ
```

## Home Page Links

Home should link to:

- `/brands/`
- `/systems/`
- `/products/`
- `/rfq/`
- `/sourcing/`
- `/capabilities/`
- selected P0 brand pages
- selected high-value system pages

Do not make home depend only on generic CTA buttons. Use descriptive text links where they help clarify site structure.

## Brand Page Links

Each brand page should link to:

- `/rfq/` with brand context
- related system pages
- relevant product-family pages
- parent or related brand pages where logical

Example anchor patterns:

- "send a HOWO brake parts RFQ"
- "brake system sourcing requirements"
- "engine part matching inputs"
- "submit Sinotruk parts details"

## System Page Links

Each system page should link to:

- `/rfq/` with system context
- relevant product-family pages
- relevant brand pages
- supporting Product Insight articles

Example anchor patterns:

- "brake chamber RFQ details"
- "air brake system matching fields"
- "related HOWO brake parts sourcing"

## Product-Family Page Links

Each product-family page should link to:

- parent system page
- related system pages
- relevant brand pages
- RFQ
- supporting articles

Product-family pages should be close to RFQ conversion.

## Blog Linking Rules

Product Insight posts:

- link to one system page
- link to one product-family page if available
- link to RFQ or a contextual CTA

Sourcing Knowledge posts:

- link to Sourcing
- link to Capabilities or How It Works
- link to RFQ

China Supply Chain posts:

- link to Sourcing or Capabilities
- link to relevant system pages when naturally connected

Brand guides:

- link to the matching brand page
- link to related system pages
- link to RFQ

## Anchor Text Rules

Anchor text should be specific and meaningful.

Good:

- "HOWO parts RFQ requirements"
- "brake system sourcing inputs"
- "commercial vehicle suspension matching fields"
- "submit a structured parts inquiry"

Weak:

- "click here"
- "learn more"
- "products"
- "read this"

## Orphan Page Check

No important brand, system, product-family, or RFQ page should be orphaned.

Each important page should have:

- at least one hub link
- at least one contextual link from related content
- a clear path to RFQ

## Acceptance Criteria

Internal linking is healthy if:

- important pages are crawlable through normal links
- anchors describe the destination
- blog posts move users into landing pages
- landing pages move users into RFQ
- brand/system/product pages reinforce each other without duplicate intent
