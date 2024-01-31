import { defineConfig } from "astro/config";

import preact from "@astrojs/preact";

// https://astro.build/config
export default defineConfig({
  include: ["src/components/**/*.astro.jsx"],
  integrations: [preact()]
});