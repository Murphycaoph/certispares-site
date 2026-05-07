# System Page Strategy

Purpose: define the system page model for category-led RFQ entry.

## System Page Role

System pages are category-led RFQ entries.

They answer this buyer question:

"I know the part system, but I need help identifying what details matter before sourcing."

System pages should explain common part groups, matching drivers, required inputs, and RFQ routing.

## Two-Level System Model

Use major systems as hubs and specific systems as leaf pages.

Major hubs:

- Brake
- Engine
- Transmission
- Chassis
- Electrical

Possible leaf systems:

- Air system
- Suspension
- Steering
- Axle and wheel-end
- Cooling
- Rubber and bushing

The exact list can expand based on RFQ data and existing content depth.

## Hub Page Role

System hub pages should:

- summarize the major system
- list common sub-systems and part families
- explain what buyers should prepare
- link to leaf system pages
- link to high-priority brand pages
- link to RFQ

System hubs should not:

- pretend every part in the system has known exact fitment
- list broad unverified compatibility tables
- use Product markup

## Leaf Page Role

System leaf pages should:

- target a specific RFQ category
- explain match-critical fields
- list common part families
- link to product-family pages
- link to related brand pages
- route to RFQ with system context

## Match-Critical Fields By System

| System | Important inputs |
|---|---|
| Brake | vehicle model/VIN, OE reference, drum/disc dimensions, brake type, photos |
| Air system | valve type, connector type, port size, pressure rating, OE reference, photos |
| Engine | engine model, OE reference, displacement or configuration where relevant, photos |
| Transmission | gearbox model, clutch size, spline details, OE reference, photos |
| Suspension | bushing size, pin size, torque rod length, load spec, vehicle model/VIN |
| Steering | steering gear/pump reference, mounting details, connector/line details, photos |
| Axle and wheel-end | axle model, bearing dimensions, hub details, bolt pattern, photos |
| Cooling | radiator/intercooler dimensions, inlet/outlet position, core size, photos |
| Rubber and bushing | inner/outer diameter, length, hardness if known, application context, photos |
| Electrical | voltage, connector type, plug pins, OE reference, mounting position, photos |

## System Page Template

Recommended sections:

1. System sourcing overview
2. Common part groups
3. Match-critical fields
4. What to send
5. Common mismatch risks
6. Related product-family pages
7. Related brand pages
8. RFQ CTA
9. Fitment disclaimer

## CTA Rules

System CTAs should pass source context:

- system slug
- page title
- relevant product group if selected
- suggested required fields

CTA copy should focus on sending details for matching, not buying from a catalogue.

## Structured Data

System hubs and system leaf pages should generally use:

- WebPage
- BreadcrumbList
- FAQPage if visible FAQs exist

Do not use Product markup on system hubs.

## Acceptance Criteria

A system page is ready if:

- it clearly answers category-led RFQ intent
- it lists match-critical fields
- it avoids broad compatibility claims
- it links to product-family pages and RFQ
- it uses safe fitment language
