# Literature and priority check

- **Date:** 2026-11-27 (one priority check before the work started; it must be re-run before any public release).
- **Question:** has anyone proved or refuted Conjecture 6.2 of Barcau, Paşol and Ţurcaş, or proved the line-direction lemma or its corollaries?
- **Update (pre-release re-check, 2026-11-27):** the line-direction lemma (if some $A_u$ lies in an affine line, then $\lvert T-T\rvert\ge(2p-1)^2$) was posted publicly earlier on the same day by Robert Leshner with Codex, in [open-math-agents pull request #6492](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/6492) (opened 2026-11-27, 12:56 UTC; [README at commit `ba804a2`](https://github.com/rleshner/open-math-agents/blob/ba804a2813650e214c5172a1f484b1c1eda5edd8/research/transversal-seven/README.md), section "A projection bound for every odd prime"). Their proof uses a basis change, a shear, a projection onto a cyclic transversal and Kneser's theorem; ours is independent and avoids Kneser's theorem. With the count of `PROOF.md` §5 their lemma gives Corollaries 2–4. The pull request also claims a computer-assisted proof that $\delta=169$ at $p=7$ (unreviewed, not checked by us). We claim no priority. The short answer below is the first check, before this was found.
- **Short answer:** the conjecture is open for $p\ge7$. The source itself settles $p=3$ and $p=5$ by computer. Two AI-assisted groups touched the problem and went dormant; one of them (automath) has an unpublished special case of our main theorem that already gives Corollaries 2 and 4. We claim no priority.

## The source

M. Barcau, V. Paşol, G. C. Ţurcaş, *Transversal Difference Numbers in Finite Abelian Quotients*, [arXiv:2606.27961v1](https://arxiv.org/abs/2606.27961), submitted 2026-06-26; v1 is the only version on 2026-11-27. Read in the [HTML full text](https://arxiv.org/html/2606.27961v1).

What it proves or reports, as used in this repository:

| Result in the source | Content |
| --- | --- |
| Proposition 5.3 | The coordinate box gives $\delta\le(2p-1)^r$; for $r=2$ this is $(2p-1)^2$ |
| Corollary 5.2 | $\delta=9$ for $(\mathbb{Z}/4)^2$ modulo $2(\mathbb{Z}/4)^2$ |
| Lemma 6.1 | $\lvert T_f-T_f\rvert=\sum_u\lvert A_u(f)\rvert$ and $A_0=\lbrace0\rbrace$ |
| Lemma 6.3 | The cycle identity; $\lvert A_u\rvert\ge2$ for $u\ne0$; if $\lvert A_u\rvert=2$, then $A_u$ lies on a line parallel to $u$ |
| Lemma 6.4 | Two independent directions with $\lvert A_u\rvert=2$ force $\lvert T_f-T_f\rvert\ge(2p-1)^2$ |
| Theorem 6.5 | $\delta\ge3p^2-p-1$ for every odd prime $p$ |
| §6.4 | "We verified the conjecture for $p=3$ and $p=5$ by deterministic Python computations": $\delta=25$ and $\delta=81$; code and JSON certificates in [georgeturcasubb/transversals](https://github.com/georgeturcasubb/transversals). $p=7$ was not completed |
| Theorem 4.2 | Cross-transversal estimate $\lvert A-B\rvert\ge2\lvert G/H\rvert-m(G,H)$, proved with Kneser's theorem |
| Theorems 7.1, 7.2 | Random liftings, and fixed integer-polynomial liftings for large $p$, satisfy the bound; Remark 7.6 says these do not settle the conjecture |
| Conjecture 8.2 | The rank-$r$ form $(2p-1)^r$; $r=1$ is a theorem of the source, $r=2$ is Conjecture 6.2 |

## Sources searched (2026-11-27)

| Source | What was searched | Finding |
| --- | --- | --- |
| Primary source, all versions; authors' companion repository | arXiv submission history and full HTML (§§1, 6, 7, 8); companion repository README, tree, all 5 commits, issues, pull requests and forks | One version only. The paper itself settles $p=3$ and $p=5$. The companion repository was created and last pushed on 2026-06-26, with 0 issues, 0 pull requests and 0 forks |
| arXiv listing, author pages, citation databases | arXiv API searches for "transversal difference" and "transversal difference number"; author searches for Barcau, Ţurcaş and Paşol; citers through OpenAlex and Semantic Scholar | No resolution. The only other paper on the invariant is the authors' [arXiv:2609.12624](https://arxiv.org/abs/2609.12624) (an application to cryptography), which uses only the cyclic formula. Both citation databases list one citer, that paper. Google Scholar returned a bot check and was not used |
| Web and GitHub-wide search | Web search for the paper id, title and topic; GitHub-wide issue, pull-request and code search for `2606.27961`, "transversal difference" and the authors' names | No proof or counterexample anywhere. Hits: trureturing issue #8487 and the chy4pro/automath notes (both below); an open-problem catalogue entry (status open, checked 2026-10-08); feed and corpus copies of the arXiv listing |
| the-omega-institute/trureturing | Issues and pull requests (all states), issue #8487 timeline, code search | [Issue #8487](https://github.com/the-omega-institute/trureturing/issues/8487), "Research: square-plane transversal difference Conjecture 6.2", opened 2026-09-17, last updated the same day, open, 0 comments. It reports one bounded probe with "Current disposition: open", isolates the remaining inequality on the branch where the directions with $\lvert A_u\rvert=2$ lie on one line, and reports that a bounded, non-exhaustive local search at $p=7$ found nothing below 169. No pull request implements or proves it |
| chy4pro/automath | The full tree, the folder [problems/tdn_2606_27961](https://github.com/chy4pro/automath/tree/5542184180d014b68637851941109dd5e584e920/problems/tdn_2606_27961) (19 files), the briefs on this problem, the output [tdn_r4_column.out](https://github.com/chy4pro/automath/blob/5542184180d014b68637851941109dd5e584e920/problems/tdn_2606_27961/tdn_r4_column.out), the [selection note](https://github.com/chy4pro/automath/blob/5542184180d014b68637851941109dd5e584e920/notes/selection/selection_0824.md) and the [status sweep of 2026-09-25](https://github.com/chy4pro/automath/blob/5542184180d014b68637851941109dd5e584e920/notes/STATUS_SWEEP_20260925.md) | Unpublished partial work, parked. Round 4 claims a "provisional THEOREM": one direction with $\lvert A_u\rvert=2$ anywhere forces the box bound. It also states a hand proof of $p=3$, says only the "0-branch" ($\lvert A_w\rvert\ge3$ for all $w\ne0$) remains open, and reports a computational check at $p=5$. No file is dated after about 2026-08-24; the status sweep marks the line "park". Nothing was deposited (no paper, no Zenodo record) |
| Other catalogues and AI-math sites | MathDB (entries for Conjecture 6.2 and the rank-$r$ form), Hexagon, Prove2Me/formalpedia, Crab Research, eulersolve, google-deepmind/formal-conjectures, OEIS, Open Problem Garden, MathOverflow and Math.SE, Zenodo, several GitHub AI-math repositories | No hit, or "open" with no recorded progress. UnsolvedMath could not be checked (bot checkpoint) |

Not completed on 2026-11-27: UnsolvedMath and Google Scholar "cited by" (both behind bot checks, which were not bypassed).

## Timeline

| Date | Event |
| --- | --- |
| 2026-06-26 | The source appears on arXiv with Conjecture 6.2, Lemma 6.4, Theorem 6.5 and the computer verification of $p=3,5$ |
| about 2026-08-24 | Last dated automath file on the problem: round 4 states the one-2-direction theorem, the hand proof of $p=3$ and the residual "0-branch" |
| 2026-09-17 | trureturing issue #8487 is opened (and last updated) |
| 2026-09-25 | automath marks the line "park" in its [status sweep](https://github.com/chy4pro/automath/blob/5542184180d014b68637851941109dd5e584e920/notes/STATUS_SWEEP_20260925.md) |
| 2026-11-27, 12:56 UTC | Leshner with Codex open [open-math-agents pull request #6492](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/6492): the line-direction lemma ("a projection bound for every odd prime", via Kneser's theorem) and a claimed computer-assisted proof of $p=7$ |
| 2026-11-27 | This work, done independently and posted later the same day: priority check, proof of the line-direction lemma, review round 1, revision, this write-up; the pre-release re-check then found pull request #6492 |

## Comparison

| | Source (Lemma 6.4, Theorem 6.5) | automath round 4 (unpublished) | Leshner with Codex, PR #6492 (earlier on 2026-11-27) | This repository |
| --- | --- | --- | --- | --- |
| Hypothesis that forces $(2p-1)^2$ | two independent directions with $\lvert A_u\rvert=2$ | one direction with $\lvert A_u\rvert=2$ | one direction with $A_u$ on a line (any size) | one direction with $A_u$ on a line (any size) |
| General lower bound | $3p^2-p-1$ | $3p^2-2$ (same two-line count) | implied by the same count (not stated as such) | $3p^2-2$ |
| $p=3$ | by computer | by hand | not discussed; implied by the same count | by hand (Corollary 4) |
| Residual class | — | all $\lvert A_w\rvert\ge3$ (their "0-branch") | no $A_w$ on a line (used for $p=7$) | no $A_w$ on a line |
| Method | fibre decomposition and cycle identity | cycle identity, aperiodicity of a binary word of prime length, "per-coset budget" | basis change, shear, projection onto a cyclic transversal, Kneser's theorem | covering by $p$ cosets of a cyclic subgroup, then a one-dimensional cross-transversal bound used twice (no Kneser) |
| Coset form (Theorem 1 (c)) | no | not found in the files read | not stated as such in the section read | yes |

Notes:
- **The step from "$\lvert A_u\rvert=2$" to "$A_u$ on a line" is small.** A two-point set always lies on a line, so the automath statement is a special case of Theorem 1. Corollaries 2 and 4 follow from the automath statement by the same count. The extension to any collinear $A_u$ is also in pull request #6492 (Leshner with Codex), posted earlier on 2026-11-27; full credit goes to automath for the reduction and to Leshner with Codex for the lemma.
- **No file of the automath or trureturing projects was executed or copied.** Their notes were read as data.
- **The source's own $p=3$ and $p=5$ results** were not re-certified here. Our scripts share no code with the authors' repository.

## Related methods

These come from the methods review written before the proof (2026-11-27). They are context, not evidence for any claim here, and the citations were not re-checked for this write-up.

- Kneser's theorem and the cross-transversal estimate of the source (Theorem 4.2): in the cyclic group $\mathbb{Z}/p^2$ modulo $p\mathbb{Z}/p^2$, the one-dimensional bound used here (Lemma F) gives the case $m(G,H)=1$ of Theorem 4.2, by an elementary argument that avoids Kneser's theorem.
- Freiman-type results in $\mathbb{Z}^2$ for sets covered by few parallel lines, for example Grynkiewicz and Serra, [arXiv:0710.3127](https://arxiv.org/abs/0710.3127): with $p^2$ points on $p$ parallel lines such bounds give $(2p-1)^2$, and Theorem 1 can be read as an analogue in the torsion group $G$.
- Carries and transversals: Diaconis, Shao and Soundararajan, [arXiv:1309.0434](https://arxiv.org/abs/1309.0434), study which coset representatives minimise carries.

## Conclusion

- **The line-direction lemma itself was posted earlier the same day by Leshner with Codex** (pull request #6492), with a proof via Kneser's theorem. Our proof is independent and was posted later; no priority is claimed for the lemma or the corollaries. The pull request also claims $\delta=169$ at $p=7$ (unreviewed).
- Apart from that claim for $p=7$, the conjecture is **open** for $p\ge7$ and in general, as far as these checks could see on 2026-11-27.
- $\delta=25$ at $p=3$ and $\delta=81$ at $p=5$ are **in the source** (computer verification).
- The **one-2-direction statement (called a "provisional theorem", with an unreviewed sketch) and the reduction to a residual branch are in the automath notes** (unpublished, parked). Corollaries 2 and 4 follow from it.
- This repository proves the same lemma as pull request #6492 (any collinear $A_u$) by a different, Kneser-free route, adds the coset form, and writes everything out with a self-contained proof. **We claim no priority and no novelty.**
- **Collision watch.** trureturing issue #8487 is still open, and that group resumes targets at scale; the automath line could resume. The priority check must be re-run against both groups and the source's authors before any public release.
