#!/usr/bin/env python3
"""Collapses a month's social items into ONE card in the review queue.

Before: every social checklist item (feed posts, carousels, reels, videos, Google
Business posts...) showed as its own card in the review queue, all linking to the
same Social plan page.
After: items whose link points to the Social plan tab (a link ending in "#social")
are grouped per month into one "Social media plan" card that lists what's inside,
opens the Social plan tab, and approves, sends back or resubmits them all at once.
Everything else in the queue is unchanged. The checklist itself still lists each item.

Usage:  python3 upgrade_social_review.py <dashboard.html>
Needs the Social plan tab (add_social_tab.py). Does nothing if already applied.
"""
import sys

MARK = "/* social-review v1 */"

PATCHES = [
    # 1. Split social items out of the two lanes and group them by month.
    (
        """    const rev = pool.filter((i) => i.status === "review" && !isDone(i));
    const back = pool.filter((i) => i.status === "changes" && !isDone(i));""",
        """    """ + MARK + """
    const isSoc = (i) => /#social$/.test(String(i.link || ""));
    const groupSoc = (list) => { const g = {}; list.filter(isSoc).forEach((i) => { (g[i._ym] = g[i._ym] || []).push(i); }); return Object.keys(g).sort().map((ym) => ({ ym, items: g[ym] })); };
    const revAll = pool.filter((i) => i.status === "review" && !isDone(i));
    const backAll = pool.filter((i) => i.status === "changes" && !isDone(i));
    const rev = revAll.filter((i) => !isSoc(i)), back = backAll.filter((i) => !isSoc(i));
    const revG = groupSoc(revAll), backG = groupSoc(backAll);""",
    ),
    # 2. The grouped card.
    (
        """    const teamBar = S.teamEdit && !ro""",
        """    const gcard = (g, lane) => {
      const ids = g.items.map((i) => i.id).join(","), Y = `data-ym="${esc(g.ym)}"`, I = `data-ids="${esc(ids)}"`, rq = S.reqFor === "social|" + g.ym;
      const notes = g.items.map(last).filter(Boolean).sort((a, b) => String(a.at || "").localeCompare(String(b.at || ""))), l = notes.length ? notes[notes.length - 1] : null;
      return `<div class="rv"><div class="rv-top"><b>Social media plan</b><span>${esc(MONTHS[parseYM(g.ym).m])} · ${g.items.length} ${g.items.length === 1 ? "piece" : "pieces"}</span></div>
        <div class="last">${esc(g.items.map((i) => i.title).join(" · "))}</div>
        ${l ? `<div class="last">${esc(nameOf(l.by))}: ${esc(l.text)}</div>` : ""}
        <div class="acts"><button class="btn sm" type="button" data-act="open-social" ${Y}>Open the social plan</button>
          ${ro ? "" : lane === "rev"
            ? (rq ? "" : `<button class="btn sm ok" type="button" data-act="approve-group" ${I} ${Y}>Approve all</button><button class="btn sm" type="button" data-act="req-group" ${Y}>Request changes</button>`)
            : `<button class="btn sm" type="button" data-act="resubmit-group" ${I} ${Y}>Mark ready for review</button>`}</div>
        ${rq ? `<textarea id="rq-note" rows="2" maxlength="1000" placeholder="What should change? Name the post numbers if it's specific ones."></textarea><div class="acts"><button class="btn sm primary" type="button" data-act="sendback-group" ${I} ${Y}>Send back</button><button class="btn sm ghost" type="button" data-act="req-cancel">Cancel</button></div>` : ""}</div>`;
    };
    const teamBar = S.teamEdit && !ro""",
    ),
    # 3. Lanes: grouped cards first, counts are cards.
    (
        """<span class="n num">${rev.length}</span><h3>Ready for review</h3></div>
          ${rev.length ? rev.map((i) => card(i, "rev")).join("") :""",
        """<span class="n num">${rev.length + revG.length}</span><h3>Ready for review</h3></div>
          ${rev.length + revG.length ? revG.map((g) => gcard(g, "rev")).join("") + rev.map((i) => card(i, "rev")).join("") :""",
    ),
    (
        """<span class="n num">${back.length}</span><h3>Sent back for changes</h3></div>
          ${back.length ? back.map((i) => card(i, "back")).join("") :""",
        """<span class="n num">${back.length + backG.length}</span><h3>Sent back for changes</h3></div>
          ${back.length + backG.length ? backG.map((g) => gcard(g, "back")).join("") + back.map((i) => card(i, "back")).join("") :""",
    ),
    # 4. Buttons.
    (
        """    if (act === "approve") { addToThread(id, "approved", "Approved", "approved", b.dataset.ym); return; }""",
        """    if (act === "open-social") { if (b.dataset.ym && b.dataset.ym !== S.ym) setMonth(b.dataset.ym); setPage("social"); window.scrollTo?.(0, 0); return; }
    if (act === "approve-group") { (b.dataset.ids || "").split(",").filter(Boolean).forEach((x) => addToThread(x, "approved", "Approved", "approved", b.dataset.ym)); return; }
    if (act === "req-group") { S.reqFor = "social|" + b.dataset.ym; renderFlow(); return; }
    if (act === "sendback-group") { const t = ($("rq-note")?.value || "").trim() || "Please revise."; S.reqFor = null; (b.dataset.ids || "").split(",").filter(Boolean).forEach((x) => addToThread(x, "changes", t, "changes", b.dataset.ym)); return; }
    if (act === "resubmit-group") { const ymv = b.dataset.ym; (b.dataset.ids || "").split(",").filter(Boolean).forEach((x) => write(() => S.db.collection("months/" + ymv + "/items").doc(x).update({ status: "review" }))); return; }
    if (act === "approve") { addToThread(id, "approved", "Approved", "approved", b.dataset.ym); return; }""",
    ),
]


def main(path):
    s = open(path, encoding="utf-8").read()
    if MARK in s:
        print("Already upgraded:", path)
        return
    if 'id="tab-social"' not in s:
        sys.exit("Add the Social plan tab first (add_social_tab.py).")
    for old, new in PATCHES:
        n = s.count(old)
        if n != 1:
            sys.exit(f"Expected one match, found {n}: {old[:80]!r}")
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)
    print("Social items now review as one card:", path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
