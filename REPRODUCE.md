# Reproducing the checks

The proof has **no computational step**. Everything here is `numerical` evidence: it checks that the written statements and an independent implementation of the definitions agree on finite data. No argument of the proof depends on it.

## Versions

| Item | Value |
| --- | --- |
| Python | 3.12.10 (CPython), as recorded in every log header |
| Platform of the archived runs | Windows 11, 2026-11-27 |
| `scripts/check_L1.py` | standard library only, exact integers; SHA-256 `6be5f43954a27c0a1d66cce6d44a7d8655a6ac197c1dc727a2789c1457c80f8d` (each log header prints the first 16 hex digits) |
| `scripts/rows.py` | needs NumPy (2.5.5 recorded in `scripts/out/rows_p3.json`); SHA-256 `de946177d4a70eab8427871a34fb8d6f05049bc11573ef369827e2c459155943` |
| `scripts/lint_proof.py` | standard library only; SHA-256 `fcf97945f457ee15f11f70b486f66bb337fd275f80a4b11c61ed8d0773a3c6c2` |

The scripts are copies of the archived versions; none was edited for this repository. `check_L1.py` writes its logs into `scripts/out/`, and reads its four input data files (`rows_p3.json`, `rowword_p3_L30.json`, `rowword_p5_L88_0branch.json`, `triangle_columns.json`) from the same folder.

**Each run overwrites its archived log.** Run in a fresh clone and compare with `git diff`: only elapsed times should change.

## Commands

From the `scripts/` folder:

```
python check_L1.py algebra
python check_L1.py lemmaF
python check_L1.py p2
python check_L1.py p3class 0
python check_L1.py p3class 1
python check_L1.py p3class 2
python check_L1.py p3class 3
python check_L1.py p3merge
python check_L1.py stored
python check_L1.py random 5 1500 20261127
python check_L1.py random 7 200 20261127
python check_L1.py random 11 10 20261127
python lint_proof.py
```

The four `p3class` shards are independent and can run in parallel. `p3merge` needs their four outputs `out/p3class_0.json` to `out/p3class_3.json`.

Optional, the separate exhaustive scan at $p=3$ that `p3merge` compares against (it rewrites `out/rows_p3.json`):

```
python rows.py --json=out/rows_p3.json > out/rows.log
```

In Windows PowerShell 5.1, `>` writes UTF-16; use `python rows.py --json=out/rows_p3.json | Out-File -Encoding ascii out/rows.log` there.

## Runtimes

"Measured" times are wall-clock times of a rerun on 2026-11-27 on the same Windows 11 machine. "Log" times are the `elapsed` values printed in the archived logs, which cover the main loop only.

| Command | Runtime |
| --- | --- |
| `algebra` | 189.6 s (measured) |
| `lemmaF` | 28.5 s (measured) |
| `p2` | 1.4 s (measured) |
| `p3class 0`, `1`, `2`, `3` | 440.7 s, 435.7 s, 418.3 s, 422.0 s (log) |
| `p3merge` | 3.8 s (measured) |
| `stored` | 6.7 s (measured) |
| `random 5 1500 20261127` | 53.7 s (log) |
| `random 7 200 20261127` | 27.0 s (measured); 25.7 s (log) |
| `random 11 10 20261127` | 21.0 s (measured); 9.4 s (log) |
| `lint_proof.py` | under 1 s |
| `rows.py` (optional) | 142.0 s for the exhaustive part (log); under 1.5 GB of memory |

## Expected output

Every `check_L1.py` run ends with this line:

```
RESULT: ALL CHECKS PASS
```

A failing step would print `STEP FAILED -> <label>` instead. The labels use internal names: `L1` is Theorem 1, `C1` is Corollary 2, `Cor L1c` is the last sentence of Theorem 1 (c), and `N1`, `N2`, `N3` are Facts 1, 2, 3.

The other lines, copied from the archived logs (elapsed times vary):

