"""Adds the Social plan tab to a Marketing Command Center page.

Usage: python3 add_social_tab.py <page.html>   (edits the file in place)

Safe to run on the template or on an agent's existing dashboard: it only
inserts new pieces at fixed anchors, and refuses to run twice.
"""
import sys

CSS = r"""
/* social plan */
.tabs{flex-wrap:wrap;row-gap:2px}
.sp-top{padding:16px 18px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between}
.sp-sum{margin:6px 0 0;color:var(--muted);font-size:13.5px}
.sp-todo{padding:14px 18px}
.sp-todo h3{margin:0 0 6px;font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.sp-todo ul{margin:0;padding-left:18px;display:grid;gap:4px;font-size:14px}
#social{display:grid;gap:18px;min-width:0}
#social>*{min-width:0}
.sp-cal-wrap{overflow-x:auto;padding:6px;min-width:0;max-width:100%}
.sp-cal{display:grid;grid-template-columns:repeat(7,minmax(110px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);min-width:780px}
.sp-dow{background:var(--bg);padding:6px 8px;font-size:10.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.sp-day{background:var(--panel);min-height:92px;padding:6px;display:flex;flex-direction:column;gap:4px;min-width:0}
.sp-day.out{background:var(--bg)}
.sp-dn{font-size:12px;color:var(--muted)}
.sp-chip{display:block;font-size:11.5px;line-height:1.3;padding:3px 6px;text-decoration:none;color:var(--ink);background:color-mix(in srgb,var(--c) 12%,var(--panel));border-left:3px solid var(--c);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.sp-chip:hover{background:color-mix(in srgb,var(--c) 22%,var(--panel))}
.sp-list{display:grid;gap:14px;padding:6px}
.sp-post{padding:16px 18px;display:grid;gap:10px;border-top:4px solid var(--c)}
.sp-head{display:flex;flex-wrap:wrap;align-items:center;gap:6px 12px}
.sp-head h3{margin:0;flex:1 1 220px;font-family:var(--f-display);font-weight:var(--hw,650);font-size:18px;line-height:1.2}
.sp-n{font-family:var(--f-num);font-style:italic;font-size:24px;line-height:1}
.sp-head .tag{--n:var(--c)}
.sp-head .pill{width:auto;padding:5px 10px}
.sp-meta{font-size:13px;color:var(--muted)}
.sp-onimg{font-size:13.5px;background:var(--bg);border:1px solid var(--line);padding:8px 12px}
.sp-onimg a{color:var(--accent);font-weight:700;margin-left:6px}
.sp-post details summary{cursor:pointer;font-size:13px;font-weight:700;color:var(--muted)}
.sp-post details[open] summary{margin-bottom:8px}
.sp-slides{margin:0;padding-left:20px;display:grid;gap:4px;font-size:14px}
.sp-pre{margin:0;white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.6 var(--f-body);background:var(--bg);border:1px solid var(--line);padding:12px 14px;max-height:420px;overflow:auto}
.sp-cap{display:grid;gap:6px}
.sp-cap-h{display:flex;justify-content:space-between;align-items:center;gap:10px}
.sp-cap-h b{font-size:13px}
.sp-cap-acts{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.sp-ta{font:14px/1.6 var(--f-body);color:var(--ink);background:var(--panel);border:1px solid var(--line-strong);padding:12px 14px;width:100%;box-sizing:border-box;resize:vertical;min-height:220px}
.sp-acts{display:flex;flex-wrap:wrap;gap:8px}
.sp-edited{font-size:12.5px;color:var(--muted)}
"""

TAB = '\n    <button class="tab" role="tab" id="tab-social" data-page="social" aria-selected="false">Social plan</button>'

SECTION = """
  <section id="page-social" hidden style="gap:18px">
    <div class="sec-h"><h2>Social plan</h2><span>This month's posts, captions and video scripts in one place.</span></div>
    <div id="social"></div>
  </section>
"""

