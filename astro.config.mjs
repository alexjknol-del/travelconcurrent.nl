import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://travelconcurrent.nl',
  integrations: [sitemap()],
  output: 'static',
  trailingSlash: 'never',
});
