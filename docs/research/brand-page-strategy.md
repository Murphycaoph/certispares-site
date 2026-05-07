# Brand Page Strategy

Purpose: define how CertiSpares should create, prioritize, and write brand pages.

## Brand Page Role

Brand pages are platform-led RFQ entries.

They answer this buyer question:

"I know the vehicle brand or platform. What information should I send so CertiSpares can discuss matching and sourcing?"

Brand pages should not be catalogues or exact model compatibility databases.

## Brand Priority Matrix

| Priority | Brands | Page role | Execution depth |
|---|---|---|---|
| P0 | Sinotruk, HOWO, Shacman, Foton, Dongfeng, FAW, JAC | Core brand RFQ pages | Build first and deepest |
| P1 | JMC, DFSK, Wuling | Secondary coverage pages | Keep lighter until RFQ volume supports expansion |
| P2 | MAN, Volvo Truck, Mercedes-Benz Truck | Controlled aftermarket inquiry pages | Use strict independent support language |

## Slug Recommendations

| Brand | Suggested slug | Notes |
|---|---|---|
| Sinotruk | `sinotruk` | OEM umbrella page |
| HOWO | `howo` | Platform/family page under Sinotruk logic |
| Shacman | `shacman` | Core China heavy-duty brand |
| Foton | `foton` | Commercial vehicle brand |
| Dongfeng | `dongfeng` | Commercial vehicle brand |
| FAW | `faw` | Commercial vehicle brand |
| JAC | `jac` | Commercial vehicle brand with market variation caution |
| JMC | `jmc` | Secondary coverage |
| DFSK | `dfsk` | Secondary coverage |
| Wuling | `wuling` | Secondary coverage |
| MAN | `man` | Controlled aftermarket support |
| Volvo Truck | `volvo-truck` | Controlled aftermarket support |
| Mercedes-Benz Truck | `mercedes-benz-truck` | Controlled aftermarket support |

## Sinotruk and HOWO Rule

Treat Sinotruk as the OEM umbrella.

Treat HOWO as a platform or product-family page within that umbrella logic.

Do not create flat duplicate pages where `Sinotruk parts` and `HOWO parts` compete with nearly identical content.

Sinotruk page should cover:

- umbrella brand context
- common truck platforms or families
- systems handled
- RFQ input requirements
- link to HOWO and future platform pages

HOWO page should cover:

- HOWO-specific buyer intent
- common systems and part groups
- required matching inputs
- related system/product-family pages
- RFQ CTA

## Brand Page Content Template

Recommended sections:

1. Brand/platform sourcing overview
2. Common systems handled
3. What to send before quotation
4. Common mismatch risks
5. Related systems
6. Related product families
7. RFQ CTA
8. Fitment and authorization disclaimer

## Required Inputs

Brand pages should ask for:

- OE number or part number, if available
- VIN or vehicle model
- model year and market, if relevant
- part photos
- old supplier reference, if available
- quantity
- destination country or port
- packaging or labeling notes
- part list for mixed-SKU inquiries

## P2 Brand Rules

For MAN, Volvo Truck, and Mercedes-Benz Truck:

- describe pages as independent aftermarket inquiry support
- do not imply CertiSpares replaces official dealer/service channels
- do not claim official genuine parts access
- do not claim VIN catalogue lookup capability unless technically and legally true
- require buyer-provided OE/VIN/model/spec confirmation

## Structured Data

Brand pages should not use Product markup.

Allowed schema types may include:

- WebPage
- BreadcrumbList
- FAQPage, if visible FAQs exist
- Organization references where appropriate

## Acceptance Criteria

A brand page is ready if:

- it has one platform-led RFQ intent
- it asks for match-critical inputs
- it links to relevant systems and RFQ
- it avoids exact fitment overclaims
- it does not imply official authorization
