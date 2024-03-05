import { defineConfig } from "astro/config";
import preact from "@astrojs/preact";

import vercel from "@astrojs/vercel/serverless";

// https://astro.build/config
export default defineConfig({
  include: ["src/components/**/*.astro.jsx"],
  integrations: [preact()],
  // output: "server",
  // adapter: vercel({
  //   webAnalytics: {
  //     enabled: true,
  //   },
  // }),
});
