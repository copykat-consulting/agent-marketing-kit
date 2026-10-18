# Getting the posts into Metricool (Step 8)

Metricool can't read Claude artifacts: the design canvas and the dashboard
are private. Every image has to sit somewhere Metricool can fetch it. The
route that works for agents with no technical setup is: Claude renders the
designs to image files, the agent drops them into Google Drive, Metricool
pulls them from Drive. Claude then loads every post as a draft.

## 1. Render the designs to images (Claude does this)

1. Read the Design artifact's published `project/*.dc.html` artboards with
   the artifact read tool (`paths`, saved to a scratch folder), and list its
   assets (`scope: "assets"`) to get each image's blob id and sha256. Save
   those as `assets.json`: `{"<blob id>": "<sha256>"}`.
2. The images inside the canvas are the photo and logo files uploaded in
   Step 5. The blob files themselves can't be downloaded, so use the
   originals: the files the agent attached, or the resized copies you made
   before uploading. The script matches each blob to a local file by sha256,
   so use the exact files you uploaded.
3. The workspace usually can't reach Google Fonts. Install the canvas's font
   families from npm into a scratch folder:
   `npm i @fontsource/<family-slug>` (e.g. `@fontsource/bodoni-moda`,
   `@fontsource/montserrat`).
4. Run:
   ```
   NODE_PATH=$(npm root -g) node scripts/render_designs.js <project dir> <images dir> <assets.json> <out dir> <fonts dir>
   ```
   It writes one 1080 × 1350 JPG per artboard, named by post number:
   `Post-07.jpg`, and for carousels `Post-15-1.jpg`, `Post-15-2.jpg`, …
   in slide order. It warns about any image or font it couldn't match; fix
   those before going on.
5. Make a contact sheet and look at it. Check that text, logo and photos
   all came through and nothing is clipped.

## 2. Give the agent the files

- **Computer linked:** write the images into their folder (for example
  `Claude/<agent>-social-<month>/<Agent> <Month> Posts`) and say exactly
  where it is.
- **Not linked:** zip the images and send the zip in the chat.

Don't upload the images through the Google Drive connector. It only takes
file content passed inline, which is far too large for a month of images.

## 3. What the agent does (two steps, tell them plainly)

1. **Drag the folder into Google Drive** (drive.google.com, or the Google
   Drive folder in Finder or File Explorer if they use the Drive app).
2. **Link Google Drive in Metricool**, under their Metricool account's
   connections. This lets Metricool pull images from Drive links. It's a
   one-time setup.

If they'd rather use Dropbox, the same steps work with a Dropbox folder;
Metricool pulls from Dropbox links too.

## 4. Load the drafts (Claude does this)

1. Find the images with the Google Drive connector: search for the folder by
   title, then list the files in it (`parentId = '<folder id>'`). Use each
   file's Drive link as its media URL. Match files to posts by name
   (`Post-07.jpg` is Post 7; `Post-15-1.jpg`… are Post 15's slides in order).
2. `getBrandSettings`, then pick the brand whose label matches the agent. If
   none matches, list the labels and ask. Use a different brand only if the
   agent explicitly says it's a test or demo account, and confirm its name
   back to them first.
3. Read the month's caption edits (`references/dashboard.md`, "Caption
   edits") and use each edited caption instead of the original.
4. **Load one post first.** Check that it shows up as a draft with its image
   (`getScheduledPosts` for that day), and give the agent its planner link.
   Then load the rest.
5. For each post, call `createScheduledPost` with:
   - `draft: true` and `autoPublish: false`, every time
   - `publicationDate` from the plan's date and time, in the brand's
     `timezone` from `getBrandSettings`
   - `text`: the final caption
   - `media`: the post's image, or every slide in order for a carousel
   - `providers` for the networks on the plan that the brand has connected
     (`networksData` in the brand settings), each with its network data
     (`instagramData: {type: "POST"}`, `facebookData: {type: "POST"}`)
6. **Google Business posts** go as `gmb` with `gmbData: {type: "publication"}`
   and the post's text (up to 1,500 characters, no hashtags). They don't need
   an image.
7. **Skip what can't be loaded yet:** reels and talking videos need the
   finished video file (Instagram rejects posts without media). List them
   with their dates so the agent can add them in Metricool once filmed.
8. Dates in the past are rejected. If a post's date has passed, ask whether
   to move it or skip it.

## 5. Report back

Tell the agent what loaded, with the planner links, what was skipped and
why, and that everything is a draft: nothing posts until they open each
draft in Metricool and schedule it. Set the dashboard items to `scheduled`
only if they ask.
