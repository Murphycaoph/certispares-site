export const SITE_URL = "https://certispares.com";
export const ORGANIZATION_ID = `${SITE_URL}/#organization`;
export const WEBSITE_ID = `${SITE_URL}/#website`;
export const CONTACT_EMAIL = "murphy@certispares.com";
export const WHATSAPP_DISPLAY = "+86 156 3302 2618";
export const FACEBOOK_URL = "https://www.facebook.com/profile.php?id=61585722976089";

export const baseStructuredData = [
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": ORGANIZATION_ID,
    name: "CertiSpares",
    url: `${SITE_URL}/`,
    logo: `${SITE_URL}/images/logo.webp`,
    description:
      "RFQ-first commercial vehicle aftermarket parts sourcing support from China for importers, distributors, wholesalers, and fleet-related buyers.",
    email: CONTACT_EMAIL,
    contactPoint: [
      {
        "@type": "ContactPoint",
        contactType: "sales",
        email: CONTACT_EMAIL,
        telephone: WHATSAPP_DISPLAY,
        areaServed: "Worldwide",
        availableLanguage: ["en"],
      },
    ],
    sameAs: [FACEBOOK_URL],
  },
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": WEBSITE_ID,
    name: "CertiSpares",
    url: `${SITE_URL}/`,
    description: "Commercial vehicle parts sourcing support from China.",
    publisher: {
      "@id": ORGANIZATION_ID,
    },
  },
];

export const makeFaqPageSchema = (items: { q: string; a: string }[], id?: string) => ({
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "@id": id,
  mainEntity: items.map((item) => ({
    "@type": "Question",
    name: item.q,
    acceptedAnswer: {
      "@type": "Answer",
      text: item.a,
    },
  })),
});