`algebra` (`out/check_algebra.log`):

```
  p=2: N1, N2, N3 on all 16 elements of G; Lemma D (i)-(iv) for all 12 g outside H; 6 cyclic subgroups of order p^2: Lemma D (v), Lemma G (last statement), steps 3a, 3b, 3d; Lemma E: box 9 = (2p-1)^2, |A_w(0)| = 2^n(w) for all 4 w
  p=3: N1, N2, N3 on all 81 elements of G; Lemma D (i)-(iv) for all 72 g outside H; 12 cyclic subgroups of order p^2: Lemma D (v), Lemma G (last statement), steps 3a, 3b, 3d; Lemma E: box 25 = (2p-1)^2, |A_w(0)| = 2^n(w) for all 9 w
  p=5: N1, N2, N3 on all 625 elements of G; Lemma D (i)-(iv) for all 600 g outside H; 30 cyclic subgroups of order p^2: Lemma D (v), Lemma G (last statement), steps 3a, 3b, 3d; Lemma E: box 81 = (2p-1)^2, |A_w(0)| = 2^n(w) for all 25 w
  p=7: N1, N2, N3 on all 2401 elements of G; Lemma D (i)-(iv) for all 2352 g outside H; 56 cyclic subgroups of order p^2: Lemma D (v), Lemma G (last statement), steps 3a, 3b, 3d; Lemma E: box 169 = (2p-1)^2, |A_w(0)| = 2^n(w) for all 49 w
  p=11: N1, N2, N3 on all 14641 elements of G; Lemma D (i)-(iv) for all 14520 g outside H; 132 cyclic subgroups of order p^2: Lemma D (v), Lemma G (last statement), steps 3a, 3b, 3d; Lemma E: box 441 = (2p-1)^2, |A_w(0)| = 2^n(w) for all 121 w
```

`lemmaF` (`out/check_lemmaF.log`):

```
  Z=Z/1 K=<0> index q=1 hypothesis(order>q outside K)=True pairs=1 min|A-B|=1 bound 2q-1=1 violations=0
  Z=Z/4 K=<2> index q=2 hypothesis(order>q outside K)=True pairs=16 min|A-B|=3 bound 2q-1=3 violations=0
  Z=Z/9 K=<3> index q=3 hypothesis(order>q outside K)=True pairs=729 min|A-B|=5 bound 2q-1=5 violations=0
  Z=Z/8 K=<2> index q=2 hypothesis(order>q outside K)=True pairs=256 min|A-B|=3 bound 2q-1=3 violations=0
  Z=Z/25 K=<5> index q=5 hypothesis(order>q outside K)=True pairs=390625 (A,B normalised: translation does not change |A-B|) min|A-B|=9 bound 2q-1=9 violations=0
  Z=Z/27 K=<3> index q=3 hypothesis(order>q outside K)=True pairs=531441 min|A-B|=5 bound 2q-1=5 violations=0
  Z=Z/16 K=<2> index q=2 hypothesis(order>q outside K)=True pairs=4096 min|A-B|=3 bound 2q-1=3 violations=0
  Z=Z/6 K=<3> index q=3 hypothesis(order>q outside K)=False pairs=64 min|A-B|=3 bound 2q-1=5 violations=0
  Z=Z/8 K=<4> index q=4 hypothesis(order>q outside K)=False pairs=256 min|A-B|=7 bound 2q-1=7 violations=0
```

`p2` (`out/check_p2.log`):

```
  p=2: 64 normalised f; histogram (|T-T|, number of line-direction subspaces): {(9, 2): 48, (13, 0): 16}
```

`p3class K` (`out/check_p3class_K.log`), one line each:

