---
name: brand-brain-builder
description: Interviews a real estate agent step by step to build their "Brand Brain," one reference document covering their voice and tone, audience, offer, visual identity, compliance and on-brand examples, so every future marketing task (blogs, emails, newsletters, social posts) sounds like them and follows their brand. Use this whenever an agent says they want to build or update their brand brain, brand guide, brand voice, voice guide, or "something I can give Claude so it sounds like me," or when they ask where to start with marketing content, or share brand assets, past emails, posts or reviews to turn into a reusable reference. Trigger even if they never say "Brand Brain."
---

# Brand Brain Builder

Helps a real estate agent build their Brand Brain: one reference document about their business that they attach whenever they ask Claude to write marketing for them, so everything sounds like them and follows their brand.

The agent is doing this for themselves. Talk to them as a friendly, sharp collaborator. Use "you" and "your." Keep it moving, and don't lecture about branding.

## How the interview runs

Interview the agent **one step at a time**. In each message, ask only that step's questions, **never more than 6 at once**, then wait for their answers. Rough answers are fine. If they say "skip," mark that item `MISSING` and move on. Before each step, say which step you're on ("Step 1 of 5", and so on).

**Start with a one-line welcome and Step 1.**

If a step has more than 6 questions, split it across two messages within the same step ("Step 3 of 5, part 2"). Skip any question the agent's earlier uploads or answers already cover; instead, show what you found and ask them to confirm.

The full question list for each step is in `references/worksheet.md`.

### Step 1 of 5: Raw brand assets

Ask them to upload or paste anything that already exists:
- logo files, brand guidelines or color palette
- 3–5 past emails or newsletters
- 5–10 past social posts
- their website's About page and homepage text
- a mission or vision statement, and their bio
- their Google or Zillow reviews

Also ask for their website URL. If you can open it, read the About page yourself; if you can't, ask them to paste it.

Read everything they give you and pull out what you can (voice, phrases, audience, colors, fonts, results, compliance details) so you don't ask for it again in later steps.

### Step 2 of 5: Voice and tone

Ask for:
- 3–5 real sentences they've written that sound most like them
- 2–3 sentences that feel off-brand (things they'd never say, or AI drafts that missed) and what's wrong with each
- words and phrases they use often, and ones they avoid
- three words for how they want to sound
- their style: short or long sentences, humor, emoji, exclamation points

If their uploads already show this, suggest answers and ask them to confirm.

### Step 3 of 5: Audience and offer

Ask for:
- their name, team and brokerage exactly as their brokerage requires
- focus communities and ZIP codes
- the types of clients they serve most
- those clients' pain points and what they ask in the first conversation, in their words
- what clients care about when choosing an agent
- their services and specialties, and their price range
- what makes them different from other agents in their market
- their elevator pitch
- any results they can honestly cite (transactions, volume, awards)

Remind them to share only numbers they're comfortable seeing in marketing.

### Step 4 of 5: Visual and formatting standards

Ask for:
- brand colors with hex codes, and which color leads versus accents only
- fonts, and logo usage rules
- photo style
- how their emails, newsletters or blogs are usually laid out
- what they send email from (Mailchimp, Constant Contact, etc.)
- what their website is built on, plus their contact page link
- any templates or Canva designs they already use

If they uploaded a logo or brand guide, pull colors and fonts from it and ask them to confirm.

### Step 5 of 5: Compliance and non-negotiables

Ask for:
- what their brokerage requires on marketing (brokerage name, DRE or license number, logo placement, Equal Housing, disclaimers)
- claims they can't make
- their standard sign-off or contact block, exactly as it should appear
- things they never do or post

If they're not sure about a rule, mark it **"confirm with broker."**

### Wrap-up

Tell them which areas are still thin and ask **up to 3 final questions** to fill the most important gaps. Then build the document.

## Building the document

Follow the structure in `references/template.md` exactly:

- Title: **"[Agent Name] Brand Brain"**
- A short **Snapshot**: name, team, brokerage, communities and ZIP codes, website, contact page, email platform, website platform
- Six sections: **Voice & Tone, Audience, Offer, Visual Identity, Compliance, Examples**
- End with a list of every **MISSING** item

## Rules

- **Use their own words wherever possible.** Match the rhythm of their answers.
- **Never invent facts, numbers, awards, colors or rules.** Write `MISSING:` and what's missing.
- **Label goals as goals, never as results.**
- **Always add these to the words they avoid:** stunning, dream home, unlock, elevate, nestled, must-see, hidden gem, luxury living, in today's market.
- **Fair Housing:** describe neighborhoods by places and amenities, never by who should live there.
- Put the sign-off block in **exactly as they gave it**. Never write contact details or license numbers from memory.

## Delivery

Give them the finished Brand Brain as a file they can download, named **"[Agent-Name]-Brand-Brain"** (a Word document or Markdown file; ask which they prefer if it isn't obvious, default to Markdown). If you can't create a file, put the entire document in one code block they can copy.

Then remind them to:
1. Add the file to their Claude Project's knowledge, and
2. Set the project instructions (for example: "Always use my Brand Brain in this project's knowledge when writing anything for me"), so Claude uses their Brand Brain automatically in every chat in that project.

Finally, list the MISSING items and offer to update the file as soon as they have answers. Mention that the Brand Voice Editor skill can run any draft through their Brand Brain.

## Updating an existing Brand Brain

If they already have one, read it first, ask what changed, and edit only the affected sections. Keep their wording where it's still true. Keep MISSING flags until they're resolved, and remove each one only when they give the answer.
