
// 1. Import utilities from `astro:content`
import { z } from "astro/zod";
import { defineCollection } from "astro/content/runtime";

// 2. Define a `type` and `schema` for each collection
const blogCollection = defineCollection({
    type: 'content', // v2.5.0 and later
    schema: z.object({
        title: z.string(),
        tags: z.array(z.string()),
        pubDate: z.string().transform((date) => new Date(date).toISOString()),
        layout: z.string(),
        description: z.string(),
        author: z.string(),
        image: z.object({ alt: z.string(), url: z.string() }).optional(),
    }),
});

const meetingCollections = defineCollection({
    type: 'content',
    schema: z.object({
        week: z.string(),
        tags: z.array(z.string()),
        author: z.string(),
        pubDate: z.string(),
        layout: z.string(),
        description: z.string(),
})
});

// 3. Export a single `collections` object to register your collection(s)
export const collections = {
  'posts': blogCollection,
    'meetings': meetingCollections,
};