JS = r"""
  /* ---------- social plan ---------- */
  S.social = null; S.socialLoaded = false; S.socialFilter = "All"; let unsubSocial = null;
  S.spEdits = {}; S.spEdit = null; S.spMsg = ""; let unsubSpEdits = null;
  const spIdle = () => S.page === "social" && S.spEdit == null;
  const spPlural = (k, v) => { const b = k === "Google Business" ? "Google Business post" : k; return (v === 1 ? b : b.replace(/s?$/, "s")).replace(/^(?!Google)./, (c) => c.toLowerCase()); };
  const SP_FORMATS = { "Feed post": "--c-social", "Carousel": "--c-mail", "Market graphic": "--c-email", "Video": "--c-video", "Reel": "--c-blog", "B-roll": "--c-gbp", "Google Business": "--c-gbp" };
  function subscribeSocial() {
    unsubSocial?.(); unsubSpEdits?.(); S.social = null; S.socialLoaded = false; S.spEdits = {}; S.spEdit = null; S.spMsg = "";
    if (!S.db) { if (S.page === "social") renderSocial(); return; }
    const want = S.ym;
    unsubSpEdits = S.db.collection("social/" + want + "/edits").onSnapshot((snap) => {
      if (want !== S.ym) return;
      S.spEdits = {}; snap.docs.forEach((d) => { S.spEdits[d.id] = d.data(); });
      if (spIdle()) renderSocial();
    }, () => {});
    unsubSocial = S.db.doc("social/" + want).onSnapshot((snap) => {
      if (want !== S.ym) return;
      S.social = snap.exists ? snap.data() : null; S.socialLoaded = true;
      if (spIdle()) renderSocial();
    }, () => { S.socialLoaded = true; if (S.page === "social") renderSocial(); });
  }
  function renderSocial() {
    const el = $("social"); if (!el) return;
    const { y, m } = parseYM(S.ym), label = MONTHS[m] + " " + y;
    if (!S.db) { el.innerHTML = S.dbChecked ? `<div class="card empty"><h3>Social plan unavailable here</h3><p>Open this page in Claude while signed in.</p></div>` : ""; return; }
    if (!S.socialLoaded) { el.innerHTML = `<div class="card empty"><div class="skel" style="width:60%"></div><div class="skel" style="width:40%"></div></div>`; return; }
    const sp = S.social;
    if (!sp || !Array.isArray(sp.posts) || !sp.posts.length) {
      el.innerHTML = `<div class="card empty"><h3>No social plan for ${esc(label)} yet</h3><p>Once this month's blogs and newsletter are done, ask Claude in your project to build your social plan for ${esc(label)}. The calendar, captions and video scripts will show up here.</p></div>`;
      return;
    }
    const posts = sp.posts.slice().sort((a, b) => String(a.date).localeCompare(String(b.date)) || (N(a.n) - N(b.n)));
    const itemOf = (p) => p.item ? S.items.find((i) => i.key === p.item || i.id === p.item) : null;
    const counts = {}; posts.forEach((p) => { counts[p.format] = (counts[p.format] || 0) + 1; });
    const fc = (f) => `var(${SP_FORMATS[f] || "--c-other"})`;
    const ro = !S.canWrite || S.writeRefused;
    const editOf = (p) => { const e = S.spEdits[String(p.n)]; return e && typeof e.caption === "string" ? e : null; };
    const capOf = (p) => editOf(p)?.caption ?? p.caption;
    const capHTML = (p) => {
      const n = esc(p.n), ed = editOf(p);
      if (S.spEdit === String(p.n)) return `<div class="sp-cap"><label class="sp-cap-h" for="sp-edit-${n}"><b>Edit caption</b></label>
        <textarea class="sp-ta" id="sp-edit-${n}" rows="12">${esc(capOf(p))}</textarea>
        <div class="sp-acts"><button class="btn sm primary" type="button" data-sp-save="${n}">Save caption</button><button class="btn sm ghost" type="button" data-sp-cancel="1">Cancel</button></div>
        ${S.spMsg ? `<p class="msg">${esc(S.spMsg)}</p>` : ""}</div>`;
      const who = ed ? (ed.by && ed.by === S.me ? "you" : (ed.by && S.names?.[ed.by]) || "your team") : "";
      return `<div class="sp-cap"><div class="sp-cap-h"><b>Caption</b><span class="sp-cap-acts">
          ${ro ? "" : `<button class="btn sm" type="button" data-sp-edit="${n}">Edit</button>`}<button class="btn sm" type="button" data-sp-copy="${n}">Copy</button></span></div>
        <pre class="sp-pre" id="sp-cap-${n}">${esc(capOf(p))}</pre>
        ${ed ? `<div class="sp-edited">Edited by ${esc(who)}${ed.at ? " · " + esc(dayLabel(ed.at)) : ""}${ro ? "" : ` · <button class="lnk" type="button" data-sp-restore="${n}" style="border:0;background:none;color:var(--accent);font-weight:700;padding:0">Restore original</button>`}</div>` : ""}</div>`;
    };
    const design = safeUrl(sp.designUrl || "");
    const first = new Date(y, m, 1).getDay(), days = daysIn(S.ym), cells = Math.ceil((first + days) / 7) * 7;
    let cal = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].map((d) => `<div class="sp-dow">${d}</div>`).join("");
    for (let i = 0; i < cells; i++) {
      const d = i - first + 1;
      if (d < 1 || d > days) { cal += `<div class="sp-day out"></div>`; continue; }
      const iso = S.ym + "-" + String(d).padStart(2, "0");
      cal += `<div class="sp-day"><span class="sp-dn num">${d}</span>${posts.filter((p) => p.date === iso).map((p) =>
        `<a class="sp-chip" href="#sp-${esc(p.n)}" data-sp-jump="${esc(p.n)}" style="--c:${fc(p.format)}" title="${esc(p.format + ": " + p.title)}">${esc(p.n)} · ${esc(p.title)}</a>`).join("")}</div>`;
    }
    const f = S.socialFilter;
    const status = (p) => {
      const it = itemOf(p); if (!it) return "";
      if (it.qty > 1) return `<span class="pill num" data-s="${stateOf(it)}">${it.done || 0} of ${it.qty} live</span>`;
      const st = stateOf(it); return `<span class="pill" data-s="${st}">${STATUS[st]}</span>`;
    };
    const list = posts.filter((p) => f === "All" || p.format === f).map((p) => `
      <article class="card sp-post" id="sp-${esc(p.n)}" style="--c:${fc(p.format)}">
        <div class="sp-head"><span class="sp-n num">${esc(String(p.n).padStart(2, "0"))}</span><h3>${esc(p.title)}</h3><span class="tag">${esc(p.format)}</span>${status(p)}</div>
        <div class="sp-meta">${esc(dayLabel(p.date))}${p.time ? " · " + esc(p.time) : ""}${(p.networks || []).length ? " · " + esc(p.networks.join(", ")) : ""}${p.source ? " · From: " + esc(p.source) : ""}</div>
        ${p.onImage && (p.onImage.label || p.onImage.headline) ? `<div class="sp-onimg"><span class="muted">On the image:</span> ${esc([p.onImage.label, p.onImage.headline].filter(Boolean).join(" / "))}${design ? `<a href="${design}" target="_blank" rel="noopener">Open design</a>` : ""}</div>` : ""}
        ${(p.slides || []).length ? `<details><summary>Slides (${p.slides.length})</summary><ol class="sp-slides">${p.slides.map((s) => `<li>${esc(s)}</li>`).join("")}</ol></details>` : ""}
        ${p.script ? `<details open><summary>${/Google/.test(p.format) ? "Post text" : "Script and shot list"}</summary><pre class="sp-pre">${esc(p.script)}</pre></details>` : ""}
        ${p.caption ? capHTML(p) : ""}
      </article>`).join("");
    el.innerHTML = `
      <div class="card sp-top">
        <div><div class="eyebrow">${esc(label)}${sp.theme ? " · " + esc(sp.theme) : ""}</div><p class="sp-sum num">${posts.length} items · ${Object.entries(counts).map(([k, v]) => `${v} ${esc(spPlural(k, v))}`).join(" · ")}</p></div>
        ${design ? `<a class="btn primary" href="${design}" target="_blank" rel="noopener">Open post designs</a>` : ""}
      </div>
      ${(sp.todo || []).length ? `<div class="card sp-todo"><h3>Still to fill in</h3><ul>${sp.todo.map((t) => `<li>${esc(t)}</li>`).join("")}</ul></div>` : ""}
      <div class="sec-h"><h2>Posting calendar</h2><span>Tap a post to jump to its caption.</span></div>
      <div class="sp-cal-wrap"><div class="sp-cal">${cal}</div></div>
      <div class="sec-h"><h2>Every post</h2><span>Status comes from your checklist on This month.</span></div>
      <div class="filters">${["All", ...Object.keys(counts)].map((k) => `<button class="fchip" type="button" data-sp-filter="${esc(k)}" aria-pressed="${k === f}">${esc(k)}</button>`).join("")}</div>
      <div class="sp-list">${list}</div>
      ${(sp.sources || []).length ? `<p class="tip">Built from: ${sp.sources.map((s) => esc(s.title || s)).join(" · ")}</p>` : ""}`;
  }
  $("social").addEventListener("click", (e) => {
    const j = e.target.closest("[data-sp-jump]");
    if (j) {
      e.preventDefault();
      if (S.socialFilter !== "All") { S.socialFilter = "All"; renderSocial(); }
      $("sp-" + j.dataset.spJump)?.scrollIntoView({ block: "start" });
      return;
    }
    const fb = e.target.closest("[data-sp-filter]");
    if (fb) { S.socialFilter = fb.dataset.spFilter; renderSocial(); return; }
    const eb = e.target.closest("[data-sp-edit]");
    if (eb) { S.spEdit = eb.dataset.spEdit; S.spMsg = ""; renderSocial(); $("sp-edit-" + S.spEdit)?.focus(); return; }
    if (e.target.closest("[data-sp-cancel]")) { S.spEdit = null; S.spMsg = ""; renderSocial(); return; }
    const sb = e.target.closest("[data-sp-save]");
    if (sb) {
      const n = sb.dataset.spSave, val = $("sp-edit-" + n)?.value ?? "";
      sb.disabled = true;
      S.db.collection("social/" + S.ym + "/edits").doc(n).set({ caption: val, by: S.me || "", at: new Date().toISOString() })
        .then(() => { S.spEdit = null; S.spMsg = ""; renderSocial(); })
        .catch((err) => { if (err?.code === "invalid_argument") S.writeRefused = true; S.spMsg = err?.code === "invalid_argument" ? "You have view-only access, so captions can't be changed." : "That didn't save. Check your connection and try again."; sb.disabled = false; renderSocial(); });
      return;
    }
    const rb = e.target.closest("[data-sp-restore]");
    if (rb) { S.db.collection("social/" + S.ym + "/edits").doc(rb.dataset.spRestore).delete().catch(() => {}); return; }
    const cb = e.target.closest("[data-sp-copy]");
    if (cb) {
      const pre = $("sp-cap-" + cb.dataset.spCopy), text = pre?.textContent || "";
      const ok = () => { cb.textContent = "Copied"; setTimeout(() => { cb.textContent = "Copy"; }, 1600); };
      const sel = () => { try { const r = document.createRange(); r.selectNodeContents(pre); const s = getSelection(); s.removeAllRanges(); s.addRange(r); cb.textContent = "Selected"; } catch {} };
      try { navigator.clipboard.writeText(text).then(ok, sel); } catch { sel(); }
    }
  });
"""

