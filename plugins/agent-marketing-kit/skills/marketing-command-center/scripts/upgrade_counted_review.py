#!/usr/bin/env python3
"""Lets counted checklist items (quantity above 1, e.g. 12 feed posts) go through review.

Before: a counted item only had a live counter ("3 of 12"), never "Ready for review"
or "Approved", and never appeared in the review queue.
After: a counted item has a status drop-down (Not started -> Drafting -> Ready for
review -> Needs changes -> Approved -> Scheduled) next to its live counter, it shows
in the review queue like any other item, and it reads "Published" once every piece
is live. The Social plan tab's status pill shows both, e.g. "Approved · 3/12 live".

Usage:  python3 upgrade_counted_review.py <dashboard.html>
Works on the template and on any dashboard built from it, including ones with
agent-specific colors and fonts. Does nothing if already applied.
"""
import sys

MARK = "/* counted-review v1 */"

PATCHES = [
    # 1. A counted item's state: Published once all are live, otherwise its review status.
    (
        'if (it.qty > 1) { const d = it.done || 0; return d <= 0 ? "todo" : d >= it.qty ? "done" : "doing"; }',
        'if (it.qty > 1) { ' + MARK + ' const d = it.done || 0; if (d >= it.qty) return "done"; '
        'if (["review", "changes", "approved", "scheduled"].includes(it.status)) return it.status; '
        'return d > 0 || it.status === "doing" ? "doing" : "todo"; }',
    ),
    # 2. Review queue includes counted items.
    ('const rev = pool.filter((i) => i.qty <= 1 && i.status === "review");',
     'const rev = pool.filter((i) => i.status === "review" && !isDone(i));'),
    ('const back = pool.filter((i) => i.qty <= 1 && i.status === "changes");',
     'const back = pool.filter((i) => i.status === "changes" && !isDone(i));'),
    # 3. Checklist row: status drop-down plus the live counter for counted items.
    (
        '''    const control = it.qty > 1
      ? `<span class="step num"''',
        '''    const statusSel = (opts) => `<select class="pill" data-s="${st}" data-status-id="${esc(it.id)}" ${ro ? "disabled" : ""} aria-label="Status for ${esc(it.title)}">${opts.map(([k, v]) => `<option value="${k}" ${k === st ? "selected" : ""}>${v}</option>`).join("")}</select>`;
    const control = it.qty > 1
      ? `<span class="cnt">${st === "done" ? `<span class="pill" data-s="done">Published</span>` : statusSel(Object.entries(STATUS).filter(([k]) => k !== "done"))}<span class="step num"''',
    ),
    (
        '''aria-label="One more done">+</button></span>`
      : `<select class="pill"''',
        '''aria-label="One more live">+</button></span></span>`
      : `<select class="pill"''',
    ),
    # 4. Moving the live counter keeps the review status.
    (
        'write(() => itemsCol().doc(id).update({ done: d, status: d >= it.qty ? "done" : d > 0 ? "doing" : "todo" }));',
        'write(() => itemsCol().doc(id).update({ done: d, status: d >= it.qty ? "done" : it.status === "done" ? "scheduled" : (it.status || "todo") }));',
    ),
    # 5. Editing a counted item's quantity keeps its review status.
    (
        'upd.status = upd.done >= data.qty ? "done" : upd.done > 0 ? "doing" : "todo"; }',
        'upd.status = upd.done >= data.qty ? "done" : it?.status && it.status !== "done" ? it.status : upd.done > 0 ? "doing" : "todo"; }',
    ),
    # 6. CSS for the status + counter pair.
    ('\n</style>\n\n<canvas id="confetti"',
     '\n.cnt{display:inline-flex;flex-direction:column;gap:6px;align-items:stretch}\n</style>\n\n<canvas id="confetti"'),
]

# Social plan tab pill (only on dashboards that have the tab).
SOCIAL = (
    'if (it.qty > 1) return `<span class="pill num" data-s="${stateOf(it)}">${it.done || 0} of ${it.qty} live</span>`;',
    'if (it.qty > 1) { const s2 = stateOf(it); return `<span class="pill num" style="width:auto;padding:6px 12px" data-s="${s2}">${s2 === "done" ? "Published" : esc(STATUS[s2]) + " · " + (it.done || 0) + "/" + it.qty + " live"}</span>`; }',
)


def main(path):
    s = open(path, encoding="utf-8").read()
    if MARK in s:
        if SOCIAL[0] in s:  # Social plan tab added after this upgrade ran
            open(path, "w", encoding="utf-8").write(s.replace(SOCIAL[0], SOCIAL[1]))
            print("Updated the Social plan status pill:", path)
        else:
            print("Already upgraded:", path)
        return
    for old, new in PATCHES:
        n = s.count(old)
        if n != 1:
            sys.exit(f"Expected one match, found {n}: {old[:80]!r}")
        s = s.replace(old, new)
    if 'id="tab-social"' in s:
        n = s.count(SOCIAL[0])
        if n != 1:
            sys.exit(f"Social plan tab found but its status pill didn't match ({n})")
        s = s.replace(SOCIAL[0], SOCIAL[1])
    open(path, "w", encoding="utf-8").write(s)
    print("Counted items can now go through review:", path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
