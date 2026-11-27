#!/usr/bin/env python3
"""rows.py -- first values for Barcau-Pasol-Turcas Conjecture 6.2 (arXiv:2606.27961).

Independent of the companion repository of the source (georgeturcasubb/transversals):
nothing is imported or copied from it.  Two code paths that share no arithmetic:

  LITERAL : build the transversal T = {[x] + p[f(x)]} inside (Z/p^2)^2 and count T - T
            by subtracting group elements.
  FIBRE   : Lemma 6.1 of the source, sum_u |A_u(f)|, with A_u the image of
            d_u f(x) = f(x+u) - f(x) + c_u(x),  c_u(x) = ([x+u]-[x]-[u])/p,  in F_p^2 only.

Sections
  [1] conventions: box f = 0 gives (2p-1)^2 for p = 3,5,7,11,13 (both paths)
  [2] Lemma 6.1 and Lemma 6.3 (cycle, curl) on random f, p = 3,5,7,11 (both paths agree)
  [3] p = 3 EXHAUSTIVE over all 9^8 = 43,046,721 normalised f (f(0)=0), both paths,
      full histogram of |T-T|; delta = min.
  [4] p = 3 exhaustive side statistics (FIBRE path): directions whose image lies in a line,
      the column bound of the line-direction lemma, the "0-branch" (no such direction).

Usage:  python rows.py [--skip-exhaustive] [--json=PATH]
Tested with Python 3.12.10, numpy 2.5.5.  Exhaustive part: a few minutes, < 1.5 GB RAM.
"""
import sys, time, random
import numpy as np


# ----------------------------------------------------------------------------- scalar reference
def literal_count(p, f):
    """|T_f - T_f| computed in (Z/p^2)^2.  f: dict (x1,x2) -> (a1,a2), entries mod p."""
    q = p * p
    T = [((x1 + p * f[(x1, x2)][0]) % q, (x2 + p * f[(x1, x2)][1]) % q)
         for x1 in range(p) for x2 in range(p)]
    return len({((s[0] - t[0]) % q, (s[1] - t[1]) % q) for s in T for t in T})


