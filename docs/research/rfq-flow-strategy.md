# RFQ Flow Strategy

Purpose: define how RFQ entry, prefill, field structure, and CTA routing should work across CertiSpares.

## RFQ Role

The RFQ path is the main conversion path.

It should collect enough information for CertiSpares to begin technical matching, supplier comparison, quotation consolidation, QC planning, document handling, and shipment coordination.

The RFQ page should not be a weak contact form.

## Target Path

Preferred path:

```text
/rfq/
```

Current contact forms may remain, but future strategy should treat RFQ as the structured submission destination.

## Source Context

RFQ links should preserve where the buyer came from.

Useful context:

- source page type
- source slug
- source title
- selected brand
- selected system
- selected product family
- suggested required inputs

Example:

```text
/rfq/?brand=howo&system=brake&source=/brands/howo/
```

Implementation can use query parameters, hidden form fields, or client-side prefill, depending on the site architecture.

## Minimum RFQ Fields

Required or strongly recommended:

- buyer name
- company
- email
- country
- destination country or port
- part information type
- OE number or part number
- vehicle model or VIN
- quantity
- message or part list
- file upload or photo upload

Optional but useful:

- model year
- market or configuration
- dimensions/specs
- connector type
- voltage
- load spec
- bushing size
- old supplier reference
- packaging or labeling requirements
- target shipment method
- mixed-SKU list attachment

## Part Information Type

Allow buyers to classify what they can provide:

- OE/part number
- VIN or vehicle details
- photos only
- dimensions/specs
- sample or old supplier reference
- mixed parts list

This helps route the inquiry internally and sets matching expectations.

## Page-Specific Prefill

Brand page CTA should prefill:

- brand
- source page
- prompt for OE/VIN/model/photos/part list

System page CTA should prefill:

- system
- source page
- prompt for system-specific fields

Product-family page CTA should prefill:

- product family
- parent system
- source page
- product-specific required inputs

Blog CTA should prefill:

- article source
- related landing page if applicable

## RFQ Copy

Use copy that encourages structured detail:

- "Send part details for matching discussion"
- "Upload photos or a parts list"
- "Include OE number, VIN/model, dimensions, quantity, and destination where available"
- "Final quotation scope depends on technical confirmation"

Avoid:

- "Buy now"
- "Check live stock"
- "Guaranteed match"

## Attachments

The RFQ flow should support attachments because commercial vehicle parts matching often depends on visual and document evidence.

Supported attachment types should include:

- part photos
- Excel part lists
- PDF lists
- old invoices or supplier references
- dimension drawings
- packaging or label files

## Acceptance Criteria

The RFQ flow is ready if:

- it collects more than name/email/message
- it preserves source context
- it asks for match-critical data
- it supports attachments
- it avoids immediate fitment promises
- it supports mixed-SKU commercial inquiries
