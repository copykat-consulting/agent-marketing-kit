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
- `qty` above 1 is a counted item (e.g. 15 feed posts); `done` counts how
  many are finished.
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
 "data": {"status": "review", "link": "<plan page URL>", "done": 15},
 "if_version": 7}
```

- `link`: the plan page URL for copy, script and calendar items; the design
  canvas URL for items that are only designs (e.g. the market stats graphic).
- `done`: only for counted items; the number you actually produced.
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