def carry(p, u, x):
    return tuple((((x[i] + u[i]) % p) - x[i] - u[i]) // p % p for i in range(2))


def d(p, f, u, x):
    y = ((x[0] + u[0]) % p, (x[1] + u[1]) % p)
    c = carry(p, u, x)
    return ((f[y][0] - f[x][0] + c[0]) % p, (f[y][1] - f[x][1] + c[1]) % p)


def images(p, f):
    pts = [(a, b) for a in range(p) for b in range(p)]
    return {u: {d(p, f, u, x) for x in pts} for u in pts}


def fibre_count(p, f):
    return sum(len(s) for s in images(p, f).values())


def section1():
    print("[1] box f = 0: |T-T| by LITERAL and by FIBRE, against (2p-1)^2")
    ok = True
    for p in (3, 5, 7, 11, 13):
        f = {(a, b): (0, 0) for a in range(p) for b in range(p)}
        L, F = literal_count(p, f), fibre_count(p, f)
        good = (L == F == (2 * p - 1) ** 2)
        ok &= good
        print(f"    p={p:2d}  literal={L:4d}  fibre={F:4d}  (2p-1)^2={(2*p-1)**2:4d}  {'OK' if good else 'MISMATCH'}")
    return ok


def section2(seed=20261127):
    print("[2] random f: Lemma 6.1 (LITERAL == FIBRE), A_0 = {0}, cycle and curl identities, |T-T| odd, >= 3p^2-p-1")
    rng = random.Random(seed)
    ok = True
    for p, trials in ((3, 400), (5, 200), (7, 60), (11, 12)):
        pts = [(a, b) for a in range(p) for b in range(p)]
        bad = 0
        lo = 10 ** 9
        for _ in range(trials):
            f = {x: (rng.randrange(p), rng.randrange(p)) for x in pts}
            f[(0, 0)] = (0, 0)
            L, im = literal_count(p, f), images(p, f)
            F = sum(len(s) for s in im.values())
            lo = min(lo, L)
            if L != F or im[(0, 0)] != {(0, 0)} or L % 2 == 0 or L < 3 * p * p - p - 1:
                bad += 1
            for _ in range(20):
                u, v, x = rng.choice(pts[1:]), rng.choice(pts[1:]), rng.choice(pts)
                xv = ((x[0] + v[0]) % p, (x[1] + v[1]) % p)
                xu = ((x[0] + u[0]) % p, (x[1] + u[1]) % p)
                a, b = d(p, f, u, xv), d(p, f, u, x)
                c, e = d(p, f, v, xu), d(p, f, v, x)
                if ((a[0] - b[0] - c[0] + e[0]) % p, (a[1] - b[1] - c[1] + e[1]) % p) != (0, 0):
                    bad += 1                                   # curl identity
                s0 = s1 = 0
                for i in range(p):
                    y = ((x[0] + i * u[0]) % p, (x[1] + i * u[1]) % p)
                    t = d(p, f, u, y)
                    s0, s1 = s0 + t[0], s1 + t[1]
                if ((s0 + u[0]) % p, (s1 + u[1]) % p) != (0, 0):
                    bad += 1                                   # cycle identity: sum = -u
        ok &= (bad == 0)
        print(f"    p={p:2d}  trials={trials:4d}  violations={bad}  min |T-T| seen={lo}  (box {(2*p-1)**2})")
    return ok


# ----------------------------------------------------------------------------- p = 3 exhaustive
def section3_4(out=None):
    p, q = 3, 9
    pts = [(a, b) for a in range(p) for b in range(p)]          # index 0 is the origin
    nz = pts[1:]
    N_TOTAL = 9 ** 8
    CH = 9 ** 6                                                  # 531441 per chunk, 81 chunks
    hist_lit = np.zeros(82, dtype=np.int64)
    hist_fib = np.zeros(82, dtype=np.int64)
    hist_0br = np.zeros(82, dtype=np.int64)                      # no direction with image in a line
    hist_line = np.zeros(82, dtype=np.int64)                     # some direction with image in a line
    hist_two = np.zeros(82, dtype=np.int64)                      # some direction with |A_u| = 2
    prof_min = {}                                                # multiset of |A_u| among minimisers
    col_min = 10 ** 9
    col_checks = 0
    mismatch = 0
    pop = np.array([bin(i).count("1") for i in range(512)], dtype=np.int64)
    ar = np.arange(CH)
    cu = {u: [carry(p, u, x) for x in pts] for u in nz}
    idx = {x: i for i, x in enumerate(pts)}
    shift = {u: [idx[((x[0] + u[0]) % p, (x[1] + u[1]) % p)] for x in pts] for u in nz}
    t0 = time.time()
    for ch in range(N_TOTAL // CH):
        n = ch * CH + ar
        # digits: f(x) for the 8 nonzero points, each a base-9 digit (a1 + 3 a2)
        f1 = np.zeros((9, CH), dtype=np.int16)
        f2 = np.zeros((9, CH), dtype=np.int16)
        m = n.copy()
        for k in range(1, 9):
            dig = m % 9
            m //= 9
            f1[k] = dig % 3
            f2[k] = dig // 3
        # ---- LITERAL path: elements of (Z/9)^2, differences of all ordered pairs
        T1 = np.empty((9, CH), dtype=np.int16)
        T2 = np.empty((9, CH), dtype=np.int16)
        for k, x in enumerate(pts):
            T1[k] = (x[0] + 3 * f1[k]) % q
            T2[k] = (x[1] + 3 * f2[k]) % q
        pres = np.zeros((CH, 81), dtype=np.bool_)
        for a in range(9):
            for b in range(9):
                pres[ar, ((T1[a] - T1[b]) % q) + 9 * ((T2[a] - T2[b]) % q)] = True
        lit = pres.sum(axis=1)
        # ---- FIBRE path: F_3 arithmetic only
        cnt = {}
        inline = {}
        fib = np.ones(CH, dtype=np.int64)                        # A_0 = {0}
        for u in nz:
            mask = np.zeros(CH, dtype=np.int64)
            lam_first = None
            const = np.ones(CH, dtype=np.bool_)
            for k, x in enumerate(pts):
                j = shift[u][k]
                d1 = (f1[j] - f1[k] + cu[u][k][0]) % 3
                d2 = (f2[j] - f2[k] + cu[u][k][1]) % 3
                mask |= np.left_shift(1, (d1 + 3 * d2).astype(np.int64))
                lam = (u[0] * d2 - u[1] * d1) % 3                 # constant iff image in a line parallel to u
                if lam_first is None:
                    lam_first = lam
                else:
                    const &= (lam == lam_first)
            cnt[u] = pop[mask]
            inline[u] = const
            fib += cnt[u]
        mismatch += int((lit != fib).sum())
        hist_lit += np.bincount(lit, minlength=82)[:82]
        hist_fib += np.bincount(fib, minlength=82)[:82]
        anyline = np.zeros(CH, dtype=np.bool_)
        anytwo = np.zeros(CH, dtype=np.bool_)
        for u in nz:
            anyline |= inline[u]
            anytwo |= (cnt[u] == 2)
        hist_line += np.bincount(fib[anyline], minlength=82)[:82]
        hist_0br += np.bincount(fib[~anyline], minlength=82)[:82]
        hist_two += np.bincount(fib[anytwo], minlength=82)[:82]
        # column bound of the line-direction lemma: u with image in a line, v not in <u>
        for u in nz:
            sel = inline[u]
            if not sel.any():
                continue
            for v in nz:
                if (u[0] * v[1] - u[1] * v[0]) % 3 == 0:
                    continue
                col = np.zeros(CH, dtype=np.int64)
                for k in range(3):
                    w = ((k * u[0] + v[0]) % 3, (k * u[1] + v[1]) % 3)
                    col += cnt[w]
                col_min = min(col_min, int(col[sel].min()))
                col_checks += int(sel.sum())
        # profiles of minimisers
        mn = np.nonzero(fib == 25)[0]
        if mn.size:
            prof = np.sort(np.stack([cnt[u][mn] for u in nz], axis=1), axis=1)
            for row in prof:
                key = tuple(int(t) for t in row)
                prof_min[key] = prof_min.get(key, 0) + 1
        if ch % 9 == 8:
            print(f"    chunk {ch+1}/81  elapsed {time.time()-t0:6.1f}s", flush=True)

    def show(h):
        return {int(k): int(v) for k, v in enumerate(h) if v}

    res = dict(total=int(hist_lit.sum()), mismatch=mismatch, hist_literal=show(hist_lit), hist_fibre=show(hist_fib),
               hist_some_line_direction=show(hist_line), hist_no_line_direction=show(hist_0br),
               hist_some_2_direction=show(hist_two),
               minimiser_profiles={str(k): v for k, v in sorted(prof_min.items())},
               column_min=col_min, column_checks=col_checks, elapsed_s=round(time.time() - t0, 1))
    print("[3] p = 3 exhaustive, all 9^8 normalised f")
    print(f"    functions enumerated : {res['total']}  (expected {N_TOTAL})")
    print(f"    LITERAL vs FIBRE mismatches : {mismatch}")
    print(f"    histogram of |T-T| (LITERAL): {res['hist_literal']}")
    print(f"    histogram of |T-T| (FIBRE)  : {res['hist_fibre']}")
    dl = min(res['hist_literal'])
    df = min(res['hist_fibre'])
    print(f"    delta((Z/9)^2, 3(Z/9)^2) = {dl} (LITERAL) = {df} (FIBRE);  source: 25;  {'MATCH' if dl == df == 25 else 'MISMATCH'}")
    print(f"    number of normalised minimisers: {res['hist_literal'][dl]}")
    print("[4] p = 3 exhaustive side statistics (FIBRE path)")
    print(f"    minimiser profiles (sorted |A_u|, u != 0) : {res['minimiser_profiles']}")
    print(f"    f with some direction whose image lies in a line: {int(hist_line.sum())}; |T-T| histogram: {res['hist_some_line_direction']}")
    print(f"    f with some |A_u| = 2: {int(hist_two.sum())}; histogram: {res['hist_some_2_direction']}")
    print(f"    f with NO line direction (0-branch): {int(hist_0br.sum())}; histogram: {res['hist_no_line_direction']}")
    print(f"    column bound: min over (f, u line-direction, v not in <u>) of sum_k |A_(ku+v)| = {col_min}"
          f"  (lemma predicts >= 4p-2 = 10); checks: {col_checks}")
    print(f"    elapsed {res['elapsed_s']} s")
    if out:
        import json
        res["versions"] = dict(python=sys.version.split()[0], numpy=np.__version__)
        with open(out, "w") as fh:
            json.dump(res, fh, indent=1)
    return mismatch == 0 and dl == df == 25 and res['total'] == N_TOTAL


if __name__ == "__main__":
    ok = section1()
    ok &= section2()
    if "--skip-exhaustive" not in sys.argv:
        out = None
        for a in sys.argv[1:]:
            if a.startswith("--json="):
                out = a.split("=", 1)[1]
        ok &= section3_4(out)
    print("ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
    sys.exit(0 if ok else 1)
