#!/usr/bin/env python3
"""Brings a dashboard built from an older template up to date, in the right order.

Usage:  python3 upgrade_dashboard.py <dashboard.html>
Runs add_social_tab.py (if the Social plan tab is missing), then
upgrade_counted_review.py, then upgrade_social_review.py, then shows notes Claude adds to an item as
"Claude" instead of "Someone". Safe to run more than once.
"""
import os, subprocess, sys

if len(sys.argv) != 2:
    sys.exit(__doc__)
path, here = sys.argv[1], os.path.dirname(os.path.abspath(__file__))
if 'id="tab-social"' not in open(path, encoding="utf-8").read():
    subprocess.run([sys.executable, os.path.join(here, "add_social_tab.py"), path], check=True)
subprocess.run([sys.executable, os.path.join(here, "upgrade_counted_review.py"), path], check=True)
subprocess.run([sys.executable, os.path.join(here, "upgrade_social_review.py"), path], check=True)

OLD = 'const nameOf = (id) => (id && S.names[id]) || "Someone";'
NEW = 'const nameOf = (id) => id === "claude" ? "Claude" : (id && S.names[id]) || "Someone";'
s = open(path, encoding="utf-8").read()
if OLD in s:
    open(path, "w", encoding="utf-8").write(s.replace(OLD, NEW))
    print("Notes from Claude now show as Claude:", path)
