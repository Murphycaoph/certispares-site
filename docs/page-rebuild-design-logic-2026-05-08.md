# CertiSpares Page Rebuild Design Logic - 2026-05-08

This document records the current page-by-page rebuild logic for CertiSpares. It should be used together with `AGENTS.md` before redesigning or implementing any non-homepage public page.

## Core Goal

The current rebuild is not a content expansion project. It is a readability and conversion project.

The main problem we are solving is that many pages feel like dense explanatory documents. From a buyer's perspective, too much text creates scanning fatigue, hides the useful entry point, and makes the site feel static.

The target experience should be:

- interactive enough to feel alive
- readable enough for a buyer to find the next step quickly
- image-rich enough to make the category or RFQ scenario concrete
- structured enough to keep the RFQ path clear
- conservative enough to avoid fake inventory, fake fitment, fake authorization, or fake price claims

## Working Method

Each page should follow the same rebuild sequence.

1. Use the GPT reference design as the visual direction, not as a final copy source.
2. Compare the reference design with the current live/local page.
3. Identify where the current page is too text-heavy, visually flat, repetitive, or unclear.
4. Keep the strategic RFQ-first logic from `AGENTS.md`.
5. Rebuild the page around visible decision paths, image blocks, short cards, workflow strips, and strong CTAs.
6. Verify desktop and mobile layouts after implementation.

Do not start by writing more content. Start by deciding what the buyer needs to see first, what they should compare, and what action they should take.

## Page Design Principles

### 1. One Page, One Buyer Question

Each page should answer one dominant question.

| Page | Primary buyer question |
|---|---|
| How It Works | What happens after I send an RFQ? |
| Cases | Does CertiSpares understand messy or incomplete RFQs like mine? |
| Product / Parts RFQ | Should I start from a brand, a system, or a mixed parts list? |
| Sourcing | How does CertiSpares compare suppliers and control sourcing risk? |
| Capabilities | What operational capabilities support my order after matching? |
| Insights | What practical knowledge helps me submit a better RFQ? |
| About | Why is this sourcing team credible and focused? |
| Contact | What is the fastest way to start a useful inquiry? |

If a section does not support the page's main question, it should be shortened, moved, or removed.

### 2. Replace Text Walls With Decision Blocks

Long paragraphs should become visual modules:

- path cards
- numbered workflows
- comparison strips
- "what to send" cards
- risk / clarification cards
- before-and-after RFQ states
- compact CTA panels

The buyer should be able to scan headings, card titles, icons, and images before reading body copy.

### 3. Use Images as Meaning, Not Decoration

Images should explain the buying situation or product context:

- trucks and platforms for brand-led RFQs
- parts groups for system-led RFQs
- spreadsheets, labels, photos, cartons, and warehouse scenes for messy RFQs
- container loading, QC, documents, and consolidation for sourcing and capabilities pages

Avoid generic dark atmosphere images when the buyer needs a concrete signal. Images should show the actual thing, process, or decision scenario whenever possible.

### 4. Use Color Blocks to Create Reading Rhythm

Pages should not be only white cards on white background. Use alternating visual weight:

- dark navy hero / CTA bands
- white decision-card sections
- pale blue RFQ helper panels
- image-led cards
- thin bordered process strips
- small accent badges for stages and outputs

Color should guide attention, not create a one-note blue page.

### 5. Add Motion, But Keep It Operational

Animation should make the page feel active without becoming a gimmick.

Good uses:

- hero path cards floating subtly
- workflow dots or lines activating on scroll
- cards lifting on hover
- image cards zooming gently on hover
- RFQ route steps highlighting in sequence
- small CTA arrows moving on hover

Avoid animation that slows reading, causes layout shift, or makes the page feel like a consumer landing page.

### 6. Keep RFQ Path Visible Throughout

Every major page should include at least one clear RFQ route:

- top hero CTA
- mid-page path choice or use-case entry
- bottom CTA band

The CTA language should match buyer context. For example:

- "Send RFQ"
- "Send Similar RFQ"
- "Start Brand RFQ"
- "Send Mixed SKU RFQ"
- "Contact on WhatsApp"

