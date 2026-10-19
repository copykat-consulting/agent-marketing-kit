---
name: market-report-blog
description: Writes a real estate agent's monthly market report blog post as a branded, self-contained HTML file ready to paste into their website (Luxury Presence, Squarespace, WordPress and similar), using that month's local REALTOR association or MLS statistics. Use when an agent asks for their monthly market report, market update, market stats blog, or shares a new monthly stats PDF or numbers to turn into a post.
---

# Monthly Market Report Blog

Produces a publish-ready blog post that reports the month's housing statistics for the agent's market: a headline stat bar, a big-picture table, one section per sub-market (city, town or neighborhood) with buyer and seller takeaways, a closing takeaway and a home-valuation call to action. Built from `assets/template.html`.

**Read `assets/template.html` in full before building.** Its CSS classes and structure stay as they are; only the brand variables, placeholders and repeated sub-market blocks change.

## First time for this agent: collect their market profile

Ask only for what you don't already have (check the conversation, their Brand Brain if they have one, and any earlier post they share):

1. **Team or agent name**, brokerage name as it must be written, phone, website, and the page the button should link to (contact or home valuation page).
2. **Coverage area** (region name) and the **sub-markets** to report on, for example 3–5 cities or neighborhoods.
3. **Data source**: which REALTOR association or MLS publishes their monthly stats, and where (a public stats page, a PDF they receive, or numbers they'll paste).
4. **Brand**: main accent color, dark color, headline and body fonts (Google Fonts work best), and voice (e.g. warm and conversational, polished and luxury).
5. **Website platform** (Luxury Presence, Squarespace, WordPress, other), so you can give the right paste instructions.
6. **Photos**: whether they have hosted photo URLs for the region and each sub-market. If not, the photo boxes are removed rather than left as placeholders.

At the end of the first post, offer to save this profile (as a note or their own copy of this skill) so future months only need the new numbers.

## Each month

1. **Get the numbers.** Use the stats the agent pastes or uploads. Otherwise fetch the latest monthly release from their data source. For the region and each sub-market, collect for this month and the same month last year: closed sales, new listings, median sold price, median days on market, and months' supply or inventory if published. **Never invent, estimate or carry over a figure.** If a number isn't in the source, leave that row out and say so.
2. **Compute changes.** Year-over-year change as a percentage for counts and prices (rounded to whole percent), and as a plus or minus number of days for days on market. Mark each change cell `up`, `dn` or `fl` (flat when within about ±1%). Remember that rising days on market or inventory is a "down" signal for sellers. Keep colors honest to the direction of the number, and explain the meaning in the copy.
3. **Find the storyline.** Look across sub-markets for what's notably different: a standout gainer, a cooling area, an inventory squeeze, a price shift. This drives the stat bar, the pull quote, each sub-market's tag (e.g. "Strong Momentum", "Cooling Off", "Buyer Opportunity") and the headline.
4. **Write a unique headline.** The website's blog post already has its own title field (e.g. "[Area] Market Update — [Month Year]"). The in-page `<h1>` must say something different so the page doesn't duplicate its own title. Formula: **[Area] + [this month's specific trend] + [Month Year]**, e.g. "Sacramento Prices Hold Steady as Inventory Climbs — October 2026".
5. **Fill in the template.** Copy `assets/template.html` and:
   - Set the brand variables (accent, dark color) and swap the Google Fonts link and font names if the agent uses different fonts.
   - Replace every `[BRACKETED]` placeholder. A finished file has no brackets left.
   - Repeat the sub-market block once per sub-market, in the agent's preferred order.
   - Write 2–3 sentences per sub-market that interpret what moved and why it matters, grounded in the actual figures. Add "For buyers" and, where useful, "For sellers" callouts for the sub-markets with the most notable movement.
   - Close with "Our Takeaway": 3–4 sentences on the throughline and what a buyer or seller should actually do.
   - Cite the exact report name and publish date in the source line.
   - Insert photos only as real hosted URLs inside the existing image boxes (`<img src="…" alt="descriptive alt text">`). Otherwise delete the image boxes.
6. **Deliver** one HTML file named like `<Agent>_Market_Report_<Month><Year>.html`, with short paste instructions for their platform (custom HTML or code block). Don't paste the HTML into the chat.

## Voice and compliance

- Write in the agent's voice (first-person plural "we/our" by default). Interpret the numbers, don't just restate them. Avoid hype and hard-sell clichés.
- **Fair housing:** describe markets by data, amenities and housing stock, never by who lives there. Don't characterize neighborhoods by race, religion, national origin, family status, disability or similar, and avoid steering language ("perfect for young families", "exclusive area").
- Include the brokerage name exactly as required. Don't give legal, tax or financial advice. Keep forward-looking statements soft ("may", "could").

## Hard-won layout lessons (keep these)

- **All CSS stays scoped under `.mr`.** Website themes otherwise restyle or get restyled by the post. Any new CSS must start with `.mr`.
- **The CTA button stays inside `.cta-btn-wrap`** (flex with `!important`). Website builders frequently override plain centering and margins on buttons.
- **Keep text generously sized** (body around 17px). Many readers are older homeowners; don't shrink text for density.
- **Tables stay 4 columns** (Metric, last year, this year, change). On narrow content areas, don't add extra columns; split into another table instead.
- **No price-range breakdowns unless the agent supplies that data** (e.g. from an MLS analytics tool). Free association reports usually don't include it, and guessed bands are not acceptable.

## If there's a Marketing Command Center

Whenever this skill runs, on its own or from the monthly guide, mark it on the agent's dashboard: set the month's market report blog item to Ready for review with a note saying where the file is saved (and its link, if it's live or published). Read the item first, write pinned to its version, and leave it alone if it's already Approved, Scheduled or Published. Save the file to the Project too, so the other monthly pieces can build on it.
