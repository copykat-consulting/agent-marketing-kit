---
name: brand-voice-editor
description: Edits a real estate agent's draft (monthly community or lifestyle blog, market report, newsletter, email, social caption) against their Brand Brain so it sounds authentically like them instead of generic AI, while keeping every fact and stat intact. Use when an agent asks to "run this through my Brand Brain," make a draft sound more like them, make it more authentic, fix the voice, de-AI a post, or polish a blog before publishing.
---

# Brand Voice Editor

Takes a finished draft and the agent's Brand Brain, and returns a version that sounds like the agent wrote it: their rhythm, their words, their proof, their CTA, their compliance. It is an edit, not a new post. The facts, numbers, structure and purpose stay; the voice changes.

Talk to the agent in plain, friendly language. Don't lecture about writing.

## Step 1: Gather the two inputs

1. **The draft.** Most often this is the monthly community or lifestyle blog post, but any written piece works. Accept whatever they give you: pasted text, an uploaded file (.docx, .txt, .md, .html, PDF), or a Google Doc if a Google connector is available. Note the format; you'll return the same format.
2. **Their Brand Brain.** Look in this order and use the first you find:
   - A Brand Brain already in this chat, or attached
   - The current Claude Project's docs (search for "Brand Brain")
   - Ask them to paste or upload it
   If they don't have one, say so plainly and offer two paths: build it now with the Brand Brain Builder skill (best, about 15–20 minutes), or a 2-minute quick voice check: ask for three words for their tone, two or three phrases they actually say, words they never use, their usual call to action, and their brokerage name as it must appear. Label the result "quick voice check, not a full Brand Brain."

Read the whole Brand Brain before touching the draft. The parts that matter most are: **Voice & Tone** (tone, sentence style, formatting rules, words used and avoided), **Examples** (on-brand and off-brand sentences, the best guide to how they really sound), **Audience** (pain points in their words), **Offer** (what makes them different, results they can cite), **Compliance** (rules, claims they can't make, sign-off block) and the **Snapshot** (exact brokerage name, contact page). Older Brand Brains may use different headings (My Voice, Words I Use, Proof, Standard CTA); use whichever headings are there.

## Step 2: Diagnose before editing

Read the draft once all the way through and note, privately:

- **Voice mismatches:** sentence length, formality, humor, contractions, "we" vs "I," against Voice & Tone and the on-brand Examples.
- **Avoided words and clichés** from Voice & Tone, anything resembling their off-brand Examples, plus the generic AI patterns in `references/ai-tells.md`.
- **Formatting rules** from Voice & Tone (for example, no em dashes, no emoji, no exclamation points) that the draft breaks.
- **Missed authenticity:** places where a phrase they actually use, a real differentiator or result from Offer, a client pain point in their words from Audience, or a genuine local detail (their communities and ZIP codes) would make it unmistakably theirs.
- **Call to action:** does the ending point to their real next step (their contact page from the Snapshot, or a CTA named in the Brand Brain) in their voice, instead of a generic "give us a call!"?
- **Compliance:** brokerage and team name exactly as in the Snapshot, required disclaimers, claims they can't make, and their sign-off block (Compliance). Fair Housing: describe neighborhoods by places and amenities, never by who should live there.
- **Facts:** every number, date, percentage, price and source. List any stat with no source, or a source that's vague ("data shows").

## Step 3: Edit

Apply these rules:

- **Keep every fact exactly.** Don't change, round, add or drop numbers, dates, prices, percentages or sources. If a stat looks wrong or unsourced, keep it as written and flag it.
- **Never invent.** No new stats, client stories, testimonials, awards, years in business or personal anecdotes. Where a real story or detail would help, insert a clearly marked placeholder in the text, like `[ADD: a quick story about a seller you helped price right this year]`, and list it for them.
- **Only use proof that's in the Brand Brain.** Results listed under Offer are fair game; goals are not results. Never use a claim listed under "Claims I can't make."
- **Keep the structure and purpose.** Same sections in the same order, same headline intent and SEO topic, length within about 10% of the original. Rewrite headings only if they clash with the voice; keep them keyword-friendly.
- **Swap in their language.** Use their "words and phrases I use" where they fit naturally, and model sentences on their on-brand Examples. Remove every avoided word and AI tell. Don't overload: two or three signature phrases per post is plenty.
- **Match their rhythm.** If they write short and punchy, cut long sentences. If they're warm and conversational, loosen stiff ones.
- **Use their real call to action** at the end (their contact page or named CTA), and their sign-off block exactly as written under Compliance where it belongs.
- **Edit level:** default to a medium edit (voice, word choice, rhythm, CTA, compliance). If they ask for a "light polish," change only clichés, banned words, formatting rules and compliance. If they ask for a "full rewrite," you may restructure sentences and paragraphs freely, but the facts and section order still stay.
- **HTML drafts** (like a market report file): change only the visible text. Leave tags, classes, styles, links and data tables untouched, and return the full file.

## Step 4: Deliver

Return, in this order:

1. **The revised draft**, in the same format they gave you (a file for files; text in the reply for short pasted text). Name files like `<original name> - Brand Voice.<ext>`.
2. **What I changed** (5–8 bullets max, grouped: voice, words removed, words added, CTA, compliance). Quote one or two before/after examples so they can see the difference.
3. **Needs your input** (only if there's anything): each `[ADD: …]` placeholder, any stat to verify or source, any MISSING item from their Brand Brain that limited the edit (for example, no on-brand Examples or no sign-off block).
4. One line offering a next step, such as a lighter or stronger edit, or turning it into a newsletter blurb or social caption.

Don't paste a long list of every small change, and don't grade the original harshly; the person who wrote it may be the agent or their assistant.

## If the Brand Brain is thin

If key sections are MISSING or generic (no tone words, no phrases, no Examples), still do the edit with what's there, then tell them exactly which sections held the edit back and offer to update their Brand Brain with what you learned from this draft. Never fill those gaps yourself.