```
  p=3 shard 0: constructed=177147 processed=177147 hist={'25': 2187, '27': 4374, '29': 4374, '31': 8748, '33': 13122, '35': 39366, '37': 61236, '39': 43740} stats={'min_cosets': 3, 'min_cross_C': 5, 'min_YY': 5, 'min_per_coset': 5, 'min_column': 10, 'column_checks': 358668, 'line_f': 177147, 'line_min_total': 25} elapsed=440.7s
  p=3 shard 1: constructed=177147 processed=176418 hist={'25': 1458, '27': 4374, '29': 4374, '31': 8748, '33': 13122, '35': 39366, '37': 61236, '39': 43740} stats={'min_cosets': 3, 'min_cross_C': 5, 'min_YY': 5, 'min_per_coset': 5, 'min_column': 10, 'column_checks': 355752, 'line_f': 176418, 'line_min_total': 25} elapsed=435.7s
  p=3 shard 2: constructed=177147 processed=175689 hist={'25': 729, '27': 4374, '29': 4374, '31': 8748, '33': 13122, '35': 39366, '37': 61236, '39': 43740} stats={'min_cosets': 3, 'min_cross_C': 5, 'min_YY': 5, 'min_per_coset': 5, 'min_column': 10, 'column_checks': 352836, 'line_f': 175689, 'line_min_total': 25} elapsed=418.3s
  p=3 shard 3: constructed=177147 processed=174960 hist={'27': 4374, '29': 4374, '31': 8748, '33': 13122, '35': 39366, '37': 61236, '39': 43740} stats={'min_cosets': 3, 'min_cross_C': 5, 'min_YY': 5, 'min_per_coset': 5, 'min_column': 11, 'column_checks': 349920, 'line_f': 174960, 'line_min_total': 27} elapsed=422.0s
```

(Shard 3 reports a column minimum of 11, which is correct: the functions attaining 10 have two line-direction subspaces and are processed in shards 0–2.)

`p3merge` (`out/check_p3merge.log`):

```
  p=3 complete hypothesis class: constructed (with repeats) = 708588; distinct f = 704214
  histogram of |T-T| over the class     : {25: 4374, 27: 17496, 29: 17496, 31: 34992, 33: 52488, 35: 157464, 37: 244944, 39: 174960}
  rows_p3.json hist_some_line_direction : {25: 4374, 27: 17496, 29: 17496, 31: 34992, 33: 52488, 35: 157464, 37: 244944, 39: 174960}
  number of line-direction subspaces    : {1: 699840, 2: 4374}
  stats (minima over the class)         : {'min_cosets': 3, 'min_cross_C': 5, 'min_YY': 5, 'min_per_coset': 5, 'min_column': 10, 'column_checks': 1417176, 'line_f': 704214, 'line_min_total': 25}
  rows_p3.json column_min=10 column_checks=8503056
  histogram identical to the exhaustive scan: True;  column minimum 10 = 4p-2 in both: True;  column checks here (f, line subspace, nonzero column) = 1417176
```

`stored` (`out/check_stored.log`):

```
  rowword_p3_L30.json: 756 solutions; (|T-T|, line subspaces): {(25, 2): 216, (27, 1): 486, (29, 1): 54}; stats {'min_cosets': 3, 'min_cross_C': 5, 'min_YY': 5, 'min_per_coset': 5, 'min_column': 10, 'column_checks': 1944, 'line_f': 756, 'line_min_total': 25}
  rowword_p5_L88_0branch.json: 70 solutions; (|T-T|, line subspaces): {(87, 0): 70}; stats {'min_cosets': 6, 'zero_branch': 70, 'zero_branch_min_total': 87}  [3p^2-2 = 73, (2p-1)^2 = 81; least number of cosets of a cyclic C of order 25 covering T = 6]
  p=5 box f=0: |T-T|=81, line subspaces=2, stats {'min_cosets': 5, 'min_cross_C': 9, 'min_YY': 9, 'min_per_coset': 9, 'min_column': 18, 'column_checks': 8, 'line_f': 1, 'line_min_total': 81}
  p=5 box with one corner moved (f(4,4) = (-1,-1)): |T-T|=97, line subspaces=0, stats {'min_cosets': 6, 'zero_branch': 1, 'zero_branch_min_total': 97}
  triangle_columns.json p=5: |T-T|=85 (box 81), line subspaces=[(1, 2)], stats {'min_cosets': 5, 'min_cross_C': 9, 'min_YY': 9, 'min_per_coset': 9, 'min_column': 19, 'column_checks': 4, 'line_f': 1, 'line_min_total': 85}
  triangle_columns.json p=7: |T-T|=191 (box 169), line subspaces=[(1, 3)], stats {'min_cosets': 7, 'min_cross_C': 13, 'min_YY': 13, 'min_per_coset': 13, 'min_column': 29, 'column_checks': 6, 'line_f': 1, 'line_min_total': 191}
```

