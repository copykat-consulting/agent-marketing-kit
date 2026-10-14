---
name: "real-estate-newsletter-setup"
description: Builds a real estate agent's monthly email newsletter as a self-contained HTML file ready to paste into Mailchimp, Constant Contact or another email platform, with a hero, video spotlight, article features and a listings grid in the agent's brand. Use when an agent asks to set up, build or update their monthly newsletter, email newsletter or Mailchimp email.
---

# Real Estate Newsletter (Generic Template)

This is the reusable base this whole newsletter format was built from. It
produces a monthly email newsletter with: an optional branded header, a
seasonal/topical hero section, a video spotlight (position configurable —
above or below the article features), up to 4 rotating article features
(one of which is often a recurring market report), a 4-listing grid with
status tags, and an optional branded footer — all in one table-based HTML
file for maximum email-client compatibility.

This structure was proven out over many months of real revisions with
real estate teams. The "Hard-won gotchas" section below exists because of
real mistakes caught in that process. Read it before building; it'll save
you from repeating them.

## First-time setup for an agent

In this skill, "the client" means the agent or team whose newsletter you're
building (often the person you're talking to).

1. **Get or build a brand reference doc first.** Don't start filling in the
   template from a blank slate. If the client has a "Brand Brain" project
   doc (or similar), read it in full. If not, ask for (or help them
   establish): color palette (which colors are dominant vs. accent-only —
   most real estate brands have ONE lead accent color and should not spread
   accent weight evenly across 2-3 colors), headline and body fonts, voice/
   tone, compliance requirements (every brokerage has its own — don't assume
   one brokerage's rules apply to another), and current live domain. If the
   agent has the Brand Brain Builder skill, offer to build their Brand Brain
   first.

2. **Work on a copy of the template, never the original.** Copy
   `assets/template.html` to a new file named for the agent (e.g.
   `smith-realty-newsletter.html`) and build in that copy, so the original
   stays a clean starting point. When the first month is done, deliver the
   finished file and tell the agent to keep it: next month they can share it
   again (or paste their notes) and you update only the content.

3. **Fill in every `[BRACKETED TOKEN]`** in the duplicated `template.html`
   with the client's actual brand values (see the design-tokens comment at
   the top of the `<style>` block for the full list) and their first
   month's real content. Once real values are in, the brackets should be
   gone — a finished template has no literal `[TOKEN]` text left in it.

4. **Decide: header/footer in the template, or built in the client's ESP?**
   This template includes both by default. Some teams prefer to build them
   directly in Mailchimp instead — that's a preference, not a default to
   copy blindly. Ask which they want. If they want it removed, delete the two
   `<!-- ... (optional — delete if...) -->`-marked sections and note in the
   client's own SKILL.md what their ESP-built footer/header must legally
   include (see step 5).

5. **Compliance is brokerage- and state-specific — verify, don't assume.**
   At minimum, most US real estate newsletters need: the brokerage name (in
   whatever exact form that brokerage requires — some require spelling it
   out in full, never abbreviated), a Fair Housing / Equal Housing
   Opportunity statement, the office address, and an unsubscribe link. Some
   brokerages have additional rules about logo placement or how the
   brokerage name is written — ask whether theirs does, and note the answer
   for future months.

6. **Decide the video spotlight's position** (above the articles vs. below,
   just before the listings grid) — ask the client's preference rather than
   defaulting silently. It's the same block either way; see the placement
   comment near the top of `template.html`.

7. **Offer to save their setup as their own skill.** Once the first month
   is approved, offer to turn the finished template and their preferences
   (content sources, listing rules, compliance notes, and any corrections
   they made) into a personal newsletter skill so future months are
   one-step. Let its "gotchas" grow from their real corrections rather than
   hypotheticals.

## Hard-won gotchas — apply these to every newsletter

- **Never nest an HTML comment inside another HTML comment.** `-->` inside
  a comment closes it early, and everything after leaks out as visible
  text at the top of the live email. If you want to leave instructions
  inside `template.html`, keep each comment simple and never put example
  markup containing `<!--` or `-->` inside another comment's body — put
  that kind of guidance in the SKILL.md instead.
- **Prefer system fonts for headlines when a client cares about consistent
  rendering.** A Google Fonts `@import` (or any web font) gets silently
  dropped by a meaningful share of email clients (Outlook desktop
  especially), so the client ends up seeing their "real" headline font far
  less often than they think. A well-chosen system font (Times New Roman,
  Georgia, Arial) renders identically everywhere. This isn't a hard rule —
  some clients will prefer the brand-accurate look even knowing it won't
  always render — but raise the tradeoff explicitly rather than picking
  silently.
- **One lead accent color, one minor/hairline-only accent color.** Almost
  every real estate brand palette reviewed so far works this
  way: black/white or a similar neutral pair as the dominant base, one
  confident accent color carrying CTAs and brand-weight moments, and at
  most one more color used sparingly for tiny details only. Resist the
  urge to give a secondary brand color equal visual weight even if the
  client's logo uses it — ask which one is meant to lead.
- **Always label listing status** (For Sale / Pending / For Rent, etc.) on
  every listing card. Never present a Pending or off-market listing as if
  it were available without a visible tag — it's a small design detail with
  real accuracy implications.
- **Confirm domain-migration status before building links**, every time —
  don't assume a "we're moving to X domain" note from a prior conversation
  is still accurate; re-confirm, especially since a site mid-migration can
  return inconsistent 404s on some pages before others.
- **Article/listing images and video thumbnails can't be fetched or hosted
  by Claude.** Every image in the template stays a `[TOKEN]` placeholder
  until the client supplies an already-hosted URL (their ESP's asset
  library — Content Studio in Mailchimp, etc.). Don't try to hot-link
  images from the client's own website; those URLs usually aren't stable or
  even directly accessible.
- **When testing a design change the client hasn't confirmed yet** (a font
  swap, reordering a section, an all-caps treatment), save it as a
  separate preview file rather than overwriting their working template.
  Only fold it into the main file once they explicitly confirm they want
  it kept.
