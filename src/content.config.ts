import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: () => z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.date(),
    updatedDate: z.date().optional(),
    tags: z.array(z.string()).default([]),
    author: z.string().default('Merel Aerts'),
  }),
});

const aanbieders = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/aanbieders' }),
  schema: () => z.object({
    name: z.string(),
    website: z.string().url(),
    category: z.string(),
    summary: z.string(),
    order: z.number().default(99),
  }),
});

export const collections = { blog, aanbieders };
