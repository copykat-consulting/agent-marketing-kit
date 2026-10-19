---
name: "real-estate-newsletter-setup"
description: Builds a real estate agent's monthly email newsletter as a self-contained HTML file ready to paste into Mailchimp, Constant Contact or another email platform, with a hero, video spotlight, article features and a listings grid in the agent's brand. Use when an agent asks to set up, build or update their monthly newsletter, email newsletter or Mailchimp email.
---

# Real Estate Newsletter (Generic Template)

This is the reusable base for a monthly real estate email newsletter. It
produces one table-based HTML file with, in order:

1. A light header with the agent's logo (tight spacing, no dark band)
2. A hero: centered month label and headline, then a short **left-aligned**
   personal note signed with the agent's first name
3. An optional video spotlight on the lead accent color
4. Up to four article features, each with an image, category label, title,
   teaser and button:
   - Market update (swapped every month)
   - This month's blog post (lifestyle, seller or buyer piece)
   - An expertise tip list written right in the email (the agent's niche:
     horse property, first-home steps, downsizing, etc.)
   - A relationship piece (vendor list, client event, seasonal home checklist)
5. A four-listing grid with status tags
6. A closing invitation panel using the agent's standard CTA
7. An optional compliance footer, and the required ESP bar (copyright,
   mailing address, preferences, unsubscribe) built on Mailchimp merge tags

The "Design defaults" and "Hard-won gotchas" sections below come from real
client revisions. Read both before building.

## First-time setup for an agent

In this skill, "the client" means the agent or team whose newsletter you're
building (often the person you're talking to).

1. **Get or build a brand reference doc first.** If the client has a "Brand
   Brain" project doc (or similar), read it in full. If not, ask for (or help
   them establish): color palette (which color leads and which are
   accent-only), voice/tone, words to avoid, standard CTA and contact
   method, compliance requirements (every brokerage has its own), current
   live domain, and hosted logo links. If the agent has the Brand Brain
   Builder skill, offer to build their Brand Brain first.

2. **Work on a copy of the template, never the original.** Copy
   `assets/template.html` to a new file named for the agent (e.g.
   `smith-realty-newsletter.html`) and build in that copy. When the first
   month is done, deliver the finished file and tell the agent to keep it;
   next month they can share it again and you update only the content.

3. **Gather the month's content before filling the template.** Look for the
   month's market report, blog post(s), video and listings in the project
   docs, attachments or conversation. If a blog post the agent mentions
   isn't available, ask them to paste it rather than guessing at its
   content. Use the post's own title and image; write a fresh two- or
   three-sentence teaser in the agent's voice.

4. **Fill in every `[BRACKETED TOKEN]`** with real brand values (see the
   design-tokens comment at the top of the `<style>` block) and real
   content. Delete any section with no content this month (video, listings,
   an article) rather than leaving placeholders. Before delivering, list any
   tokens still unfilled (usually links the agent will send later) so they
   know exactly what to add.

5. **Header, footer and compliance: ask, and default to the ESP.** Many
   agents already have their license numbers, brokerage and Equal Housing
   logo in their Mailchimp footer. Ask whether theirs does.
   - If yes, delete the optional compliance footer row and remind them the
     ESP footer must carry everything their brokerage requires.
   - If no, fill in the compliance footer with the exact wording the
     brokerage requires (some require the brokerage name spelled out in
     full, a specific Fair Housing line or an Equal Housing logo image).
   - Always keep the required ESP bar. Its merge tags (`*|CURRENT_YEAR|*`,
     `*|LIST:ADDRESSLINE|*`, `*|UPDATE_PROFILE|*`, `*|UNSUB|*`) are
     Mailchimp's; swap them for the equivalent tags if the client uses
     another platform.

6. **Decide the video spotlight's position.** Default is right after the
   hero, since many agents treat video as their lead format. Offer to move
   it lower, just before the listings, if they prefer.

7. **Offer to save their setup as their own skill.** Once the first month
   is approved, offer to turn the finished file and their preferences
   (content sources, listing rules, compliance notes, corrections they
   made) into a personal newsletter skill so future months are one step.

## Design defaults (apply unless the client asks otherwise)

- **One background color for everything.** The email and the page behind it
  share the same light background. Don't frame the email in a darker outer
  color; clients have found it heavy and asked for it removed.
- **System serif font throughout.** Use Times New Roman (with Times and
  Georgia as fallbacks) for headlines and body. Brand fonts, even Google
  Fonts, are silently dropped by Outlook desktop and other inboxes, and
  clients notice the inconsistency. Only add a web font `@import` if the
  client explicitly accepts that some recipients won't see it. Don't use
  light (300) font weights with Times; they render too thin.
- **Centered layout, left-aligned letter.** Headlines, labels, teasers,
  buttons, tip lists and listing details are centered. The opening personal
  note and sign-off are left-aligned so they read like a letter.
- **Tight header.** Keep the logo close to the top edge with minimal
  padding above and below. Put the logo on the light background (charcoal
  logo on ivory, etc.), not on a dark band.
- **Mailto links for reply-style CTAs.** For "ask me," "request a vendor"
  or "private showing" buttons, use `mailto:` with a URL-encoded subject
  line so replies arrive sorted. Use the agent's booking or contact page
  for the primary CTA if they have one.
- **Calm copy.** Teasers stay two or three short sentences. CTAs are
  invitations ("Request a private consultation"), never urgent.

## Hard-won gotchas: apply these to every newsletter

- **Logos and images must be hosted, public URLs.** An email can only show
  an image that loads from a public link. If no hosted logo exists, the
  logo will be blank; ask the client to upload it (Mailchimp Content
  Studio, ImageKit, etc.) and send the link. Don't hot-link images from
  the client's website; those URLs often aren't stable. Never use a
  lifestyle library image to represent a specific listing.
- **Never nest an HTML comment inside another HTML comment.** `-->` inside
  a comment closes it early, and everything after leaks out as visible
  text at the top of the live email. Keep each comment simple.
- **One lead accent color, one minor/hairline-only accent color.** Most real
  estate palettes work this way: a light neutral base, one confident
  accent carrying buttons and feature blocks, and at most one more color
  for tiny details. Ask which color leads if it isn't clear.
- **Always label listing status** (For Sale / Pending / For Rent) on every
  listing card. Never present a Pending or off-market listing as
  available.
- **Confirm domain-migration status before building links**, every time;
  a site mid-migration can return 404s on some pages before others.
- **Follow the client's voice rules strictly.** Check the finished file for
  banned words and punctuation from their brand doc (many agents ban em
  dashes, for example) before delivering.
- **Preview changes the client hasn't confirmed yet** (a font swap, a
  section reorder) as a separate preview file rather than overwriting their
  working file. Fold it in once they confirm.

## Subject lines and preview text

See `references/subject-lines-and-preview-text.md`. Offer 3-5 subject lines
under ~45 characters, plus preview text that teases 2-3 concrete things
inside the issue and doesn't repeat the opening sentence.

## If there's a Marketing Command Center

Whenever this skill runs, on its own or from the monthly guide, mark it on the agent's dashboard: set the month's monthly newsletter item to Ready for review with a note saying where the file is saved (and its link, if it's live or published). Publish a review page for it and put that link on the item, following the monthly guide's "Review pages" steps (`../monthly-marketing/references/checklist-map.md`), so the agent can click straight into it from the dashboard. Read the item first, write pinned to its version, and leave it alone if it's already Approved, Scheduled or Published. Save the file to the Project too, so the other monthly pieces can build on it.
