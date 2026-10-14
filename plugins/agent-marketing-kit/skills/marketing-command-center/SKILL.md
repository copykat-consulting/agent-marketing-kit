---
name: marketing-command-center
description: Sets up a real estate agent's Marketing Command Center, a private dashboard with a monthly content checklist, review and approval workflow, social and Google Business performance from Metricool, a visual content ideas board and a 12-month year plan. Use when an agent asks to set up, build, rebuild or customize their Marketing Command Center, content dashboard or marketing tracker.
---

# Marketing Command Center setup

You are setting up a Marketing Command Center for a real estate agent or team. The finished product is ONE private, published artifact page built from `assets/template.html`, with the agent's own plan, team names, year themes and style stored in that artifact's database. Everything the agent sees comes from that database; never write their data into the HTML.

Speak to the agent in plain, friendly language. Most agents are not technical: don't mention databases, documents, JSON, capabilities or file names.

## Step 1: Check the setup they need

1. **Metricool connected to Claude.** Look for tools whose names contain `Metricool` (load deferred tools by searching for "metricool" if your session supports it).
   - If they're present, call the brand-settings tool (`getBrandSettings`) and note each brand's `label` and which networks are linked in `networksData` (Instagram, Facebook, LinkedIn, Google Business Profile).
   - If they're missing, tell the agent: "Your performance numbers come from Metricool. Create a Metricool account, link your Instagram, Facebook, LinkedIn and Google Business Profile there, then in Claude open Settings → Connectors and connect **Metricool Social Media Management**." Offer to continue now and have the numbers appear once it's connected. The checklist, ideas and year plan work without it.
2. If a network they use isn't linked in Metricool, mention it once; that card will say "Not connected yet" until they link it.

## Step 2: Interview the agent

Ask these in one or two short rounds (use a multiple-choice question tool if you have one). Offer the defaults so they can just say "yes":

1. **Team or brand name** as it should appear on the page (default: their Metricool brand label, text before any ":" or " - ").
2. **Agent's first name** and **assistant's first name** (if they have one; default "Assistant").
3. **Monthly content plan.** Show `assets/default-plan.json` as a short readable list grouped by section (Email, Blog, Video, Social media, Google Business Profile, Direct mail): title, how many, go-live day. Ask what to add, remove or change. Keys must stay unique, lowercase, letters/digits/hyphens. `qty` above 1 makes a counter (e.g. 15 feed posts). `dueDay` is the go-live day of the month (1–31). Channel must be one of: `Email`, `Blog`, `Video`, `Social media`, `Google Business Profile`, `Direct mail`, `Other`.
4. **Draft deadline.** Explain: "Every draft is turned in for review by the 20th of the month before it goes live, so November content is due October 20." This is built in. If they want a different day, note it and tell them it's currently fixed at the 20th (see "Changing the draft day" below).
5. **Brand colors (optional).** Ask for their main brand color (hex if they have it, or describe it). Optionally up to six section colors. If they skip it, keep the template's navy plus bright section palette.
6. **Font.** Offer the built-in options: Noto Serif Display + Jost (default), Instrument Serif, Playfair Display, DM Serif Display, Bodoni Moda, Cormorant, Gloock, Italiana, Fraunces, Plus Jakarta Sans, Outfit. They can also switch later with the page's Fonts button, or upload a licensed web font there.
7. **Year plan themes.** Offer the seasonal themes in `assets/year-themes.json` (keyed by month number 1–12) as a starting point and ask if they want any local events or topics swapped in. Light, generic local flavor is fine ("fall festivals nearby"); don't invent specific events, businesses or statistics.

## Step 3: Build the page

