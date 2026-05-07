export type ImageDimensions = {
  width: number;
  height: number;
};

const IMAGE_DIMENSIONS: Record<string, ImageDimensions> = {
  "/images/hero.webp": { width: 1600, height: 900 },
  "/images/hero-02-commercial-fleet.webp": { width: 1600, height: 900 },
  "/images/hero-03-container-port.webp": { width: 1600, height: 900 },
  "/images/hero-04-logistics-truck.webp": { width: 1306, height: 803 },
  "/images/logo.webp": { width: 200, height: 200 },
  "/images/hebei-industrial-park-aerial.webp": { width: 3071, height: 1943 },
  "/images/china-industrial-warehouse.webp": { width: 1909, height: 1272 },
  "/images/container-loading-supervision.webp": { width: 1600, height: 1071 },
  "/images/logistics-container-export-port.webp": { width: 2000, height: 1124 },
  "/images/factory-quality-inspection-metal-parts.webp": { width: 2560, height: 1707 },
  "/images/shipping-documents-export-paperwork.webp": { width: 2560, height: 1670 },
  "/images/Brake-System.webp": { width: 2048, height: 2048 },
  "/images/Suspension.webp": { width: 2730, height: 1535 },
  "/images/Engine-Parts.webp": { width: 2730, height: 1535 },
  "/images/homepage/homepage-hero-truck.webp": { width: 2400, height: 900 },
  "/images/homepage/homepage-supplier-fit.webp": { width: 1200, height: 760 },
  "/images/homepage/homepage-part-confirmation.webp": { width: 1200, height: 760 },
  "/images/homepage/homepage-qc-packing.webp": { width: 1200, height: 760 },
  "/images/homepage/homepage-shipment-planning.webp": { width: 1200, height: 760 },
  "/images/homepage/homepage-landed-cost.webp": { width: 1200, height: 760 },
  "/images/homepage/homepage-turnover.webp": { width: 1200, height: 760 },
  "/images/homepage/homepage-cta-port.webp": { width: 1400, height: 760 },
};

export const getImageDimensions = (src: string): ImageDimensions => {
  const dimensions = IMAGE_DIMENSIONS[src];

  if (!dimensions) {
    throw new Error(`Missing image dimensions for: ${src}`);
  }

  return dimensions;
};
