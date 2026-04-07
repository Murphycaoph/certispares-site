// @ts-check
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

// https://astro.build/config
export default defineConfig({
  site: "https://certispares.com", // ✅ 改成你的真实域名
  integrations: [
    sitemap({
      filter: (page) => page !== "https://certispares.com/thank-you/",
    }),
  ],
  build: {
    inlineStylesheets: "always",
  },
});
