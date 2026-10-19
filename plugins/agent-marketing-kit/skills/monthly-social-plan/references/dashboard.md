# Reading and updating the Marketing Command Center

The dashboard is a published artifact built by the Marketing Command Center
skill. Everything on it lives in that artifact's database. Read and write it
with the artifact data tool (its `get`, `list`, `query` and `batch` actions),
passing the dashboard's URL. Never edit the dashboard's HTML.

Find the dashboard by listing the agent's artifacts and matching the title
("Marketing Command Center", or the agent's team name plus "Command Center").
If more than one could be theirs, ask which. Never read or write a dashboard
that belongs to a different agent.

`YYYY-MM` below is the target month, e.g. `2026-11`.

## What to read

| What | Collection | Doc id | Fields used |
|---|---|---|---|
| Recurring plan | `config` | `plan` | `items`: array of `{key, title, channel, qty, dueDay}` |
| Names | `config` | `team` | `agent`, `assistant` (first names) |
| Month theme | `calendar` | `YYYY-MM` | `theme`, `market`, `community`, `email`, `hooks` |
| Month checklist | `months/YYYY-MM/items` | one per item, id = `key` | `key, title, channel, qty, dueDay, status, done, link` |
| Saved ideas | `ideas` | any | `title, type, month, hook, caption, shots, notes, link, used` |

- **Use the month checklist first.** It is what the agent will actually
  review, including one-off items they added for that month (these have
  random ids, and some carry `fromIdea` pointing at a saved idea). If the
  month has no items yet (they haven't tapped "Set up <Month>"), build from
  `config/plan` instead and tell the agent to set up the month on the
  dashboard so the items appear there; skip the dashboard update until they
  do.
- `channel` is one of `Email`, `Blog`, `Video`, `Social media`,
  `Google Business Profile`, `Direct mail`, `Other`.
- `qty` above 1 is a counted item (e.g. 15 feed posts). It has two
  separate things: `status` for the drafts (Ready for review, Approved…),
  and `done`, which counts how many are **live** (posted). `done` equal to
  `qty` shows as Published. Counted items go through the review queue like
  any other item. (Dashboards built before this change ignore `status` on
  counted items; check for `counted-review v1` in the page, and if it's
  missing, upgrade the dashboard with the Command Center skill's
  `scripts/upgrade_dashboard.py` first.)
- `dueDay` is the go-live day of the target month.
- **Ideas:** use ideas where `month` equals `YYYY-MM` and `used` is not
  true. Each is a reel or post the agent saved from elsewhere; adapt its
  hook and format to their own content, never copy its caption.
- The year-plan `hooks` (e.g. "Veterans Day, Thanksgiving") are
  suggestions for timely posts; keep them light and on-brand, and skip any
  the Brand Brain rules out (for example politics or religion).

## Statuses

| Value | Shows as |
|---|---|
| `todo` | Not started |
| `doing` | Drafting |
| `review` | Ready for review |
| `changes` | Needs changes |
| `approved` | Approved |
| `scheduled` | Scheduled |
| `done` | Published |

## What to write (Step 7)

Only items in `months/YYYY-MM/items` that this skill produced. Read each
one, then send ONE batch of `update` writes, each pinned with the version
you read:

```json
{"op": "update", "collection": "months/2026-11/items", "doc_id": "feed-posts-15",
 "data": {"status": "review", "link": "<dashboard URL>#social"},
 "if_version": 7}
```

- `link`: the dashboard's Social plan tab (`<dashboard URL>#social`) for every
  item you produced, design-only ones included (the tab links to the design
  canvas). The review queue groups every item whose link ends in `#social`
  into one "Social media plan" card per month, with Approve all and Request
  changes, so the agent reviews the plan once instead of item by item. Use the
  plan page URL only when the dashboard has no Social plan tab.
- Set `status` to `review` on every item you produced, counted items
  included.
- **Never set `done`.** On counted items it counts posts that are live;
  filling it marks the item as Published. The agent moves it up as posts
  go out (or Claude does, later, if they ask).
- Skip any item at `approved`, `scheduled` or `done`, and any item at
  `changes` unless this run is the revision the agent asked for.
- If a write fails because the item changed meanwhile, read it again and
  redo that one write. Don't overwrite their change.
- Don't touch `config`, `calendar`, `ideas` or other months. Don't mark
  ideas as used unless the agent asks.

## Approval (Step 8)

The agent approves either by telling you, or on the dashboard (status
`approved`). Before loading Metricool drafts in a later run, read the
month's items and load drafts only for items that are `approved`. Set an
item to `scheduled` only if the agent asks.

## The social plan document (Step 6)

Dashboards with a **Social plan** tab (look for `id="tab-social"` in the
page; older ones can be upgraded with the Command Center skill's
`scripts/upgrade_dashboard.py`) read the plan from one document:
collection `social`, doc id `YYYY-MM`. Write it with `set` from a local
JSON file (`file_path`), pinned with its version if it already exists.

```json
{"month": "2026-11", "theme": "<year-plan theme>", "designUrl": "<canvas URL>",
 "todo": ["Add the live link to the home value blog", "..."],
 "sources": [{"title": "<blog or report title>", "link": "<URL or empty>"}],
 "posts": [{"n": 1, "date": "2026-11-02", "time": "9:30 AM",
   "networks": ["Instagram", "Facebook"], "format": "Feed post",
   "title": "<short name>", "source": "<where it came from>",
   "item": "<checklist key this post counts toward>",
   "onImage": "<label / headline>", "slides": ["<carousel slide copy>"],
   "script": "<video or reel script, plain text>", "caption": "<full caption with sign-off>"}],
 "updatedAt": "<ISO time>"}
```

- `format` is one of `Feed post`, `Carousel`, `Market graphic`, `Video`,
  `Reel`, `B-roll`, `Short tip`, `Google Business`. Leave out fields a post
  doesn't have (`slides` for single images, `script` for designs).
- `item` must be the key of a real item in `months/YYYY-MM/items`, so the
  post shows that item's status.
- Google Business posts: `caption` is the Google text, `script` is just the
  `IMAGE:` and `BUTTON:` lines, and `reuses` is the number of the designed
  post whose image it reuses (Step 8 loads that post's image with it).
- Rewriting the plan replaces `posts`. Caption edits live separately (below)
  and are keyed by post number, so keep post numbers stable on revisions.

## Caption edits (read before Metricool)

When someone edits a caption on the Social plan tab, it is saved to
collection `social/YYYY-MM/edits`, doc id = the post number, as
`{caption, by, at}`. The original stays in the plan document. Before
loading Metricool drafts or revising the plan, `list` this collection and
use each edited caption in place of the original. Don't delete edits; the
agent removes them with **Restore original**.