1. Copy `assets/template.html` to a working file named `marketing-command-center.html`. Change only these things in the copy:
   - **Brand colors** (only if they gave any): in the first `:root{ … }` block, set `--navy` to their main color (keep `--navy-ink` readable on it, usually `#ffffff`), and optionally `--c-email`, `--c-blog`, `--c-video`, `--c-social`, `--c-gbp`, `--c-mail`. Then set lighter versions of the same tokens in BOTH dark-theme blocks (`@media (prefers-color-scheme: dark)` and `:root[data-theme="dark"]`), where `--navy` must stay a light color and `--navy-ink` dark. Check text contrast.
   - **Default font:** find `S.font = "noto";` and change `"noto"` to the chosen id: `noto`, `instrument`, `gloock`, `italiana`, `fraunces`, `playfair`, `dmserif`, `bodoni`, `cormorant`, `jakarta` or `outfit`.
   - Change nothing else. All the logic, layout and Metricool wiring are already done.
2. Publish it as a NEW artifact with:
   - `icon`: `"checklist"`
   - `description`: "Monthly content checklist, review workflow, social performance, content ideas and year plan."
   - `capabilities` exactly:
     ```json
     {"db": {}, "user": {"scopes": ["profile"]}, "assets": {}, "sample": {}, "mcp": {"servers": [{"server": "Metricool Social Media Management", "tools": ["getBrandSettings", "getAnalyticsDataByMetrics"]}]}}
     ```
   If the publish is refused because of the Metricool entry (for example the connector isn't available on their account), publish again without the `mcp` key, and tell the agent the Performance numbers will appear once Metricool is connected and you republish.

## Step 4: Load their data

Write everything to the new artifact's database in ONE batch (use the artifact data tool's batch action; at most 50 writes). Let `YYYY-MM` be the current month and `NEXT` the following month.

| Collection | Doc id | Data |
|---|---|---|
| `config` | `plan` | `{"items": [ …their plan items… ]}`, each `{key, title, channel, qty, dueDay}` |
| `config` | `team` | `{"agent": "<agent first name>", "assistant": "<assistant first name>"}` |
| `config` | `style` | `{"font": "<font id>"}` |
| `calendar` | `YYYY-MM` for each of the next 12 months starting with the current one | `{theme, market, community, email, hooks}` from the agreed themes |
| `months/YYYY-MM/items` | each plan item's `key` | `{key, title, channel, qty, dueDay, status: "todo", done: 0, link: ""}` |
| `months/NEXT/items` | each plan item's `key` | same as above |

If that's over 50 writes, split it into two batches (config and calendar first, then the month items).

Do not create content ideas, review notes or statuses for them. Those are theirs to add.

## Step 5: Hand it over

Tell the agent, briefly:
- The page is private to them. To bring in an assistant, use the page's Share menu, invite them by email with **Can edit**; the assistant needs their own Claude account. (The Performance page and "Fill in from screenshot" use the agent's own Claude and connectors, so those work for the agent only.)
- How it works:
  - **This month:** progress, network snapshots, a tracker for next month's content (due the 20th), the review queue, and checklist cards by section. Status is a drop-down: Not started → Drafting → Ready for review → Needs changes → Approved → Scheduled → Published. Setting "Ready for review" asks for the Google Doc or draft link.
  - **Performance:** Instagram, Facebook, LinkedIn and Google Business numbers from Metricool, month over month.
  - **Content ideas:** paste a reel link and add a screenshot; Claude reads the hook, caption and likes from the screenshot. Plan ideas into any month and add them to that month's checklist in one tap.
  - **Year plan:** monthly themes and topics; tap Edit on any month.
  - **Fonts** button: try other fonts live.
  - Each new month: tap "Set up <Month>" to load the recurring items.

## Changing things later

- **Plan, team names, themes, font:** the agent can change most of these on the page itself. If they ask you, update the matching document in the artifact's database (read it first and pass its version).
- **Colors or layout:** read the artifact, edit its HTML and republish to the same artifact.
- **Changing the draft day:** in the HTML, find `S.draftDay = 20;` and change the number, then republish.

## Rules

- One artifact per agent. Never reuse or write to another agent's artifact.
- Keep all of the agent's data in the artifact's database, never in the HTML.
- Don't invent performance numbers, reviews, listings or client names.
