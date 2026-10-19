---
name: market-report-postcard
description: Builds a real estate agent's monthly market report postcard, an 8.5 x 5.5 inch two-sided print-ready PDF with the month's headline stats, a community table, their headshot, branding, call to action and compliance, made from that month's market report blog. Use when an agent asks for their market postcard, direct mail postcard, just-sold or market update mailer, or "a postcard that goes with my market report."
---

# Market Report Postcard

A two-sided 8.5 × 5.5 inch postcard that goes with the agent's monthly market report blog and mails to their database. It's built from `assets/postcard.html` and rendered by `scripts/render_postcard.js` into:

- **A print-ready PDF:** two pages (front, back), 8.75 × 5.75 in, which is the 8.5 × 5.5 trim plus 0.125 in bleed on every side. Fonts are embedded and every word sits at least 0.25 in inside the trim.
- **PNG previews** of each side as it will look once trimmed, plus a guides preview showing the trim line, safe area, postage area and address block.

Talk to the agent in plain language. Don't mention file names, scripts or JSON.

## What it uses

Find each in this order: this chat, the Project's docs, then ask in one short round.

1. **This month's market report.** The blog post from the Market Report Blog skill, or the agent's stats. Every number on the card comes from it, exactly as written, with its source and month. Never round, estimate or add a number the report doesn't have.
2. **The Brand Brain:** voice, banned words and formatting rules (many agents ban em dashes), colors, fonts, standard call to action, contact details, and the compliance section.
3. **Files** (ask up front; hosted links usually can't be downloaded here):
   - a **headshot** (any photo of the agent works; you'll crop it to head and shoulders)
   - their **co-branded lockup** (their logo, a divider and the brokerage's logo) if the Brand Brain requires co-branding. It goes on both sides: a light version on the photo side and the original on the light side. If they only have a dark one, make the light copy by recoloring it (keep the artwork exactly; only change its color) and mention it, in case the brokerage requires its logo in its own colors.
   - Without a lockup: their **logo** (light and dark versions, made the same way) and the **brokerage's logo** as separate files. If the brokerage logo is missing, the card shows a red "Add brokerage logo" box. Never type out a logo as text.
   - a **front photo**: one of their own lifestyle or area photos, as large as they have. For print, 2,600 px wide or more is ideal; under about 1,600 px may look soft, so say so.
4. **Mailing details**, if known: return address, and whether their print shop or mail house adds postage and addresses. Leave the return address off if the agent doesn't give one.

## Build it

1. **Pick the story.** Use the blog's headline story. Write a front headline of six words or fewer (it can echo the blog's H1, shortened) and a one-line subhead naming the communities.
2. **Front stats:** three or four of the blog's headline numbers (its KPI bar is usually right), each with a short label of six words or fewer.
3. **Back table:** one row per community the blog covers, plus the region or county, up to seven rows. Columns: median sold price, change vs. last year, days on market. Mark each change `up`, `dn` or `fl` by the direction of the number.
4. **The note:** two or three sentences in the agent's voice, first person, interpreting the month (not listing numbers already in the table). Check it against the Brand Brain's banned words and formatting rules.
5. **Call to action:** their standard CTA as a calm invitation, with phone and email. If the blog is live, add its link as `qrUrl` so the card prints a QR code to the full report; until then leave it out and list it as a to-do.
6. **Compliance** from the Brand Brain, verbatim: agent and brokerage names with license numbers, "Equal Housing Opportunity" (the template draws the symbol; use the brokerage's official file instead if they provide one), and any "independently owned and operated" wording the brokerage requires. If the Brand Brain says the exact wording is still missing, flag it rather than inventing it.
7. **Fair housing:** describe the market and the places, never who should live there.

## Render it

1. Prepare the images: crop the headshot to a square around the face and shoulders (about 500 px or more), and make the dark logo if needed.
2. Install the fonts and QR library in a scratch folder: `npm i @fontsource/<serif-slug> @fontsource/<sans-slug> qrcode` (the Brand Brain's fonts, e.g. `bodoni-moda`, `montserrat`).
3. Write `data.json` (shape below) next to the images and run:
   ```
   NODE_PATH=$(npm root -g) node scripts/render_postcard.js data.json <out dir> <fonts dir>
   ```
4. **Look at all three previews.** The type is sized to read at arm's length; keep it that way. If something doesn't fit, shorten it (a shorter note, a shorter headline, short column labels) rather than shrinking the type. Check that nothing is clipped, the stat labels fit, the headshot is well cropped, the logos sit clear of the postage area, and the address block is empty. Fix and re-render before delivering.

### Data shape

```json
{
  "fileName": "Agent-Name-Market-Postcard-September-2026",
  "colors": {"bg": "#F3F0E9", "panel": "#D5C9B7", "accent": "#9A8D7E", "feature": "#4D5548", "ink": "#292C29", "on-dark": "#F3F0E9"},
  "fonts": {"serif": "Bodoni Moda", "sans": "Montserrat"},
  "frontPhoto": "front.jpg", "lockupOnDark": "lockup-white.png", "lockupOnLight": "lockup.png",
  "logoOnDark": "logo-white.png", "logoOnLight": "logo-dark.png",
  "brokerLogo": "brokerage.png",
  "brokerLogoMissing": "Add brokerage logo",
  "kicker": "Inland North County Market Update", "month": "September 2026",
  "headline": "Supply tightens. Prices firm.", "subhead": "What September looked like in …",
  "stats": [{"value": "+15%", "label": "Westlake median price"}],
  "source": "Source: <association>, <month year>, <property type>. Changes are year over year.",
  "headshot": "headshot.jpg", "headshotPosition": "50% 50%",
  "agentName": "…", "agentRole": "<business name>",
  "note": "…",
  "columns": ["Community", "Median price", "Change", "Days to sell"],
  "rows": [{"name": "Westlake", "median": "$982,000", "change": "+15%", "dir": "up", "dom": "58"}],
  "tableSource": "…",
  "ctaHead": "…", "ctaLine": "…", "contactLine": "(760) 420-4415  ·  name@email.com",
  "qrUrl": "https://… (optional)",
  "compliance": ["Agent | DRE: …", "Brokerage | DRE: …", "Equal Housing Opportunity"],
  "returnAddress": ["Agent name", "Street", "City, ST ZIP"]
}
```

With a lockup, use `lockupOnDark` and `lockupOnLight` and leave out the separate logo fields. Otherwise use `logoOnDark`/`logoOnLight` plus one of `brokerLogo` or `brokerLogoMissing`. Leave out what doesn't apply (no `brokerLogo` for an agent without co-branding, no `returnAddress` if none is given).

## Deliver

- Send the PDF and the front and back previews to the agent. If their computer is linked, also save them in their month folder.
- Tell them: it's print-ready at 8.5 × 5.5 with bleed; their print shop or mail house adds postage and addresses in the blank area on the back; and what's still to do (brokerage logo, QR link once the blog is live, return address, broker sign-off on compliance wording).
- 8.5 × 5.5 is larger than USPS's postcard size, so it usually mails at letter or flat rates. Suggest they confirm postage with their mail house; don't quote prices.
- If they want to tweak the layout by hand, offer to rebuild the card on a Claude Design canvas from the same content.

## If there's a Marketing Command Center

Set the month's postcard item (titled "Market report postcard" or "Direct mail postcard") to Ready for review with a note of where the PDF is. Publish a review page for it and put that link on the item, following the monthly guide's "Review pages" steps (`../monthly-marketing/references/checklist-map.md`), so the agent can click straight into it from the dashboard. Follow the Command Center's data rules: read the item first, write pinned to its version, and leave it alone if it's already Approved, Scheduled or Published.
