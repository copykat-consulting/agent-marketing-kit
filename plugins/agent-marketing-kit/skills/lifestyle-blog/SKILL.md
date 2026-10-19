---
name: lifestyle-blog
description: Takes the lifestyle, community or seller blog a real estate agent brings (pasted text, a doc or a file), edits it into their voice with their Brand Brain, and builds it as a branded, self-contained HTML blog post that matches their monthly market report blog, ready to paste into their website (Luxury Presence, Squarespace, WordPress and similar). Use when an agent shares their blog for the month, asks to "format my blog," "code my lifestyle blog," "make my blog match my market report," or pastes a blog post to publish.
---

# Lifestyle Blog

The agent writes or brings their own lifestyle blog each month. This skill makes it publish-ready: their voice, their market, and the same design as their market report blog, so the two posts look like one brand on their website.

Output: one HTML file built from `assets/template.html`, plus short paste instructions. Talk to the agent in plain language; don't mention CSS or file internals.

**Read `assets/template.html` in full before building.** It uses the Market Report Blog's design: same CSS, scoped under `.mr`, same brand variables and fonts. Keep its classes and structure; only the brand variables, placeholders and repeated section blocks change.

## Step 1: Gather

1. **The blog.** Pasted text, an uploaded file (.docx, .txt, .md, PDF) or a Google Doc if a connector is available. If they also have a video script for it, take that too: it's voice-edited here and used later for the blog video (the Monthly Social Plan picks it up).
2. **Their Brand Brain** from the Project. No Brand Brain: offer to build one first, or do a quick voice check (three tone words, phrases they use, words they never use, their call to action, brokerage name and license wording).
3. **Their design.** Look in the Project for this month's (or last month's) market report post. If there is one, copy its font link and its whole `<style>` block (it carries any tweaks made for this agent, like a different button or callout color), drop the rules for the stat bar, tables and community headers, and append the "Lifestyle blog additions" rules from the template with the font names swapped to theirs. That's what makes the two posts match. If there's no market report yet, use the template as is with the Brand Brain's colors and fonts, the same way the Market Report Blog skill does.
4. **Photos.** Hosted, public image links only (ImageKit or similar), from the Brand Brain's image list or links they give you. A website can't show a file from their computer. No suitable link: delete that image box rather than leave a placeholder. Never present a lifestyle photo as a specific listing.
5. **Live links** the post mentions (their website, a valuation page). Missing: leave `[ADD: …]` and list it at the end.

## Step 2: Edit the words (voice pass)

Follow the Brand Voice Editor skill's rules. This is an edit, not a rewrite:

- Keep every fact, number, source, place and the post's structure and purpose.
- Fix the voice: their rhythm, their phrases, first person ("I" for a solo agent, "we" for a team), their communities in place of generic ones.
- Remove their banned words and formatting (many ban em dashes), clichés and AI tells.
- Replace any call to action with their standard one, calm and never urgent.
- Remove anything their Brand Brain rules out: other brokerages' or agents' names that don't belong to them, claims they can't make, transaction counts, steering language. Fair housing: describe places and amenities, never who should live there.
- Every statistic keeps its source. If the post gives a number without one, ask, or add the source the post names elsewhere and flag it for them to confirm.
- Tighten long paragraphs to three sentences or fewer. Keep their headings, sharpened if needed.

Show the agent a short list of what you changed and why (banned words removed, names removed, CTA swapped, sources added), not the whole diff.

## Step 3: Build the HTML

Copy `assets/template.html` to a new file named `<Agent>_Lifestyle_Blog_<Month><Year>.html` and:

- Set the brand variables and fonts (Step 1.3).
- **Kicker:** a short category (For Sellers, Life Inland, Horse Property, Things to Do) and the month.
- **Headline:** the post's title, or a sharper version. The website's own title field shows the post title too.
- **Intro:** the opening as `<p class="lede">`, then any second paragraph.
- **One section block per section of their post**, in their order, using only what each section needs: paragraphs, `ul.checklist` for tips or a checklist, `ol.steps` for steps in order, `div.spot` for a place, business or trail, `div.insight` for one practical takeaway, and an image box where there's a real hosted photo.
- **Pull quote:** one line worth repeating, from the post, in their voice.
- **Closing section** with the post's own wrap-up.
- **Sources line** only if the post cites statistics: each publisher and month.
- **CTA box:** their standard call to action, button to their contact page, booking link or a `mailto:` with a subject, plus phone and email.
- **Compliance line** exactly as the Brand Brain requires, unless their website footer already carries it (ask once, then remember it in the Project).
- Delete every unused block. A finished file has no `[BRACKETS]` left except `[ADD: …]` items you list for them.

Check it: open the file in a browser preview at desktop and phone widths, and look at it. Fix anything clipped, crowded or unbranded.

## Step 4: Deliver

- The HTML file, and save it to the Project as `claude/blogs/<Agent>_Lifestyle_Blog_<Month><Year>.html`.
- Paste instructions for their platform: Luxury Presence (Post Body → custom HTML / code block), Squarespace (Code block), WordPress (Custom HTML block). Tell them to paste everything from `<link` through the closing `</div>`, and to set the post title, slug and featured image in the platform's own fields.
- The voice-edited video script, if they brought one, saved to the Project for the social plan.
- What's left to add (live links, photos), and an SEO title (under 60 characters) and meta description (under 155 characters) they can paste into the platform.

## If there's a Marketing Command Center

Set the month's lifestyle or community blog item to Ready for review with a note saying where the file is. Follow the Command Center's data rules: read the item first, write pinned to its version, and leave it alone if it's already Approved, Scheduled or Published. When the post is live, ask for its link so the newsletter, single-topic email and social posts can use it.