EDITS = [
    # styles: new rules at the end of the main stylesheet
    ("\n</style>\n\n<canvas id=\"confetti\"", CSS + "</style>\n\n<canvas id=\"confetti\""),
    # tab button right after "This month"
    ('data-page="month" aria-selected="true">This month</button>',
     'data-page="month" aria-selected="true">This month</button>' + TAB),
    # page section right before Performance
    ('\n  <section id="page-performance"', SECTION + '\n  <section id="page-performance"'),
    # page switching knows about the new page
    ('["month", "performance", "ideas", "year"].forEach((x) => {',
     '["month", "social", "performance", "ideas", "year"].forEach((x) => {'),
    ('else if (p === "year") { renderYear(); loadMonthStats(); } else renderSnaps();',
     'else if (p === "year") { renderYear(); loadMonthStats(); } else if (p === "social") renderSocial(); else renderSnaps();'),
    ('if (["#performance", "#ideas", "#year"].includes(location.hash))',
     'if (["#social", "#performance", "#ideas", "#year"].includes(location.hash))'),
    # follow the month switcher and the checklist
    ('subscribeItems(); subscribeNext(); startWatches(); renderAll();',
     'subscribeItems(); subscribeNext(); subscribeSocial(); startWatches(); renderAll();'),
    ('S.itemsLoaded = true; renderProgress(); renderCards(); renderFlow(); resolveNames();',
     'S.itemsLoaded = true; renderProgress(); renderCards(); renderFlow(); resolveNames(); if (S.page === "social" && S.spEdit == null) renderSocial();'),
    ('subscribeItems(); subscribeNext(); subscribeIdeas();',
     'subscribeItems(); subscribeNext(); subscribeIdeas(); subscribeSocial();'),
    # the code itself, just before the month switcher logic
    ('  function setMonth(v) {', JS + '\n  function setMonth(v) {'),
]


def main(path):
    s = open(path, encoding="utf-8").read()
    if 'id="tab-social"' in s:
        sys.exit("Social plan tab is already on this page.")
    for old, new in EDITS:
        n = s.count(old)
        if n != 1:
            sys.exit(f"Expected one match, found {n}: {old[:60]!r}")
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)
    print("Social plan tab added to", path)


if __name__ == "__main__":
    main(sys.argv[1])
