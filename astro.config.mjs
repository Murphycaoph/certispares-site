// @ts-check
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  site: "https://certispares.com",
  trailingSlash: "always",
  integrations: [
    sitemap({
      filter: (page) =>
        page !== "https://certispares.com/thank-you/" &&
        !page.startsWith("https://certispares.com/blog/tag/"),
    }),
  ],
  build: {
    inlineStylesheets: "always",
  },
});
