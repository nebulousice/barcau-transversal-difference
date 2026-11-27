# A line-direction lemma for the odd square-plane conjecture of Barcau, Paşol and Ţurcaş

Paper: [`paper.pdf`](paper.pdf), DOI [10.5281/zenodo.24594748](https://doi.org/10.5281/zenodo.24594748) (reserved on Zenodo).

> **Credit first.** The main lemma below (if some $`A_u(f)`$ lies on an affine line, then the transversal has at least $(2p-1)^2$ differences) was posted publicly earlier on the same day, 2026-11-27, by Robert Leshner with Codex, in [open-math-agents pull request #6492](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/6492) (opened 12:56 UTC; [README at commit `ba804a2`](https://github.com/rleshner/open-math-agents/blob/ba804a2813650e214c5172a1f484b1c1eda5edd8/research/transversal-seven/README.md), section "A projection bound for every odd prime"). Our work was done independently and was posted later the same day. We claim no priority for the lemma or for any corollary. Their proof uses a basis change, a shear, a projection onto a cyclic transversal and Kneser's theorem; ours covers the transversal by cosets of a cyclic subgroup and uses an elementary two-transversal lemma instead of Kneser's theorem. The same pull request also claims a computer-assisted proof that $`\delta=169`$ at $p=7$; we have not checked that claim.

> **In one line:** if one of the "difference images" $`A_u(f)`$ of a transversal lies on a line, the transversal already has at least $(2p-1)^2$ differences, as the conjecture predicts (also obtained, earlier the same day, by Leshner with Codex; see above). This gives the lower bound $3p^2-2$ for every odd prime $p$ and reduces the conjecture to transversals with no such direction. It is a **partial result**, proved by hand with no computational step. Its status is `proposed`: review round 2 is pending, and **Expert verification required.** Verified so far with: AI referees in review round 1 (Claude Opus 5.5, line by line: one minor issue about the description of the checking script, no mathematical error, issue fixed; Claude Fable, adversarial: accept with zero issues), with round 2 pending; outside AI cross-checks by ChatGPT and Gemini (no mathematical error or gap found); and exact-arithmetic computer checks, which are evidence only. Nothing is formalized in Lean 4 with Mathlib.

## Summary

**The problem.** Let $p$ be a prime, let $`G=(\mathbb{Z}/p^2\mathbb{Z})^2`$ and let $H=pG$, the subgroup of elements whose two coordinates are multiples of $p$. A **transversal** of $H$ in $G$ is a set $`T\subseteq G`$ that contains exactly one element of each coset of $H$; it has $p^2$ elements. Its **difference set** is $T-T$, the set of all differences $t-t'$ with $`t,t'\in T`$. The **transversal difference number** $`\delta(G,H)`$ is the least size of $T-T$ over all transversals $T$. Conjecture 6.2 of Barcau, Paşol and Ţurcaş ([arXiv:2606.27961](https://arxiv.org/abs/2606.27961)) says that for every odd prime $p$

```math
\delta\bigl((\mathbb{Z}/p^{2}\mathbb{Z})^{2},\ p(\mathbb{Z}/p^{2}\mathbb{Z})^{2}\bigr)=(2p-1)^{2}.
```

The "box" $`\lbrace0,\dots,p-1\rbrace^2`$ shows that $`\delta`$ is at most $(2p-1)^2$. The source proves the lower bound $3p^2-p-1$, and it verifies $p=3$ and $p=5$ by computer.

**Coordinates on transversals.** Write $`[x]\in\lbrace0,\dots,p-1\rbrace^2`$ for the standard lift of $`x\in\mathbb{F}_p^2`$, and $`\iota(a)=p[a]`$ in $G$. Every transversal is $`T_f=\lbrace [x]+\iota(f(x))\rbrace`$ for exactly one function $`f:\mathbb{F}_p^2\to\mathbb{F}_p^2`$. For $`u,x\in\mathbb{F}_p^2`$ the source defines the carry $`c_u(x)`$, the corrected difference $`d_uf(x)`$ and its image $`A_u(f)`$:

```math
c_u(x)=\frac{[x+u]-[x]-[u]}{p},\qquad d_uf(x)=f(x+u)-f(x)+c_u(x),\qquad A_u(f)=\{d_uf(x):x\in\mathbb{F}_p^2\}.
```

The source shows that the elements of $`T_f-T_f`$ that reduce to $u$ modulo $p$ correspond one-to-one to the elements of $`A_u(f)`$, so the size of $`T_f-T_f`$ is the sum of the sizes of the sets $`A_u(f)`$. An **affine line** in $`\mathbb{F}_p^2`$ is a set $`a+\lbrace\lambda s:\lambda\in\mathbb{F}_p\rbrace`$ with $`s\ne0`$. A **line direction** of $f$ is a nonzero $u$ such that $`A_u(f)`$ lies in an affine line.

**Theorem 1 (line-direction lemma).** Let $p$ be an odd prime and $`f:\mathbb{F}_p^2\to\mathbb{F}_p^2`$. If $f$ has a line direction $u$, then

```math
\lvert T_f-T_f\rvert=\sum_{w\in\mathbb{F}_p^2}\lvert A_w(f)\rvert\ \ge\ (2p-1)^2 .
```

Moreover, every column sum $`\sum_{k}\lvert A_{ku+v}(f)\rvert`$ with $v$ off the line through $0$ and $u$ is at least $4p-2$. And $`T_f`$ lies in $p$ cosets of a cyclic subgroup of $G$ of order $p^2$. Conversely, if $`T_f`$ lies in at most $p$ cosets of a cyclic subgroup $C$ of order $p^2$, then the reduction modulo $p$ of every element of $C$ is either $0$ or a line direction. Hence $f$ has a line direction if and only if $`T_f`$ lies in at most $p$ cosets of some cyclic subgroup of order $p^2$.

**Corollary 2.** $`\delta\ge3p^2-2`$ for every odd prime $p$. (The source has $3p^2-p-1$.)

**Corollary 3.** Conjecture 6.2 holds at $p$ if and only if $`\sum_u\lvert A_u(f)\rvert\ge(2p-1)^2`$ for every function $f$ with no line direction.

**Corollary 4.** $`\delta=25`$ at $p=3$, proved without computation. (The source already has this value by computer.)

**Priority.** We claim **no priority and no novelty**. The inequality of Theorem 1 and Corollaries 2–4 were obtained earlier, on the same day, by Leshner with Codex; Corollaries 2 and 4 were also within reach of the earlier automath notes.
- Robert Leshner with Codex, [open-math-agents pull request #6492](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/6492) (opened 2026-11-27, 12:56 UTC; pinned commit `ba804a2`), section "A projection bound for every odd prime": if some $`A_u`$ lies in an affine line, then $`\lvert T-T\rvert\ge(2p-1)^2`$, proved with a basis change, a shear, a projection onto a cyclic transversal and Kneser's theorem. Our work was done independently and posted later the same day. The pull request also claims a computer-assisted proof that $`\delta=169`$ at $p=7$ (not checked by us).
- The setting, the fibre decomposition, the cycle identity, the two-direction lemma (two independent directions with $`\lvert A_u\rvert=2`$ force the box bound), the bound $3p^2-p-1$ and the conjecture are due to Barcau, Paşol and Ţurcaş. Their §6.4 also verifies $`\delta=25`$ at $p=3$ and $`\delta=81`$ at $p=5$ by computer, with code in [georgeturcasubb/transversals](https://github.com/georgeturcasubb/transversals).
- The unpublished working notes of the [chy4pro/automath](https://github.com/chy4pro/automath/tree/5542184180d014b68637851941109dd5e584e920/problems/tdn_2606_27961) project (round 4, 2026; marked "park" in their [status sweep of 2026-09-25](https://github.com/chy4pro/automath/blob/5542184180d014b68637851941109dd5e584e920/notes/STATUS_SWEEP_20260925.md)) consist of a numerical log, an unreviewed proof sketch and a [status note](https://github.com/chy4pro/automath/blob/5542184180d014b68637851941109dd5e584e920/notes/selection/selection_0824.md) (lines 36–40). The status note calls the following statement a "provisional theorem": a **single** direction with $`\lvert A_u\rvert=2`$ forces $(2p-1)^2$. The notes state this case together with its consequences (with the same two-line count used here: Corollary 2, the case $p=3$ by hand, and a reduction of the conjecture to a residual class, which their log records as open). We located no complete written proof there and did not compare our proof with their sketch. Theorem 1 replaces "$`\lvert A_u\rvert=2`$" by "$`A_u`$ lies in a line" (of any size), adds the covering form, and so leaves a smaller residual class.
- The-omega-institute/trureturing [issue #8487](https://github.com/the-omega-institute/trureturing/issues/8487) (2026-09-17) isolated the residual inequality when the directions with $`\lvert A_u\rvert=2`$ lie on one line through $0$.

Draft credit lines (drafted for the repository owner's approval; **not yet approved**, and the final release gate has not run):
- "The setting, the fibre decomposition, the cycle identity, the two-direction lemma, the bound $3p^2-p-1$ and the conjecture are due to Barcau, Paşol and Ţurcaş (arXiv:2606.27961)."
- "That a single direction with $`\lvert A_u\rvert=2`$ forces $(2p-1)^2$, with the column bound $4p-2$, the count $1+3(p^2-1)$ for the remaining branch (which gives $3p^2-2$ and settles $p=3$) and the reduction to a residual '0-branch', appears in the unpublished working notes of the chy4pro/automath project (round 4, 2026). The line-direction lemma extends that statement to every collinear image."
- "The residual inequality for collinear 2-directions was isolated in the-omega-institute/trureturing issue #8487."

A further credit line is needed and has been proposed, not approved: "The line-direction lemma (if some $`A_u`$ lies in an affine line, then $`\lvert T-T\rvert\ge(2p-1)^2`$), and with it $`\delta\ge3p^2-2`$, was posted earlier on 2026-11-27 by Robert Leshner with Codex (open-math-agents pull request #6492); the proof here was found independently and avoids Kneser's theorem."

[`LITERATURE_CHECK.md`](LITERATURE_CHECK.md) gives the search, the timeline and a comparison.

**Method.**
1. A short identity from the source (the cycle identity) forces a line containing $`A_u(f)`$ to be parallel to $u$.
2. That says exactly that every step $t(x+u)-t(x)$ of the transversal lies in one cyclic subgroup $C$ of order $p^2$. So $T$ is covered by $p$ cosets of $C$, one for each line parallel to $u$.
3. An elementary one-dimensional bound. Let $K$ be a subgroup of index $q$ in an abelian group, and assume every element outside $K$ has order larger than $q$. If $A$ and $B$ each contain exactly one element of every coset of $K$, then $A-B$ has at least $2q-1$ elements, and at most one coset of $K$ contains only one of them.
4. Apply this bound twice: once in the quotient $G/C$, to show that $T-T$ meets at least $2p-1$ cosets of $C$; and once inside $C$, to show that $T-T$ has at least $2p-1$ elements in each of those cosets. Multiply.
5. For the corollaries: a function with no line direction has $`\lvert A_u(f)\rvert\ge3`$ for all $`u\ne0`$, because any two points lie on a line. So $`\lvert T-T\rvert\ge1+3(p^2-1)=3p^2-2`$, and $`3p^2-2\le(2p-1)^2`$, with equality at $p=3$.

**Side facts.**
- The bounds of Theorem 1 are attained for every $p$ by the box, with column sums exactly $4p-2$.
- Line directions come in whole lines through $0$: if $u$ is one, so is every nonzero multiple of $u$.
- No step uses that $p$ is odd. At $p=2$ the same argument gives $`\delta=9`$, which agrees with Corollary 5.2 of the source.
- The one-dimensional bound needs its order hypothesis: in $`\mathbb{Z}/6`$ modulo $`\lbrace0,3\rbrace`$ the transversal $`\lbrace0,2,4\rbrace`$ has only 3 differences, not 5.

**Verification.**
- **Certificates:** none are needed. The proof has no computational step.
- **Numerical checks** (`numerical`, evidence only; no argument depends on them): an exact-arithmetic script, [`scripts/check_L1.py`](scripts/check_L1.py), tests the labelled steps of the proof from the definitions. At $p=3$ it runs over the complete class of 704,214 functions with $f(0)=0$ and a line direction; the minimum of $`\lvert T-T\rvert`$ is 25 and the least column sum is 10. A separate exhaustive scan of all $9^8$ functions with $f(0)=0$, [`scripts/rows.py`](scripts/rows.py), finds the same count, 704,214, and the same histogram. All archived runs of the checker end with `RESULT: ALL CHECKS PASS`.
- **Lean:** nothing is formalized yet. [`LEAN.md`](LEAN.md) gives the plan; all of it looks feasible.
- **Review:** in round 1 (commit `db81f87`) an adversarial referee (Claude Fable) accepted with zero issues, and a line-by-line referee (Claude Opus 5.5) found one minor issue: the proof overstated what the checking script tests. There was no mathematical error. The issue is fixed (commit `1c9f155`). Round 2, with three referees, is pending. See [`REVIEWS.md`](REVIEWS.md).
- **Expert verification required.** Verified so far with: AI referees in review round 1 (Claude Opus 5.5, line by line: one minor issue about the description of the checking script, no mathematical error, issue fixed; Claude Fable, adversarial: accept with zero issues), with round 2 pending; outside AI cross-checks by ChatGPT and Gemini (no mathematical error or gap found); and exact-arithmetic computer checks, which are evidence only. Nothing is formalized in Lean 4 with Mathlib.

**Use of AI.** Human directed research produced with the help of AI tools (Claude) and checked by AI referees (Claude Opus and Claude Fable; ChatGPT and Gemini as outside cross-checks). However, additional verification may still be required. Code and full proof: https://github.com/nebulousice/barcau-pasol-turcas-conjecture-6-2

**How it was made.** Produced on 2026-11-27 by an automated research pipeline of AI agents (Claude models), run by the repository owner. Separate agents checked priority, surveyed methods, wrote the proof and the scripts, and refereed blind on different models. Every claim carries a status word in a claim ledger. Computation ran on one Windows 11 machine with Python 3.12.10.

## Names in the paper

The paper numbers results by section. Theorem 1 here is Theorem 3.1 there (its last paragraph is split there into parts (c), (d) and (e)), and Corollaries 2, 3, 4 are Corollaries 3.2, 3.3, 3.4. In [`PROOF.md`](PROOF.md), Facts 1–3 are Lemma 2.2 (a)–(c) of the paper (Definition 2.1 defines line directions; column sums are defined right after it); Lemmas A–F are Lemmas 4.1–4.6; Lemma G is Lemma 5.1; steps (3a)–(3d) are Claims A–D of Section 5.2; and the sets $`A_n`$ of step (3d) are called $`S_n`$ in the paper.

## Where to start

| If you want… | Read |
| --- | --- |
| The proof | [`paper.pdf`](paper.pdf) (the paper, DOI [10.5281/zenodo.24594748](https://doi.org/10.5281/zenodo.24594748)), [`paper.tex`](paper.tex) (its LaTeX source) or [`PROOF.md`](PROOF.md) (Markdown) |
| To rerun the checks | [`REPRODUCE.md`](REPRODUCE.md): `cd scripts`, then `python check_L1.py algebra` and the other parts |
| How it relates to earlier work | [`LITERATURE_CHECK.md`](LITERATURE_CHECK.md) |
| The review history | [`REVIEWS.md`](REVIEWS.md) |
| What could be formalized in Lean | [`LEAN.md`](LEAN.md) |

---

## Research log

### Setup

Barcau, Paşol and Ţurcaş, *Transversal Difference Numbers in Finite Abelian Quotients*, [arXiv:2606.27961v1](https://arxiv.org/abs/2606.27961) (2026-06-26, the only version on 2026-11-27), §6, Conjecture 6.2. A priority check on 2026-11-27 found the conjecture open for $`p\ge7`$, with no solution claim and no active work; see [`LITERATURE_CHECK.md`](LITERATURE_CHECK.md). A re-check before release, later the same day, found [open-math-agents pull request #6492](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/6492) (opened 2026-11-27, 12:56 UTC), which contains the line-direction lemma and claims a computer-assisted proof of $p=7$.

### Notation

- $p$ is a prime; $`\mathbb{F}_p`$ is the field with $p$ elements.
- $`G=(\mathbb{Z}/p^2\mathbb{Z})^2`$, $H=pG$, and $`\pi:G\to\mathbb{F}_p^2`$ is reduction modulo $p$; its kernel is $H$.
- $[x]$ is the standard lift of $`x\in\mathbb{F}_p^2`$ to $`\lbrace0,\dots,p-1\rbrace^2`$; $`\iota(a)=p[a]`$ in $G$.
- $`t_f(x)=[x]+\iota(f(x))`$ and $`T_f=\lbrace t_f(x)\rbrace`$.
- $`c_u`$, $`d_uf`$, $`A_u(f)`$ as displayed in the Summary.
- $`\langle u\rangle=\lbrace\lambda u:\lambda\in\mathbb{F}_p\rbrace`$, the line through $0$ and $u$.
- The **column sum** of a coset $`v+\langle u\rangle`$ is $`\sum_{k\in\mathbb{F}_p}\lvert A_{ku+v}(f)\rvert`$.

The source's first values are reproduced: for the box $f=0$, literal subtraction in $G$ gives $`\lvert T_0-T_0\rvert=25,81,169,441,625`$ for $p=3,5,7,11,13$, which is $(2p-1)^2$.

### Results along the way

| # | Statement | Status | Evidence |
| --- | --- | --- | --- |
| 1 | Our conventions match the source: the box gives $(2p-1)^2$ for $p=3,5,7,11,13$ by literal subtraction | `numerical` | [`scripts/out/rows.log`](scripts/out/rows.log) part [1]; [`scripts/out/check_algebra.log`](scripts/out/check_algebra.log) for $p=2,3,5,7,11$ |
| 2 | A line containing $`A_u(f)`$ is parallel to $u$; $`\lvert A_u(f)\rvert\ge2`$ for $`u\ne0`$ (extends source Lemma 6.3) | `proposed` | [`PROOF.md`](PROOF.md) Lemma C |
| 3 | One-dimensional cross-transversal bound: if $K$ has index $q$, every element outside $K$ has order larger than $q$, and $A$, $B$ each meet every coset of $K$ exactly once, then $A-B$ has at least $2q-1$ elements | `proposed` | [`PROOF.md`](PROOF.md) Lemma F; exhaustive check on cyclic groups up to $`\mathbb{Z}/27`$ in [`scripts/out/check_lemmaF.log`](scripts/out/check_lemmaF.log) (`numerical`) |
| 4 | Covering criterion: $`A_u(f)\subseteq a+\langle u\rangle`$ if and only if $`T_f`$ lies in $p$ cosets of the cyclic group generated by $`[u]+\iota(a)`$ | `proposed` | [`PROOF.md`](PROOF.md) Lemma G |
| 5 | **Theorem 1** (line-direction lemma), parts (a), (b), (c) | `proposed` | [`PROOF.md`](PROOF.md) §4 |
| 6 | **Corollary 2**: $`\delta\ge3p^2-2`$ for every odd prime $p$ | `proposed` | [`PROOF.md`](PROOF.md) §5 |
| 7 | **Corollary 3**: the conjecture at $p$ is equivalent to its case with no line direction | `proposed` | [`PROOF.md`](PROOF.md) §5 |
| 8 | **Corollary 4**: $`\delta=25`$ at $p=3$, without computation | `proposed` | [`PROOF.md`](PROOF.md) §5; the value agrees with the source's computation and with the exhaustive scan in [`scripts/out/rows.log`](scripts/out/rows.log) part [3] |
| 9 | At $p=3$, all 704,214 functions with $f(0)=0$ and a line direction pass every labelled check; least $`\lvert T-T\rvert`$ 25, least column sum 10 | `numerical` | [`scripts/out/check_p3merge.log`](scripts/out/check_p3merge.log), identical histogram in [`scripts/out/rows_p3.json`](scripts/out/rows_p3.json) |
| 10 | The statements that do not depend on $f$ hold for $p=2,3,5,7,11$, for every element and every cyclic subgroup of order $p^2$ | `numerical` | [`scripts/out/check_algebra.log`](scripts/out/check_algebra.log) |
| 11 | Stored and random functions at $p=3,5,7,11$, and all 64 normalised functions at $p=2$: every check passes | `numerical` | [`scripts/out/check_stored.log`](scripts/out/check_stored.log), `check_random_*.log`, [`scripts/out/check_p2.log`](scripts/out/check_p2.log) |

### Status as recorded in the claim ledger (2026-11-27)

Copied from the private working repository's claim ledger. Internal identifiers are replaced by the names used here, and file paths by their copies in this repository.

| Claim | Status | Evidence | Reviews | Date |
| --- | --- | --- | --- | --- |
| Line-direction lemma (Theorem 1): if some $`A_u`$ lies in an affine line then $`\lvert T-T\rvert\ge(2p-1)^2`$ (plus column bounds and the coset form); hence $`\delta\ge3p^2-2`$ for every odd prime $p$ (Corollary 2), Conj. 6.2 is equivalent to its no-line-direction branch (Corollary 3), $`\delta=25`$ at $p=3$ (Corollary 4) | proposed (complete written proof, no computational step; the checks of `check_L1.py` are numerical evidence only, and `PROOF.md` §6 lists exactly what they test and which steps have no machine check). Credit: source, automath (one-2-direction theorem already gives Corollaries 2 and 4), trureturing #8487 | [`PROOF.md`](PROOF.md), [`scripts/out/`](scripts/out/) (incl. `check_algebra.log`), [`REVIEWS.md`](REVIEWS.md) | Round 1 at `db81f87`: adversarial referee accept (0 issues; partial blindness slip: skimmed the working brief, including a sketch of the lemma; no plans or prover notes), line-by-line referee minor (1 issue: §§6–7 overstated script coverage; no math error); issue fixed in the consolidation; round 2 pending | 2026-11-27 |

### Timeline (all 2026-11-27)

1. Priority check: the conjecture is open for $`p\ge7`$; the source settles $p=3,5$; two dormant AI-group lines (automath, trureturing) are to be credited.
2. Methods review and first values. The box values and $`\delta=25`$ at $p=3$ are reproduced; the line-direction lemma is first sketched.
3. Full written proof (commit `db81f87`), with the checking script.
4. Review round 1: one accept with zero issues, one minor issue (script coverage overstated).
5. Fix: a new `algebra` part of the script tests the remaining steps directly from the definitions; the proof's tables now say exactly what is tested (commit `1c9f155`). All 12 runs pass again.
6. This write-up. Review round 2 is pending.
7. The pre-release priority re-check found that Leshner with Codex posted the line-direction lemma, with a different proof, earlier the same day (pull request #6492). The paper, this README and `PROOF.md` now credit it first; no priority is claimed.

## Files

| Path | Contents |
| --- | --- |
| [`PROOF.md`](PROOF.md) | **The complete proof**, every step with its status word, and the table of what is machine-checked |
| [`paper.tex`](paper.tex), [`paper.pdf`](paper.pdf) | The same mathematics as an `amsart` paper, compiled with Tectonic 0.17.0 (no errors or warnings); DOI [10.5281/zenodo.24594748](https://doi.org/10.5281/zenodo.24594748) |
| [`ZENODO_NOTES.md`](ZENODO_NOTES.md) | Suggested Zenodo metadata and the compile log summary |
| [`LITERATURE_CHECK.md`](LITERATURE_CHECK.md) | Priority search, timeline and comparison with earlier work |
| [`REVIEWS.md`](REVIEWS.md) | Review history |
| [`LEAN.md`](LEAN.md) | Lean feasibility and plan (nothing formalized yet) |
| [`REPRODUCE.md`](REPRODUCE.md) | Exact commands, versions, runtimes and expected output |
| [`scripts/check_L1.py`](scripts/check_L1.py) | Step-by-step numerical checker (Python standard library, exact integers) |
| [`scripts/rows.py`](scripts/rows.py) | Exhaustive scan at $p=3$ by a separate program (NumPy) |
| [`scripts/lint_proof.py`](scripts/lint_proof.py) | Formatting lint of `PROOF.md` |
| [`scripts/out/`](scripts/out/) | Archived logs and JSON of every run, and the stored input functions |

## Credits

- Mathematics and code: AI agents of the research pipeline (Claude Fable wrote the proof, the scripts and the methods review; Claude Opus 5.5 merged the review fixes), directed by the repository owner.
- Referees: Claude Opus 5.5 (line-by-line) and Claude Fable (adversarial).
- Credit to Robert Leshner and Codex for the line-direction lemma, posted earlier the same day in [open-math-agents pull request #6492](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/6492).
- Thanks to Mugurel Barcau, Vicenţiu Paşol and George C. Ţurcaş for the conjecture and the framework, and to the automath and trureturing projects for their earlier work on it.