`random` (`out/check_random_*.log`):

```
  p=5 seed=20261127: 1500 random f in the hypothesis class: min |T-T|=93 (box 81); stats {'min_cosets': 5, 'min_cross_C': 9, 'min_YY': 9, 'min_per_coset': 9, 'min_column': 21, 'column_checks': 6000, 'line_f': 1500, 'line_min_total': 93}
  p=5 seed=20261127: 1500 uniformly random f (Lemmas A, B, C, G and the 0-branch count): stats {'min_cosets': 11, 'zero_branch': 1500, 'zero_branch_min_total': 335}; elapsed 53.7s
  p=7 seed=20261127: 200 random f in the hypothesis class: min |T-T|=411 (box 169); stats {'min_cosets': 7, 'min_cross_C': 13, 'min_YY': 17, 'min_per_coset': 13, 'min_column': 51, 'column_checks': 1200, 'line_f': 200, 'line_min_total': 411}
  p=7 seed=20261127: 200 uniformly random f (Lemmas A, B, C, G and the 0-branch count): stats {'min_cosets': 24, 'zero_branch': 200, 'zero_branch_min_total': 1419}; elapsed 25.7s
  p=11 seed=20261127: 10 random f in the hypothesis class: min |T-T|=2765 (box 441); stats {'min_cosets': 11, 'min_cross_C': 21, 'min_YY': 57, 'min_per_coset': 23, 'min_column': 217, 'column_checks': 100, 'line_f': 10, 'line_min_total': 2765}
  p=11 seed=20261127: 10 uniformly random f (Lemmas A, B, C, G and the 0-branch count): stats {'min_cosets': 69, 'zero_branch': 10, 'zero_branch_min_total': 9065}; elapsed 9.4s
```

In these logs, "hypothesis class" means the functions with at least one line direction, and "0-branch" means the functions with no line direction.

`lint_proof.py` lints `PROOF.md` of this repository and exits with code 0. For the version of 2026-11-27 its output is archived in `out/lint_PROOF_writeup.log`; the last line must end in `problems: 0`. (`out/lint_proof.log` is the archived lint of the working version of the proof, at 47,419 characters.)

`rows.py` ends with `ALL CHECKS PASS`; its part [3] prints `delta((Z/9)^2, 3(Z/9)^2) = 25 (LITERAL) = 25 (FIBRE);  source: 25;  MATCH`.

## What was rerun for this write-up

On 2026-11-27, from a copy of this folder: `algebra`, `lemmaF`, `p2`, `stored`, `p3merge` (on the archived shard outputs), `random 7 200 20261127` and `random 11 10 20261127`. All ended with `RESULT: ALL CHECKS PASS`, and their logs are identical to the archived ones apart from elapsed times. The four `p3class` shards, `random 5 1500 20261127` and `rows.py` were not rerun for this write-up. Both referees of review round 1 reran every part of `check_L1.py` as it stood at commit `db81f87` (before the `algebra` part was added) and reported identical output apart from timings. After the fix, all 12 runs were repeated and archived; those are the logs in `scripts/out/`.