Avoid vague CTAs if a more specific RFQ action is available.

## Patterns Confirmed So Far

### How It Works

The page was rebuilt around the idea of an RFQ control path.

Confirmed logic:

- Use a cinematic logistics hero with a visible process panel.
- Convert the service explanation into a 5-step workflow.
- Add a "what helps us quote faster" section so buyers know what to prepare.
- Add incomplete-RFQ cases to reduce buyer hesitation.
- Use different buyer starting points instead of a single generic explanation.
- End with a dark CTA band that summarizes RFQ intake, matching, supplier comparison, quotation, and shipment follow-up.

Design intent:

The page should feel like a controlled process, not a service description.

### Cases

The page was rebuilt around anonymous RFQ examples.

Confirmed logic:

- Use case cards with real-world RFQ entry points.
- Make examples visual first: product group, spreadsheet, container, fleet, or photo reference.
- Show what CertiSpares clarifies before comparing suppliers.
- Let buyers choose the case closest to their own RFQ.
- Keep each case short, with tags that explain the matching challenge.
- Use a bottom CTA that invites buyers to send a similar incomplete RFQ.

Design intent:

The page should prove that messy, incomplete, or mixed inquiries can still become controlled sourcing scopes.

### Product / Parts RFQ

The page was rebuilt around entry routing.

Confirmed logic:

- Hero should immediately explain three paths: brand-led, system-led, and mixed-SKU RFQ.
- Entry path cards should use large images, not just icons.
- Brand area should use a 5-by-2 logo grid, with a right-side RFQ entry card.
- Existing low-quality brand logos should be replaced by generated, cleaner, consistent brand visuals.
- System cards should use concrete product thumbnails.
- "What to send before matching starts" should be short and practical.
- The page should not behave like a public SKU catalogue.

Design intent:

The page should help a buyer choose where to start, not overwhelm them with catalog-style text.

## Implementation Checklist

Before implementing a page:

- Confirm the page's one buyer question.
- Decide the hero image and the hero-side interactive panel.
- Identify 2 to 4 main visual sections.
- Convert paragraphs into cards, strips, paths, or short lists.
- Decide where images are required and whether to use existing assets, web images, or generated images.
- Define the RFQ CTA language for each major page section.

During implementation:

- Keep copy short and specific.
- Use existing global design tokens and components where possible.
- Use WebP assets for production images.
- Keep card radius restrained, usually 8px or less.
- Avoid nested cards.
- Make hover and scroll animations subtle.
- Keep mobile layouts readable without text overlap.

After implementation:

- Run the production build.
- Check desktop and mobile screenshots.
- Confirm the page has no broken image references.
- Confirm CTAs link to the correct RFQ/contact path.
- Confirm the page still follows RFQ-first and fitment-safety rules from `AGENTS.md`.

## Copy Rules

The page copy should be useful, not decorative.

Prefer:

- short section titles
- concrete buyer inputs
- visible outputs
- risk labels
- action-specific CTAs
- practical examples

Avoid:

- long generic service introductions
- repeating the same sourcing promise in every section
- unverified fitment claims
- public stock, price, or lead time claims
- broad "we can do everything" language

## Asset Rules

Use images to make the page easier to understand.

Image sources can include:

- current project assets
- generated images
- internet-sourced images when appropriate and legally safe
- optimized WebP conversions

For brand logos:

- use clean, high-quality generated logo visuals where current assets are weak
- keep a consistent card style and whitespace
- do not imply official authorization

For product/system images:

- prefer clear product groups on light or realistic industrial backgrounds
- avoid watermarks, blurred crops, and overly dark images
- keep product meaning recognizable at card size

## Success Standard

A rebuilt page is successful when a buyer can answer these questions within a few seconds:

1. What kind of RFQ situation is this page for?
2. Which path or example is closest to my inquiry?
3. What information should I send?
4. What will CertiSpares clarify or control before quoting?
5. Where do I click to send the inquiry?

If the buyer must read the full page to understand the page, the design is still too text-heavy.
