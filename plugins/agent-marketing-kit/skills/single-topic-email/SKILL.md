---
name: single-topic-email
description: Turns one of a real estate agent's blog posts (by default the month's lifestyle or community blog, or the market report if they choose) into a single-topic email ready to paste into Mailchimp, Constant Contact or another email platform, in the same design as their monthly newsletter. Use when an agent asks for their single-topic email, e-Report, blog email, or "an email about this blog post."
---

# Single-Topic Email

One email, one topic. It takes a blog post the agent has already written and turns it into a short email their database can read in a minute, with a button to the full post. It uses the same look as their monthly newsletter (`assets/template.html` is built from the newsletter template), so the two feel like one brand.

Talk to the agent in plain language. Don't mention file names or HTML tags.

## Which blog

- **Default: the month's lifestyle or community blog.** The market report already reaches the database through the newsletter, the postcard and the social posts. The lifestyle blog only appears as a teaser in the newsletter, so it gets its own send.
- **Use the market report instead** if the agent asks, or if there's no lifestyle blog this month. Then the points are the report's three or four biggest moves, with every number exactly as the report has it, plus its source and month.
- Never write about a post you haven't read. If it isn't in the chat or the Project, ask them to paste it.

## What it uses

1. **The blog post:** its title, sections, best facts and tips, image, and live link (leave `[ADD: link to the live post]` if it isn't live yet).
2. **The Brand Brain:** voice, banned words and formatting rules, colors, standard CTA, contact method, compliance and hosted logo link.
3. **Their newsletter**, if one was built this month or earlier: copy its colors, logo, footer and compliance choices exactly, so the two match. The newsletter skill's "Design defaults" and "Hard-won gotchas" apply here too: one background color, Times New Roman, centered headings with left-aligned reading text, hosted image links only, and no comment inside another comment.
4. **The blog video**, if it's already posted: add the optional video block. Otherwise delete it.

## Build it

1. Copy `assets/template.html` to a new file named for the agent and month (for example `Claire_Morgan_Single_Topic_Email_November2026.html`).
2. Fill every `[BRACKETED TOKEN]`. The design tokens at the top of the `<style>` block match the newsletter's.
3. **Headline:** the blog's title or its main question, shortened to fit on two lines.
4. **Opening:** two or three sentences in the agent's voice, first person: why this topic, why now, and a personal detail from the Brand Brain if it fits naturally.
5. **Points:** three to five, following the blog's sections in order. Each gets a short heading and two or three sentences with that section's most useful fact or tip. Rewrite in the agent's voice; don't paste paragraphs from the post. Keep it short: the email should take about a minute to read. If any point has a statistic, fill the sources line under the points with each publisher and month; otherwise delete it. Repurpose the blog's facts, not its phrasing: rewrite catchy lines ("Not what you paid. Not what a neighbor guessed.") rather than lifting them, and drop phrases the Brand Brain bans even when the blog uses them.
6. **Pull quote** (optional): one line worth repeating. Then one line on what else the full post covers, and the "Read the Full Post" button. No sign-off name: it looks out of place at the bottom of a one-topic email.
7. **Closing panel:** their standard CTA, calm and never urgent.
8. **Compliance and footer:** same as their newsletter. Keep the ESP bar with its merge tags.
9. Delete any section without content. Check the whole email against the Brand Brain's banned words and formatting rules (and the Brand Voice Editor's AI tells, if installed). Fair housing: describe places, never who should live there.

## Deliver

- The HTML file, plus 3 to 5 subject lines under about 45 characters and preview text that teases two or three things inside without repeating the opening line (the newsletter skill's `references/subject-lines-and-preview-text.md` has the patterns).
- Paste instructions: in Mailchimp, a "Code your own" template or a code block; in other platforms, their custom HTML option.
- The list of anything still to add, usually the live blog link.

## If there's a Marketing Command Center

Set the month's single-topic email item to Ready for review with a note of where the email is. Follow the Command Center's data rules: read the item first, write pinned to its version, and leave it alone if it's already Approved, Scheduled or Published.
