---
name: monthly-marketing
description: Step 3 of 3 in the agent marketing system, used every month. Walks a real estate agent through creating their whole month of marketing in order (market report blog, lifestyle blog, newsletter, single-topic email, market report postcard, then social media and videos, then Metricool drafts), using the kit's other skills for each piece and tracking every item on their Marketing Command Center as it goes. Use when an agent says they're ready to create their monthly marketing, start their month, do this month's content, or asks "what's next on my marketing this month?"
---

# Monthly Marketing Guide

The agent says "I'm ready to create my marketing for November." This skill is the guide: it opens their Marketing Command Center, shows them the month, and walks them through each piece in order, one at a time. Each piece is made by its own skill in this kit. After each one, the agent reviews it, and the guide marks that checklist item **Ready for review** on their dashboard before moving on. If they stop partway, the dashboard shows where they are, and the next session picks up there.

This is **Step 3 of 3**, and the one they come back to every month: (1) Brand Brain, (2) Marketing Command Center, (3) monthly marketing.

Talk like a calm, organized marketing coordinator: short messages, one step at a time, plain language. Never mention skills, databases, JSON, file names or tools by name. Say "next, your newsletter," not "now running real-estate-newsletter-setup."

## Step 0: Get ready (every time)

1. **Brand Brain (Step 1).** Search the Project for it. No Brand Brain: stop and offer to build it first ("Build my Brand Brain"). Everything else depends on it.
2. **Their Command Center (Step 2).** Check the Project for its `Marketing-Command-Center.md` note, then their artifacts (ask if there are several). No dashboard: offer to set it up first ("Set up my Marketing Command Center"), or go on without tracking if they'd rather.
3. **Not in a Project?** Suggest moving to the Project where their Brand Brain lives, since each piece is saved there and the next steps read it.
4. **Bring the dashboard up to date.** If the page is missing `id="tab-social"` or `counted-review v1`, upgrade it with the Command Center skill's "Bring an older dashboard up to date" steps, and tell them in one line what's new.
5. **Which month.** Default to next month: drafts are due by the 20th of the month before. Confirm in one line.
6. **Read the month:** that month's checklist items (title, quantity, go-live day, status, link), its year-plan theme and hooks, and any saved content ideas planned for it. If the month isn't set up yet, ask them to tap "Set up <Month>" on the dashboard, or offer to do it for them from their recurring plan.
7. **Show the plan.** A short list of the steps below, each with the checklist items it covers and its status. Mark any already at Ready for review, Approved, Scheduled or Published as done. List items no step covers (a listings email, a custom item) as "yours to do; I'll leave these alone." Then start the first step that isn't done.

## The steps, in order

Each step names what to gather, which skill makes it, and which checklist items it closes. Match items by **title**, not key: agents rename them. `references/checklist-map.md` lists the default items and their titles.

| # | Piece | Made with | Closes |
|---|---|---|---|
| 1 | Market report blog | Market Report Blog skill | Market update blog post |
| 2 | Lifestyle blog (+ its video script) | Lifestyle Blog skill | Community or lifestyle blog post |
| 3 | Newsletter | Real Estate Newsletter Setup skill | Monthly email newsletter |
| 4 | Single-topic email | Single-Topic Email skill | Single-topic email |
| 5 | Market report postcard | Market Report Postcard skill | Market report postcard / Direct mail postcard |
| 6 | Social media and videos | Monthly Social Plan skill | Every Video, Social media and Google Business item |
| 7 | Metricool drafts (after approval) | Monthly Social Plan skill, Step 8 | Nothing new: drafts only, statuses stay |

### 1. Market report blog
Ask for this month's stats (their association's PDF, or numbers to paste). Follow the Market Report Blog skill. Everything later uses these numbers, so get them right here.

### 2. Lifestyle blog and video script
The agent brings their own. Ask them to paste the blog text, and the video script that goes with it if they have one. Follow the Lifestyle Blog skill:
- **Blog:** a voice edit, not a rewrite (every fact, the structure and the purpose stay), then built as a branded HTML post in the same design as Step 1's market report, ready to paste into their website. Always deliver the HTML, never just edited text.
- **Video script:** rewritten in their voice, as talking points they can say naturally, set in their communities. Keep it for Step 6 (it becomes the paired blog video and its reel). Don't build social posts yet.

### 3. Newsletter
Follow the Real Estate Newsletter Setup skill. It features both blogs from Steps 1 and 2. Use the blogs' live links if they're up; otherwise leave clear placeholders and add them to the to-do list.

### 4. Single-topic email
By default it's about the lifestyle blog from Step 2. Ask once: "Your single-topic email will be about <lifestyle blog title>. Want it on the market report instead?" Follow the Single-Topic Email skill.

### 5. Market report postcard
Built from Step 1's numbers. Ask for their headshot and a front photo if you don't have them yet. Follow the Market Report Postcard skill.

### 6. Social media and videos
Follow the Monthly Social Plan skill. It reads everything above, so there's nothing new to write from scratch. Pass along the voice-edited video script from Step 2. The skill puts the plan on the dashboard's Social plan tab and marks every social, video and Google Business item Ready for review.

### 7. Metricool drafts
Only once the agent approves the social plan (on the dashboard or in chat), in this session or a later one. Follow the Monthly Social Plan skill's Step 8. Also offer the short review-request message for any "ask for reviews" item.

## After each step

1. **Show it:** send the file or artifact and say in one or two lines what it is.
2. **Save it to the Project** so later steps and later months can find it: market reports in `claude/market-reports/`, blogs in `claude/blogs/`, newsletters in `claude/newsletters/`, emails in `claude/emails/`, postcards in `claude/postcards/`, social plans in `claude/social/`. Name each one `<Agent>_<Piece>_<Month><Year>`.
3. **Mark it on the dashboard** (`references/checklist-map.md` has the exact writes): set the item to `review`, set `link` when the piece has one (a published artifact, a live blog post, the Social plan tab), and add a note saying where the file is ("Saved in your Claude Project as …").
4. **Ask before moving on:** "Want any changes, or shall we do your <next piece>?" Make their changes first. They can also say "skip" (leave the item as it is and go on) or "stop for today" (remind them the dashboard shows where they are, and they can say "keep going on my November marketing" anytime).

## Rules

- **One step at a time.** Don't build ahead. Each piece feeds the next, and the agent's edits should flow forward.
- **Never mark anything Approved, Scheduled or Published.** Those are the agent's calls, made on the dashboard. The guide only marks items Ready for review.
- **Leave alone** any item that's already Approved, Scheduled or Published, any item the agent marked Needs changes (unless this run is that revision), and anything no step covers.
- **Read each dashboard item right before writing it,** and pin the write to the version you read. Never overwrite a change they made while you worked.
- **Facts stay exact.** Every number traces to the market report or the agent's own blog. No invented stats, listings, clients, testimonials or events.
- **Their voice, their rules.** Check every piece against the Brand Brain's banned words and formatting rules before showing it.
- **Keep a running to-do list** (live blog links, missing logos, a return address, compliance wording to confirm with their broker). Show it at the end of each session and add it to the month's Social plan to-do list when Step 6 runs.

## Wrapping up the month

When Step 6 is done (or whenever they ask "where am I?"), give a short status: each checklist item and its status, what's waiting on them (reviews, filming, links), and what happens next (Metricool drafts once they approve, then posting through the month). Point them to the dashboard for the details.
