#!/usr/bin/env python3
"""lint_proof.py -- formatting lint for ../PROOF.md (GitHub math rules of CLAUDE.md).
Checks: no \\operatorname, no thin space, no bare * or | or \\{ in inline math, balanced $ per line,
and that every log file named in PROOF.md exists under prover/out or scripts/out."""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
s = open(os.path.join(ROOT, "PROOF.md"), encoding="utf-8").read()
BS = chr(92)
problems = 0
if "operatorname" in s:
    problems += 1
    print("operatorname present")
if BS + "," in s:
    problems += 1
    print("thin space present:", s.count(BS + ","))
body = re.sub(r"```.*?```", "", s, flags=re.S)
for m in re.finditer(r"\$[^$\n]+\$", body):
    t = m.group(0)
    if (BS + "{") in t or "*" in t or "|" in t:
        problems += 1
        print("INLINE:", t)
for i, line in enumerate(body.split("\n"), 1):
    if line.count("$") % 2:
        problems += 1
        print("ODD $ on line", i, line[:120])
names = set(re.findall(r"`((?:prover/out/|scripts/out/)?[A-Za-z0-9_]+\.(?:log|json))`", s))
for n in sorted(names):
    cands = [os.path.join(ROOT, n), os.path.join(ROOT, "prover", "out", n), os.path.join(ROOT, "scripts", "out", n)]
    if not any(os.path.exists(c) for c in cands):
        problems += 1
        print("MISSING FILE:", n)
words = sorted(set(re.findall(r"`(formalized|proved|certified|numerical|heuristic|refuted|proposed|open)`", s)))
print("status words used:", words)
print("characters:", len(s), " problems:", problems)
sys.exit(1 if problems else 0)
