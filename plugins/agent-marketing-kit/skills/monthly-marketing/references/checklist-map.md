# Checklist map and dashboard writes

## Default checklist items and the step that makes them

Agents rename, resize, add and remove items, so match by title and channel.
These are the Command Center's defaults.

| Key | Default title | Channel | Step |
|---|---|---|---|
| `market-blog` | Market update blog post | Blog | 1 |
| `community-blog` | Community or lifestyle blog post | Blog | 2 |
| `newsletter` | Monthly email newsletter | Email | 3 |
| `single-topic-email` | Single-topic email (from the lifestyle blog) | Email | 4 |
| `postcard` | Market report postcard | Direct mail | 5 |
| `market-video` | Market update video | Video | 6 |
| `tour-video` | Community or lifestyle video (pairs with the blog) | Video | 6 (from the Step 2 script) |
| `reel-market` | Reel cut from the market update video | Social media | 6 |
| `reel-community` | Reel cut from the community video | Social media | 6 |
| `broll` | B-roll videos | Social media | 6 |
| `feed-posts-15` | Feed posts | Social media | 6 |
| `feed-posts` | Carousel posts | Social media | 6 |
| `market-graphic` | Market stats graphic | Social media | 6 |
| `gbp-posts` | Google Business Profile posts | Google Business Profile | 6 |
| `gbp-reviews` | Reply to new Google reviews | Google Business Profile | not made: ongoing, the agent's |
| `review-ask` | Ask recent clients for reviews | Google Business Profile | 7 (offer a review-request message) |

Anything else (a listings email, an open house, an item they added) is the
agent's own: list it in the plan as theirs and don't change it. An item
whose title clearly matches a step (e.g. "Blog post: fall trail guide" is a
lifestyle blog) goes with that step; ask if it's unclear.

## Reading the dashboard

Use the artifact data tool with the dashboard's URL.

- Month checklist: collection `months/YYYY-MM/items`, one document per item
  (`key, title, channel, qty, dueDay, status, done, link, thread`).
- Year theme: collection `calendar`, doc `YYYY-MM`.
- Recurring plan (for setting up a month): collection `config`, doc `plan`.
- Statuses: `todo` Not started, `doing` Drafting, `review` Ready for review,
  `changes` Needs changes, `approved` Approved, `scheduled` Scheduled,
  `done` Published.
- `qty` above 1 is a counted item. `status` tracks the drafts; `done`
  counts how many are live. Never set `done`.

A step is finished when its item is at `review` or beyond. When resuming,
start with the first step whose items are still `todo`, `doing` or
`changes`.

## Marking an item Ready for review

Read the item, then write one pinned update:

```json
{"op": "update", "collection": "months/2026-11/items", "doc_id": "newsletter",
 "data": {
   "status": "review",
   "link": "<artifact URL or live page, if the piece has one>",
   "thread": [<existing thread entries…>,
     {"at": "<ISO time>", "by": "claude", "kind": "note",
      "text": "Draft ready. Saved in your Claude Project as claude/newsletters/Claire_Morgan_Newsletter_November2026.html"}]
 },
 "if_version": 4}
```

- Keep every existing `thread` entry and add the new note at the end.
- Set `link` only to something that opens in a browser: a published
  artifact, a live blog post, or `<dashboard URL>#social` for social items.
  Files saved in the Project go in the note instead.
- Skip items at `approved`, `scheduled` or `done`, and items at `changes`
  unless this is the revision they asked for.
- If the write fails because the item changed, read it again and redo that
  one write.

## Setting up a month that has no items yet

Prefer asking the agent to tap "Set up <Month>" on the dashboard. If they
ask you to do it, create one document per item in `config/plan`'s `items`
(`months/YYYY-MM/items/<key>`) with `{key, title, channel, qty, dueDay,
status: "todo", done: 0, link: ""}` in one batch.
