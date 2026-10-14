---
name: brand-brain-builder
description: Self-guided walkthrough for a real estate agent to build their own "Brand Brain," a permanent reference document covering who they are, who they serve, their voice, proof, content rules, CTA and compliance, so every future marketing task (blogs, reels, emails, postcards) sounds like them and not like generic AI. Use this whenever an agent says they want to build or update their brand brain, brand guide, brand voice, voice guide, or "something I can give Claude so it sounds like me," or when they ask where to start with marketing content, or paste a worksheet, Google reviews, or notes about their business and want them turned into a reusable reference. Trigger even if they never say "Brand Brain."
---

# Brand Brain Builder

This skill helps a real estate agent build their own Brand Brain: one document they can hand to Claude (or a teammate, VA, or freelancer) at the start of any marketing task so nobody has to guess who they are.

The agent is doing this for themselves, not with a consultant. Talk to them as a friendly, sharp collaborator. Use "you" and "your." Keep it moving, and don't lecture about branding theory. The document you produce is written in the agent's voice ("Who I Am," "My Voice") because it will be pasted into future chats as their own reference.

## Why this exists

Generic output happens when the writer has to guess. The Brand Brain removes the guessing. Everything below is built to make the result specific enough that a stranger could imitate the agent from it. A section that could describe any agent in their market is a failed section.

## How the session runs

Follow these stages in order. Say one short sentence at the start of each stage so the agent knows where they are.

### Stage 1: Welcome and set expectations (one short message)

Tell them, in a few lines:
- This takes about 15 to 20 minutes.
- They will give you raw material (rough answers are fine, fragments are fine, voice-to-text is fine).
- You will ask one batch of follow-up questions, then build the document.
- You will never invent facts, stats, or awards. Anything missing gets flagged as MISSING.

Then ask for the raw material. Offer two paths and let them pick:
1. **Worksheet path:** walk them through the questions in `references/worksheet.md`. Ask a few at a time, not all at once. Ten questions in one message overwhelms people.
2. **Paste path:** they paste notes, an existing bio, a website About page, or a past worksheet.

Also ask, as optional but strongly recommended:
- Their Google reviews (copy and paste the review text). This is the best source of honest proof and of how clients actually describe them.
- Their brokerage name and any compliance rules they already follow.

### Stage 2: Read everything before writing

Read all of it first. Do not start drafting. Note:
- What is clear and specific (keep their exact words wherever possible).
- What is vague or generic ("great service," "I care about my clients").
- What is missing from the ten sections in `references/template.md`.
- Anything contradictory (for example, they say they serve everyone but their goals point to one group).

### Stage 3: One batch of clarifying questions (maximum eight)

Ask all of them in a single message, numbered. Prioritize gaps that would cause generic output:
- Ideal client unclear, or a deliberate shift in who they want to serve. Ask what each group actually worries about in the first conversation, in their own words.
- Differentiators that sound like every other agent. Ask for the specific thing only they can say.
- Voice is thin. Ask them to pick three words, then ask about sentence rhythm (short and punchy or longer), contractions, humor, and anything they never say.
- CTA is missing or unclear. Ask what they want someone to do after a post or reel, and whether that thing exists yet.
- Name or brokerage spelling is inconsistent anywhere in the material. Confirm it. Reviews and brokerage listings are a good cross-check.
- Compliance. Ask what their brokerage requires on marketing pieces. If they are unsure, that is fine. Mark it MISSING and tell them to confirm with their broker.
- Refusals. Ask what they will never post (bashing other agents, religion, politics, trend-chasing, whatever applies).
- Life outside work. Ask what they would genuinely post about, and confirm any claim like "born and raised here."

If the answers they already gave cover a question, skip it. Fewer, sharper questions beat a full eight. If the agent answers some questions and not others, confirm what you locked in, then re-ask only what is still open, trimmed down. Do not re-ask answered questions.

### Stage 4: Build the document

Use the ten-section structure in `references/template.md`. Rules that matter:

- **Use their words.** Where you must write, match the rhythm of their fragments. If they write short sentences, you write short sentences.
- **Do not invent anything.** No stats, awards, years in business, days on market, volume, or results they did not give you. Write `MISSING:` followed by the specific thing that is missing. A visible gap is more useful than a confident guess.
- **Separate goals from results.** "Doubling transactions next year" is a goal. Label it so nobody posts it as an achievement.
- **Ban the clichés.** Always include this default banned list in Section 5, plus anything they add: stunning, dream home, unlock, elevate, nestled, must-see, hidden gem, luxury living, in today's market.
- **Make Section 4 (voice) imitable.** Another writer should be able to copy the agent from it. Include tone in three words, sentence rhythm, formality, humor, and formatting rules (for example, no em dashes). If the agent mentions their age or life stage as a voice factor, capture it so future content does not sound like a different person.
- **Pull proof from real reviews.** Summarize themes, not invented quotes. Name specific, verifiable details (a repeat client, a type of purchase) only if they appear in the material.
- **Flag unbuilt CTAs.** If a lead magnet, form, or landing page does not exist yet, say so and give the working CTA to use until it does.
- **Put the compliance sign-off block in verbatim,** exactly as the agent supplies it, and state that it goes at the end of every social post. Never write contact details or license numbers from memory.
- **Avoid em dashes in your own drafting** if the agent's voice rules say to. It is also a good habit for the document itself.

Save the result as a Markdown file named `[Agent-Name]-Brand-Brain.md` and send it to them. If they prefer a Word doc or Google Doc, convert it.

### Stage 5: Self-check before showing it

Ask yourself honestly: could this document describe any other agent in their market? If yes, tell the agent which sections are too generic and exactly what you need from them to fix it. Do not hide a weak section. Typical weak spots: differentiators, proof with no numbers, thin vocabulary list.

### Stage 6: Hand it over and show them how to use it

After delivering, tell them in plain language:
1. Save the file somewhere permanent. Best option: put it in a Claude Project so it is available in every chat. Otherwise paste it at the start of any marketing task.
2. List any `MISSING:` items and what would fix each one. Offer to update the file as soon as they have the answers.
3. Offer a few starter tasks they can run right now, like a reel script, a blog outline for a topic their ideal client searches, or a monthly email.
4. Remind them to update the document whenever goals, proof, compliance rules, or ideal client focus change.

If they ask what else they should be doing for content, suggest ideas that fit their stated goals and brand (for example: client testimonial clips, a recurring series for their ideal client's biggest question, local business spotlights, simple market updates in plain language, behind-the-scenes content from their real life). Offer to add a content pillars list to Section 8 rather than adding it unasked.

## Updating an existing Brand Brain

If they already have one, read it first, ask what changed, and edit only the affected sections. Keep their existing wording where it is still true. Preserve MISSING flags until they are resolved, and remove each flag only when the agent gives the answer.

## Things to avoid

- Do not write marketing copy during this session. The goal is the reference document.
- Do not assume what clients worry about. Ask. Guessing is the main cause of generic output.
- Do not fill gaps with plausible-sounding details, even small ones.
- Do not present a goal, an aspiration, or a planned project as a current fact.
- Do not pressure them to answer everything. A document with honest MISSING flags beats one padded with filler.
