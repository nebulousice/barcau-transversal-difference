# Zenodo notes

Prepared on 2026-11-27 for the upload of `paper.pdf`. Reserved DOI: [10.5281/zenodo.24594748](https://doi.org/10.5281/zenodo.24594748). The DOI is printed on page 1 of `paper.pdf` (first-page footnote, after the date).

**Status: upload on hold by the owner's decision (2026-11-27).** The pre-release priority re-check found that the main lemma was posted earlier the same day by Robert Leshner with Codex ([open-math-agents pull request #6492](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/6492)). The paper now credits this first (abstract, introduction, Remark 3.5, bibliography [3]).

## Before you upload (decisions for the owner)

Files cannot be changed after a Zenodo record is published, so settle these first.

1. **Credit to Leshner with Codex.** Check the new wording in the abstract and §1.3 of the paper. A new credit line has been proposed (in `README.md` and `PROOF.md` §9, marked "not approved"); it is not yet in `RELEASE.md` or the ledger.
2. **Credit statements.** The other three draft credit lines (`PROOF.md` §9) are still not approved. The paper no longer quotes them as block quotes; it states the same credit in ordinary prose in §1.3.
3. **Priority re-check.** Re-run it once more right before upload (Leshner PR #6492, automath, trureturing #8487, the source's authors).
4. **Review status.** The claim is `proposed`: review round 2 is pending. The paper's "Use of AI" paragraph uses the owner's wording and does not state the review round.
5. **Repository link.** Reference [6] cites `https://github.com/nebulousice/barcau-pasol-turcas-conjecture-6-2`, "version of 2026-11-27". Republish that repository with this text before upload, so the cited files (`PROOF.md`, `REPRODUCE.md`, `scripts/`, `scripts/out/`, `REVIEWS.md`) are there.

## Suggested metadata

- **Resource type:** Publication / Preprint
- **Title:** A line-direction lemma for the transversal difference number of (Z/p²Z)²
- **Creators:** Sachdeva, Sukhraj
- **Publication date:** the upload date (the PDF is dated 2026-11-27)
- **Language:** English
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Keywords:** transversal; difference set; sumset; finite abelian group; transversal difference number
- **Subjects (MSC 2020):** 11B13 (primary); 11P70, 20K01 (secondary)
- **Files:** `paper.pdf` (required). Optionally also `paper.tex`, so the source is archived with the PDF.

**Description (the abstract of the paper, 177 words in the LaTeX version):**

> Let p be an odd prime, G = (Z/p²Z)² and H = pG. Barcau, Paşol and Ţurcaş conjectured that every transversal T of H in G satisfies |T − T| ≥ (2p − 1)². They write each transversal through a function f: F_p² → F_p², and for each u ∈ F_p² the differences of T that reduce to u modulo p correspond to a set A_u(f) ⊆ F_p². The conjectured bound holds whenever A_u(f) lies on an affine line for some u ≠ 0. This lemma was also obtained, earlier on the same day, by Leshner using the AI system Codex (GitHub pull request #6492 to GuillaumeBAUD-coder/open-math-agents). We give an independent proof, which avoids Kneser's theorem, and we claim no priority. As consequences, every transversal has at least 3p² − 2 differences, the case p = 3 (known by computation) follows by hand, and the conjecture is equivalent to its restriction to functions for which no such u exists. This remaining case is not settled here. A computer-assisted proof of the case p = 7 has been claimed in that pull request; we have not checked it. This human-directed research was produced with the help of AI tools and checked by AI referees; additional verification may still be required.

**AI-use statement (for the "Notes" field; the owner's wording, with "AI" added before "referees"):**

> Human directed research produced with the help of AI tools (Claude) and checked by AI referees (Claude Opus and Claude Fable; ChatGPT and Gemini as outside cross-checks). However, additional verification may still be required. Code and full proof: https://github.com/nebulousice/barcau-pasol-turcas-conjecture-6-2

**Related identifiers:**

| Relation | Identifier | Type |
| --- | --- | --- |
| References | arXiv:2606.27961 (https://arxiv.org/abs/2606.27961) | Preprint |
| Is supplement to | arXiv:2606.27961 | Preprint |
| References | https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/6492 | Other |
| Is supplemented by | https://github.com/nebulousice/barcau-pasol-turcas-conjecture-6-2 | Software / Dataset |
| References | https://github.com/chy4pro/automath/tree/5542184180d014b68637851941109dd5e584e920/problems/tdn_2606_27961 | Other |
| References | https://github.com/the-omega-institute/trureturing/issues/8487 | Other |

"Is supplement to" says the paper builds on the source; "References" is the safer single choice if you prefer one relation for arXiv:2606.27961.

### Why these MSC codes

- **11B13** (additive bases, including sumsets): the object is the difference set T − T of a set in a finite abelian group, a sumset T + (−T), and the question is a lower bound for its size.
- **11P70** (inverse problems of additive number theory, including sumsets): Theorem 3.1 (c)–(e) is a structural statement (a covering by cosets of a cyclic subgroup) of the kind studied there, and the related literature uses Kneser-type estimates.
- **20K01** (finite abelian groups): the setting is transversals of the subgroup p(Z/p²Z)² and the arguments are about cyclic subgroups, quotients and element orders.
- 05B10 (combinatorial aspects of difference sets) was considered and not used: it concerns difference sets in the design-theory sense, not difference sets T − T as here.

## Compile log summary

- Engine: Tectonic 0.17.0 (XeTeX-based), `tectonic.exe -X compile --keep-logs paper.tex`, run in this folder on 2026-11-27.
- Result: `paper.pdf`, 14 pages, 153,911 bytes, SHA-256 `b6b342163dea2c8e1f0e887ca99072f3cdcf17c1bcb7c97a614089776d37d3ca` (from `paper.tex` with SHA-256 `0086bf22668f45cde640a2849a964a504f18bee09e41e3b56fe5a6f3c549d14b`).
- **0 errors, 0 warnings** in `paper.log`: no undefined references or citations, no overfull or underfull boxes.
- The only other console output is `Fontconfig error: Cannot load default config file`, from the Windows font library, not from TeX. The paper uses only Latin Modern fonts from the TeX bundle.
- Text layer checked with `pdftotext` (xpdf 4.06): the title reads "(Z/p2Z)2" with a lowercase p; "Paşol" and "Ţurcaş" keep their cedillas; the author "SUKHRAJ SACHDEVA" and "DOI: 10.5281/zenodo.24594748" are on page 1.
- Static check: every `\ref`/`\eqref` has a `\label`, every `\cite` has a `\bibitem` and vice versa, environments are balanced, and there is no `$$`.

To rebuild:

```
cd results/barcau-pasol-turcas-conjecture-6-2
"$USERPROFILE/tools/tectonic/tectonic.exe" -X compile --keep-logs paper.tex
grep -n -i "warning\|overfull\|underfull\|undefined" paper.log
```

The last command should print only the package banner of `infwarerr` ("Providing info/warning/error messages"), which is informational.

## Changelog

### 2026-11-27, pre-Zenodo revision (after the pre-publication referee report on commit 86adefd)

No mathematical argument changed.

- **Credit to Leshner with Codex (new).** The pre-release re-check found [open-math-agents pull request #6492](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/6492) (opened 2026-11-27, 12:56 UTC; pinned commit `ba804a2`), whose section "A projection bound for every odd prime" proves the inequality of Theorem 3.1 (a) with Kneser's theorem, and which also claims a computer-assisted proof of p = 7. The paper credits it first: in the abstract, in §1.2, at the start of §1.3, in Remark 3.5, and as reference [3]. It says that our work was done independently and posted later the same day, that our proof avoids Kneser's theorem, that their lemma also gives Corollaries 3.2–3.4, and that no priority is claimed. The sentence "to our knowledge the conjecture remains open for p ≥ 7" was replaced by a statement that p = 7 is claimed in [3] and not checked by us. `README.md`, `PROOF.md` and `LITERATURE_CHECK.md` were updated the same way.
- **Referee issue 1 (author):** already done; "Sukhraj Sachdeva" kept.
- **Issue 2 (title):** the title math is now `$...$` outside `\texorpdfstring`, so amsart's upper-casing leaves it alone; the PDF title metadata is set separately. The rendered title reads (Z/p²Z)² with a lowercase p.
- **Issue 3 (automath wording):** the notes are now described as a numerical log, an unreviewed proof sketch and a status note that calls the one-2-direction claim a "provisional theorem"; the paper says they *state* that case and its consequences, that we located no complete written proof, and that we did not compare our proof with their sketch. "Our proof is organised differently from theirs" was removed. "Parked on 2026-09-25" was removed from the paper (it is verifiable, from their status sweep of 2026-09-25, and is kept with that link in `README.md`, `PROOF.md` and `LITERATURE_CHECK.md`). "Lines 36–40" was verified against the pinned file (the quoted text is on lines 37–38) and kept. The bibliography entry is now the folder link plus the status-note link, pinned to commit `5542184`.
- **Issue 4 (acknowledgements):** replaced by a short "Use of AI" paragraph in the owner's wording, with "AI" added before "referees" so they are not mistaken for human referees, and the repository given as reference [6]. No model codenames beyond the owner's text, no round status, no "blindness".
- **Issue 5 (repository citation):** reference [6] now reads "S. Sachdeva, Accompanying repository of this paper: code, archived logs, full proof and review history, version of 2026-11-27".
- **Issue 6 (padding):** Sections 7 and 8 merged into one paragraph, "Computer checks and formalization" (what is checked, that no proof step depends on it, the repository pointer, and one sentence that nothing is formalized). Subsections 1.4–1.5 cut to one sentence. The credit block quotes removed. Remark 6.1 (the N₃ − E reformulation, unused) removed. The comparison with 3p² − p − 1 is now Remark 6.1. The consistency check after part (b) is now a remark. "The proof is elementary" and "the heart of the matter" removed.
- **Issue 7 (structure):** Theorem 3.1 (c) split into (c) the covering, (d) the converse and (e) the explicit "f has a line direction if and only if T_f lies in at most p cosets of a cyclic subgroup of order p²" plus closure under nonzero multiples; the proof of (e) adds one sentence on why π(C′) ≠ {0}. "Without computation" removed from the statement of Corollary 3.4 (now "This proof uses no computation" in its proof). The minimum in Corollary 3.2 moved into the proof, with (2p − 1)² − (3p² − 2) = (p − 1)(p − 3) ≥ 0 for p ≥ 3.
- **Issue 8 (notation):** in Lemma 4.6 and Remark 4.7 the group is now Γ, the transversals X₁, X₂, and the fibres D_r; [Q:K] and [C:pC] are now |Q/K| and |C/pC|; `\ord` removed; "column sum" has its own sentence after Definition 2.1 ("the total size of the sets A_w(f) over the points of the u-line"); "lying over u" replaced by "that reduce to u modulo p" in the abstract and in the proof of part (b).
- **Issue 9 (bibliography and front matter):** the bibliography is in order of first citation in the body, with BPT first; the automath entry is shortened; `\usepackage{cmap}` is loaded under pdfTeX (guarded with `iftex`, since under XeTeX it would only issue a warning) before `\usepackage[T1]{fontenc}`; the DOI line stays on the title page.
