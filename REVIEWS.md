# Review history

**Current status (2026-11-27):** `proposed`. Review round 1 did not pass (our rule needs both referees to accept with zero issues). Its single issue, which was minor, has been fixed. Review round 2, with three referees, is pending on the revised version. **Expert verification required.** Verified so far with AI referees on different Claude models (Opus, Fable; round 1, no mathematical error found; round 2 in progress) and exact computer checks

## The review rule

- **Round 1.** Two referees on different models review the same commit. Each reads the full package (proof, scripts, logs and the source), blind to the other referee and to the working notes of the proof's author. If both accept with zero issues, the proof passes.
- **Later rounds.** Otherwise every issue is fixed or rebutted in a new commit. Then three referees review that commit: the two from round 1 and a third on a third model, fresh and blind. The proof passes when at least two of the three accept with zero issues and no referee has an unresolved major issue.
- A major issue from any referee always blocks.

## Round 1 (commit `db81f87`, 2026-11-27)

Package reviewed: `PROOF.md` (blob `345528f0d462`), `check_L1.py` (blob `c31bdce2af50`), `lint_proof.py` (blob `d9ae3b9381a5`), every archived log, and the source (arXiv:2606.27961v1, HTML, read on 2026-11-27).

### Line-by-line referee (Claude Opus 5.5): **minor**, 1 issue

- **Mathematics:** checked line by line, with no gap or error found. Facts 1–3, Lemmas A–G, Theorem 1 (a)–(c) and Corollaries 2–4 are correct as written. The statement matches the source, and the cited source results say what the proof says they say.
- **Issue 1 (minor).** The proof's table of steps and its section on data checks overstated what `check_L1.py` tests.
  - Step (3a) was assumed by the script, not tested: membership in $M=H+C$ and classes in $Q/K$ were computed through the identification that (3a) proves.
  - The check for step (3c) repeated the check for step 2.
  - Lemma D (iv), the formula $\lvert A_w(0)\rvert=2^{n(w)}$ of Lemma E, the last statement of Lemma G and Facts 1–2 had no check at all.
  - "q = 1, 2, 3 by hand" for Lemma F was one example for each $q$, not a verification.
  - Why it matters: a reader would take these steps as machine-tested. It does not affect correctness, because the proof does not depend on the script.
- **Two optional notes:** a sentence comparing $3p^2-2$ with the source's $3p^2-p-1$ said "for $p\ge5$" where "for every odd $p$" is also true; and a bound variable was named twice in the Lean plan.
- **Reruns:** every archived run was repeated from a clean copy of the commit; the outputs were identical apart from timings.
- **Independent checks** (the referee's own code, kept in session scratch space and not archived):
  - a NumPy scan of all $9^8=43{,}046{,}721$ functions with $f(0)=0$ at $p=3$ (1,134.6 s): 704,214 functions with a line direction (4,374 with two line subspaces), the same histogram as the archived run, column minima 10 and 5, and zero violations of Theorem 1 (a), (b), (c), Corollary 2 and Lemma A;
  - transversals built directly as $p$ cosets of a cyclic subgroup, with local search: 0 violations, minima 25 / 10 / 5 at $p=3$, 85 / 19 / 9 at $p=5$, 437 / 61 / 31 at $p=7$.
- **Disclosure:** a file read printed more of the working brief than intended (past its statement section); the referee used only the statement section.

### Adversarial referee (Claude Fable): **accept**, 0 issues

- Assumed the proof was wrong and tried to break every lemma by hand and by independent computation; nothing broke.
- **Attacks tried** (own code, kept in session scratch space and not archived):
  - an exhaustive scan at $p=3$ testing collinearity against every affine line, not only lines parallel to $u$: the same 704,214 functions, least total 25, least column sum 10, least zero column 5, identical histogram;
  - all 256 functions at $p=2$;
  - Lemma F exhaustively on 18 pairs $(Z,K)$ satisfying hypothesis (O), including the non-cyclic groups $\mathbb{Z}/2\times\mathbb{Z}/4$, $\mathbb{Z}/2\times\mathbb{Z}/8$, $\mathbb{Z}/3\times\mathbb{Z}/9$, $(\mathbb{Z}/4)^2$ and $\mathbb{Z}/2\times\mathbb{Z}/12$: no violation;
  - steps (3a), (3b) by brute force for every cyclic subgroup of order $p^2$ at $p=2,3,5,7,11$;
  - transversals built intrinsically from $p$ cosets of a cyclic subgroup at $p=3,5,7$, reaching equality in (a) and (b) (81 and 18 at $p=5$; 169 and 26 at $p=7$);
  - every source citation re-read against the source.
- **Remarks (no change requested):** hypothesis (O) of Lemma F is sufficient but not necessary; the random runs at $p\ge5$ are far from the extremal regime; one shard of the $p=3$ run reports a column minimum of 11 instead of 10, which is correct because the functions attaining 10 fall in the other shards.
- **Disclosure:** a file read printed the working brief through its plan section, including a sketch of the lemma. The referee did not read the author's plans or working notes, and based every finding on the proof, the source and its own computations. This partial loss of blindness is recorded.

### Consolidation (Claude Opus 5.5)

1 issue fixed, 0 rebutted, 0 open; the 2 optional notes were also applied. No argument of the proof changed.

- **New script part `algebra`.** It checks, directly from the definitions for $p=2,3,5,7,11$: Facts 1–3 on every element; Lemma D (i)–(iv) for every element outside $H$ and (v) for every cyclic subgroup of order $p^2$; the last statement of Lemma G; step (3a) with sets only; steps (3b), (3d); and both parts of Lemma E.
- **Per-function checks no longer assume (3a).** $M=H+C$ is built as a set of sums, and step (3c) and the quotient check of Lemma F use that set.
- **Log headers** now give the Python version, the platform and the SHA-256 prefix of the script (`6be5f43954a27c0a`).
- **The proof's tables** now say exactly what is tested, under which labels and in which runs, and name the steps with no machine check.
- **Reruns:** all 12 runs end with `RESULT: ALL CHECKS PASS`; every number quoted in the proof is unchanged.
- Revised package: commit `1c9f155` (`PROOF.md` blob `ab179d2387df`, `check_L1.py` blob `f51715eae0cd`).

## Round 2: pending

Three referees (the two models of round 1 and a third, Claude Sonnet) are to review commit `1c9f155` blind.

## Changes made in this write-up

The files in this repository were produced from commit `1c9f155` for readability, without changing the mathematics:
- internal labels were replaced by theorem names (Theorem 1, Corollaries 2–4, Facts 1–3);
- some sentences were split;
- in step (3b), one sentence now spells out why $y\notin M$ when $\rho(y)\notin K$ (the reviewed version took this for granted).

The round 2 referees review the working version at `1c9f155`, not these files.

## External cross-checks (2026-11-27)

The owner gave the referee prompt in `external_checks/` (pipeline repository) to two outside models, ChatGPT and Gemini, in separate sessions.

- **Both:** no mathematical error or proof gap in Sections 2–6 (setting, fibre formula, cycle identity, the parallel, cyclic, cross and cover lemmas, Claims A–D, the count, parts (b) and (c), and all corollaries). Both supplied a $p=5$ example with a three-point collinear $A_u(f)$, confirming that the theorem covers more than the two-point case (independently re-checked: $A_u=\{(0,0),(1,0),(2,0)\}$).
- **One gap, provenance only:** the credit to the automath notes could not be verified from the paper. Response: the links are now pinned to commit `5542184` of the public repository chy4pro/automath, with the exact lines of the note that states the one-2-direction claim (`notes/selection/selection_0824.md`, lines 36–40).
