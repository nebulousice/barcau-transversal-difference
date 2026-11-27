#!/usr/bin/env python3
"""check_L1.py -- step-by-step consistency check of targets/barcau-transversal-difference/PROOF.md
(line-direction lemma L1 and its consequences; Barcau-Pasol-Turcas, arXiv:2606.27961, Section 6).

This is EVIDENCE for the written proof, not a part of it: the proof in PROOF.md has no
computational step.  Everything here is exact integer arithmetic (no floats).  The script shares
no code with scripts/rows.py, scripts/rowword_search.py or the source's companion repository.

Parts (python check_L1.py PART [args]):
  algebra           the facts that do not depend on f, checked directly from the definitions for
                    p = 2, 3, 5, 7, 11: N1-N3, Lemma D (i)-(v) for every g outside H, Lemma E
                    (box total and |A_w(0)| = 2^n(w)), the last statement of Lemma G, and steps
                    (3a), (3b), (3d) for every cyclic subgroup of order p^2.
  lemmaF            Lemma F (1D cross bound), exhaustive on small (Z, K).
  p2                p = 2 sanity: all 4^3 normalised f, min |T-T| (source Cor. 5.2 says 9).
  p3class K         p = 3, COMPLETE hypothesis class, shard K in 0..3 (K = index of the first
                    line-direction subspace of f).  The steps with a label in full_check are
                    checked on every f.
  p3merge           merge the four shards and compare with scripts/out/rows_p3.json.
  stored            stored solutions: p = 3 (rowword_p3_L30.json), p = 5 extremals
                    (rowword_p5_L88_0branch.json), triangle_columns.json examples.
  random P N SEED   N random f in the hypothesis class at prime P, plus N random f outside it.

Step names in failure messages are the labels used in PROOF.md, section 6.
"""
import sys, os, json, itertools, collections, random, time, platform, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
SCRIPTS_OUT = os.path.join(os.path.dirname(HERE), "scripts", "out")


class Fail(Exception):
    pass


def need(cond, label):
    if not cond:
        raise Fail(label)


def cross(a, u, p):
    """a x u in F_p: constant on cosets a + <u>, and separates the p cosets of <u> (u != 0)."""
    return (a[0] * u[1] - a[1] * u[0]) % p


class Ctx:
    """Tables depending only on p."""

    def __init__(self, p, check_orders=True):
        self.p = p
        self.q = q = p * p
        self.P = [(a, b) for b in range(p) for a in range(p)]          # F_p^2
        self.NZ = [x for x in self.P if x != (0, 0)]
        self.REPS = [(1, m) for m in range(p)] + [(0, 1)]             # one vector per 1-dim subspace
        self.G = [(a, b) for b in range(q) for a in range(q)]          # (Z/p^2)^2
        self.H = [((p * a) % q, (p * b) % q) for b in range(p) for a in range(p)]
        for u in self.REPS:
            span = {((k * u[0]) % p, (k * u[1]) % p) for k in range(p)}
            need({a for a in self.P if cross(a, u, p) == 0} == span, "setup: a x u = 0 iff a in <u>")
            need(len({cross(a, u, p) for a in self.P}) == p, "setup: a x u takes p values")
        # cyclic subgroups C(u, r) = <[u] + p[a]>, r = a x u
        self.SUB = {}
        for u in self.REPS:
            for a in self.P:
                r = cross(a, u, p)
                g = (u[0] + p * a[0], u[1] + p * a[1])
                C = {((k * g[0]) % q, (k * g[1]) % q) for k in range(q)}
                if (u, r) in self.SUB:
                    need(self.SUB[(u, r)]["C"] == C, "setup: C depends only on the coset a + <u>")
                    continue
                # Lemma D: order p^2, C cap H = pC = iota(<u>)
                need(len(C) == q, "Lemma D: g has order p^2")
                pC = {((p * c[0]) % q, (p * c[1]) % q) for c in C}
                CH = {c for c in C if c[0] % p == 0 and c[1] % p == 0}
                iota_u = {((p * k * u[0]) % q, (p * k * u[1]) % q) for k in range(p)}
                need(pC == CH == iota_u and len(pC) == p, "Lemma D: C cap H = pC = iota(<u>)")
                need({(c[0] % p, c[1] % p) for c in C} == {((k * u[0]) % p, (k * u[1]) % p) for k in range(p)},
                     "Lemma D: pi(C) = <u>")
                # coset label of y modulo C: the functional y -> g0*y1 - g1*y0 (kernel checked = C)
                ker = {y for y in self.G if (g[0] * y[1] - g[1] * y[0]) % q == 0}
                need(ker == C, "setup: kernel of the coset functional is C")
                # M = H + C computed as a set of sums (not through (3a)); Mlab labels the cosets of M,
                # that is, the elements of Q/K, with label 0 for M itself
                M = {((h[0] + c[0]) % q, (h[1] + c[1]) % q) for h in self.H for c in C}
                Mlab = {}
                lab = 0
                for y in [(0, 0)] + self.G:
                    if y in Mlab:
                        continue
                    for m in M:
                        Mlab[((y[0] + m[0]) % q, (y[1] + m[1]) % q)] = lab
                    lab += 1
                need(len(set(Mlab.values())) == p, "step 3a: [Q:K] = p (cosets of H + C)")
                self.SUB[(u, r)] = {"g": g, "C": C, "pC": pC, "M": M, "Mlab": Mlab}
                if check_orders:
                    # step (3b): every y outside M = H + C (as a set) has j*y not in C for 1 <= j <= p
                    for y in self.G:
                        if y in M:
                            continue
                        for j in range(1, p + 1):
                            jy = ((j * y[0]) % q, (j * y[1]) % q)
                            need(jy not in C, "step 3b: order in Q outside K exceeds p")
                    # step (3d): every element of C outside pC has order > p
                    for c in C:
                        if c in pC:
                            continue
                        for j in range(1, p + 1):
                            need(((j * c[0]) % q, (j * c[1]) % q) != (0, 0), "step 3d: order in C outside pC exceeds p")
        need(len(self.SUB) == p * (p + 1), "setup: p(p+1) cyclic subgroups of order p^2")
        need(len({frozenset(s["C"]) for s in self.SUB.values()}) == p * (p + 1), "setup: subgroups distinct")


def cid(g, y, q):
    return (g[0] * y[1] - g[1] * y[0]) % q


def collinear(S, p):
    """S (a set of points of F_p^2) is contained in an affine line.  Returns (bool, direction or None)."""
    S = list(S)
    if len(S) <= 1:
        return True, None
    s0 = S[0]
    d = ((S[1][0] - s0[0]) % p, (S[1][1] - s0[1]) % p)
    for s in S[2:]:
        e = ((s[0] - s0[0]) % p, (s[1] - s0[1]) % p)
        if (e[0] * d[1] - e[1] * d[0]) % p:
            return False, None
    return True, d


def analyse(ctx, f):
    """t (section), literal fibres of T - T, the maps d_u f (from the definition with carries)."""
    p, q = ctx.p, ctx.q
    t = {x: ((x[0] + p * f[x][0]) % q, (x[1] + p * f[x][1]) % q) for x in ctx.P}
    fib = {}
    dmap = {}
    for u in ctx.P:
        fu = set()
        du = {}
        for x in ctx.P:
            y0 = x[0] + u[0]
            y1 = x[1] + u[1]
            c0 = -1 if y0 >= p else 0                                  # carry c_u(x), coordinates 0 or -1
            c1 = -1 if y1 >= p else 0
            y = (y0 % p, y1 % p)
            ty = t[y]
            tx = t[x]
            fu.add(((ty[0] - tx[0]) % q, (ty[1] - tx[1]) % q))         # literal difference in (Z/p^2)^2
            du[x] = ((f[y][0] - f[x][0] + c0) % p, (f[y][1] - f[x][1] + c1) % p)
        fib[u] = fu
        dmap[u] = du
    return t, fib, dmap


def line_classes(ctx, dmap):
    """Indices k of the subspaces <REPS[k]> all of whose nonzero vectors w have A_w in a line.
    Also checks Corollary L1c: collinearity of A_w is constant along <u> minus 0."""
    p = ctx.p
    res = []
    for k, u in enumerate(ctx.REPS):
        flags = []
        for m in range(1, p):
            w = ((m * u[0]) % p, (m * u[1]) % p)
            flags.append(collinear(set(dmap[w].values()), p)[0])
        need(all(flags) or not any(flags), "Cor L1c: line directions come in whole subspaces")
        if flags[0]:
            res.append(k)
    return res


def full_check(ctx, f, st, t=None, fib=None, dmap=None, lines=None):
    """Check every step of PROOF.md on f.  Raises Fail(label) on the first failed step."""
    p, q = ctx.p, ctx.q
    if t is None:
        t, fib, dmap = analyse(ctx, f)
    if lines is None:
        lines = line_classes(ctx, dmap)
    A = {u: set(dmap[u].values()) for u in ctx.P}
    # Lemma A (source Lemma 6.1)
    D = set()
    for u in ctx.P:
        need(fib[u] == {((u[0] + p * a[0]) % q, (u[1] + p * a[1]) % q) for a in A[u]}, "Lemma A: fibre = [u] + iota(A_u)")
        need(len(fib[u]) == len(A[u]), "Lemma A: fibre size")
        D |= fib[u]
    Dlit = {((t[y][0] - t[x][0]) % q, (t[y][1] - t[x][1]) % q) for x in ctx.P for y in ctx.P}
    need(D == Dlit, "Lemma A: union of fibres is T - T")
    total = len(Dlit)
    need(total == sum(len(A[u]) for u in ctx.P), "Lemma A: |T-T| = sum |A_u|")
    need(A[(0, 0)] == {(0, 0)}, "Lemma A: A_0 = {0}")
    need(total % 2 == 1 or p == 2, "parity: |T-T| odd")
    # Lemma B (cycle identity)
    for u in ctx.NZ:
        du = dmap[u]
        for x in ctx.P:
            s0 = s1 = 0
            y = x
            for _ in range(p):
                s0 += du[y][0]
                s1 += du[y][1]
                y = ((y[0] + u[0]) % p, (y[1] + u[1]) % p)
            need((s0 + u[0]) % p == 0 and (s1 + u[1]) % p == 0, "Lemma B: cycle identity")
    # Lemma C: a line containing A_u is parallel to u
    for u in ctx.NZ:
        ok, d = collinear(A[u], p)
        if ok:
            need(len(A[u]) >= 2, "Lemma C: |A_u| >= 2")
            need(cross(d, u, p) == 0, "Lemma C: line parallel to u")
    # Lemma G: for EVERY cyclic subgroup C(u, r): T in p cosets of C  <=>  A_u in the coset {a x u = r}
    for (u, r), S in ctx.SUB.items():
        g = S["g"]
        ncos = len({cid(g, t[x], q) for x in ctx.P})
        inside = all(cross(a, u, p) == r for a in A[u])
        need((ncos == p) == inside, "Lemma G: p-coset cover <=> A_u in a + <u>")
        need(ncos >= p, "Lemma G: at least p cosets")
        st["min_cosets"] = min(st.get("min_cosets", ncos), ncos)
    # 0-branch bound (used in C1)
    if not lines:
        need(all(len(A[u]) >= 3 for u in ctx.NZ), "C1: no line direction => all |A_u| >= 3")
        need(total >= 3 * p * p - 2, "C1: 0-branch total >= 3p^2 - 2")
        st["zero_branch"] = st.get("zero_branch", 0) + 1
        st["zero_branch_min_total"] = min(st.get("zero_branch_min_total", total), total)
        return total, lines
    # main argument, for every line-direction subspace
    for k in lines:
        u = ctx.REPS[k]
        a0 = next(iter(A[u]))
        r = cross(a0, u, p)
        S = ctx.SUB[(u, r)]
        g, C, pC, Mlab = S["g"], S["C"], S["pC"], S["Mlab"]
        need(g[0] % p == u[0] and g[1] % p == u[1], "step 1: pi(g) = u")
        # step 1: t(x+u) - t(x) in g + pC
        gpC = {((g[0] + c[0]) % q, (g[1] + c[1]) % q) for c in pC}
        need(fib[u] <= gpC, "step 1: fibre over u inside g + pC")
        # step 2: chains in single cosets; exactly p cosets, each a u-line
        chains = collections.defaultdict(list)
        for x in ctx.P:
            chains[cid(g, t[x], q)].append(x)
        need(len(chains) == p, "step 2: exactly p cosets of C")
        for xs in chains.values():
            need(len(xs) == p and len({cross(x, u, p) for x in xs}) == 1, "step 2: each coset holds one u-line")
        # step 3c: Y is a transversal of Q/K, with classes computed as cosets of the set M = H + C
        need(len({Mlab[t[xs[0]]] for xs in chains.values()}) == p, "step 3c: Y transversal of Q/K")
        # step 3d: A_n transversal of C/pC
        An = {}
        for z, xs in chains.items():
            tau = t[xs[0]]
            S_n = {((t[x][0] - tau[0]) % q, (t[x][1] - tau[1]) % q) for x in xs}
            need(S_n <= C, "step 3d: A_n inside C")
            need(len({(s[0] % p, s[1] % p) for s in S_n}) == p, "step 3d: A_n transversal of C/pC")
            An[z] = (tau, S_n, xs)
        # Lemma F on (C, pC, A_n, A_n')
        for z1, (tau1, S1, xs1) in An.items():
            for z2, (tau2, S2, xs2) in An.items():
                dd = collections.defaultdict(set)
                for s1 in S1:
                    for s2 in S2:
                        e = ((s1[0] - s2[0]) % q, (s1[1] - s2[1]) % q)
                        dd[(e[0] % p, e[1] % p)].add(e)
                need(len(dd) == p, "Lemma F (C): p residue fibres")
                need(sum(1 for v in dd.values() if len(v) == 1) <= 1, "Lemma F (C): at most one singleton fibre")
                size = sum(len(v) for v in dd.values())
                need(size >= 2 * p - 1, "Lemma F (C): |A_n - A_n'| >= 2p-1")
                st["min_cross_C"] = min(st.get("min_cross_C", size), size)
        # Lemma F on (Q, K, Y, Y)
        yfib = collections.defaultdict(set)
        for z1, (tau1, S1, xs1) in An.items():
            for z2, (tau2, S2, xs2) in An.items():
                e = ((tau1[0] - tau2[0]) % q, (tau1[1] - tau2[1]) % q)
                yfib[Mlab[e]].add(cid(g, e, q))                          # class in Q/K from the set M
        need(len(yfib) == p, "Lemma F (Q): p residue fibres")
        need(yfib[0] == {0}, "Lemma F (Q): zero fibre is {0}")
        need(all(len(yfib[rr]) >= 2 for rr in range(1, p)), "Lemma F (Q): nonzero fibres have >= 2 elements")
        YY = set().union(*yfib.values())
        need(len(YY) >= 2 * p - 1, "Lemma F (Q): |Y - Y| >= 2p-1")
        st["min_YY"] = min(st.get("min_YY", len(YY)), len(YY))
        # step 5: T - T meets exactly the cosets in Y - Y, each in >= 2p-1 elements
        cnt = collections.Counter(cid(g, d, q) for d in Dlit)
        need(set(cnt) == YY, "step 5: rho(T-T) = Y - Y")
        mc = min(cnt.values())
        need(mc >= 2 * p - 1, "step 5: each coset of C in Y-Y holds >= 2p-1 differences")
        st["min_per_coset"] = min(st.get("min_per_coset", mc), mc)
        need(total >= (2 * p - 1) ** 2, "L1(a): |T-T| >= (2p-1)^2")
        # L1(b): columns
        col = collections.Counter()
        for w in ctx.P:
            col[cross(w, u, p)] += len(A[w])
        need(col[0] >= 2 * p - 1, "L1(b): zero column >= 2p-1")
        for rr in range(1, p):
            need(col[rr] >= 4 * p - 2, "L1(b): column >= 4p-2")
            st["min_column"] = min(st.get("min_column", col[rr]), col[rr])
            st["column_checks"] = st.get("column_checks", 0) + 1
    st["line_f"] = st.get("line_f", 0) + 1
    st["line_min_total"] = min(st.get("line_min_total", total), total)
    return total, lines


def hypothesis_class(ctx, k, r):
    """All f with f(0) = 0 and A_u(f) inside the coset {a : a x u = r}, u = REPS[k].  Each once."""
    p = ctx.p
    u = ctx.REPS[k]
    v = (0, 1) if u != (0, 1) else (1, 0)
    a = next(b for b in ctx.P if cross(b, u, p) == r)
    letters = [((a[0] + m * u[0]) % p, (a[1] + m * u[1]) % p) for m in range(p)]
    lines = [[((n * v[0] + i * u[0]) % p, (n * v[1] + i * u[1]) % p) for i in range(p)] for n in range(p)]
    need(len({x for L in lines for x in L}) == p * p, "enumeration: lines partition the plane")
    offs_choices = [[(0, 0)]] + [ctx.P] * (p - 1)
    for offs in itertools.product(*offs_choices):
        for words in itertools.product(itertools.product(letters, repeat=p - 1), repeat=p):
            f = {}
            for n in range(p):
                L = lines[n]
                cur = offs[n]
                f[L[0]] = cur
                for i in range(p - 1):
                    x = L[i]
                    c0 = -1 if x[0] + u[0] >= p else 0
                    c1 = -1 if x[1] + u[1] >= p else 0
                    d = words[n][i]
                    cur = ((cur[0] + d[0] - c0) % p, (cur[1] + d[1] - c1) % p)   # f(x+u) = f(x) + d - c_u(x)
                    f[L[i + 1]] = cur
            yield f


def random_in_class(ctx, rng, small_alphabet):
    p = ctx.p
    k = rng.randrange(p + 1)
    u = ctx.REPS[k]
    v = (0, 1) if u != (0, 1) else (1, 0)
    a = rng.choice(ctx.P)
    ms = list(range(p))
    if small_alphabet:
        ms = rng.sample(ms, rng.choice([2, 2, 3]))
    letters = [((a[0] + m * u[0]) % p, (a[1] + m * u[1]) % p) for m in ms]
    f = {}
    for n in range(p):
        L = [((n * v[0] + i * u[0]) % p, (n * v[1] + i * u[1]) % p) for i in range(p)]
        while True:
            w = [rng.choice(letters) for _ in range(p - 1)]
            last = ((-u[0] - sum(d[0] for d in w)) % p, (-u[1] - sum(d[1] for d in w)) % p)
            if last in letters or not small_alphabet:
                break
        cur = (0, 0) if n == 0 else rng.choice(ctx.P)
        f[L[0]] = cur
        for i in range(p - 1):
            x = L[i]
            c0 = -1 if x[0] + u[0] >= p else 0
            c1 = -1 if x[1] + u[1] >= p else 0
            cur = ((cur[0] + w[i][0] - c0) % p, (cur[1] + w[i][1] - c1) % p)
            f[L[i + 1]] = cur
    return f


def part_algebra(log):
    """Facts that do not depend on f, from the definitions (sets of residues, literal multiples)."""
    for p in (2, 3, 5, 7, 11):
        q = p * p
        ctx = Ctx(p, check_orders=False)
        G, P = ctx.G, ctx.P
        Hset = set(ctx.H)

        def add(a, b):
            return ((a[0] + b[0]) % q, (a[1] + b[1]) % q)

        def mul(k, a):
            return ((k * a[0]) % q, (k * a[1]) % q)

        def pi(y):
            return (y[0] % p, y[1] % p)

        def span(w):
            return {((k * w[0]) % p, (k * w[1]) % p) for k in range(p)}

        # N1: iota(a) = p*m mod p^2 for every integer lift m of a (lifts a + p*k, k in [-2, p-1]^2)
        iota = {}
        for a in P:
            vals = {((p * (a[0] + p * i)) % q, (p * (a[1] + p * j)) % q) for i in range(-2, p) for j in range(-2, p)}
            need(len(vals) == 1, "N1: iota well defined")
            iota[a] = vals.pop()
        need(iota == {a: ((p * a[0]) % q, (p * a[1]) % q) for a in P}, "N1: iota(a) = p[a]")
        for a in P:
            for b in P:
                need(iota[((a[0] + b[0]) % p, (a[1] + b[1]) % p)] == add(iota[a], iota[b]), "N1: iota additive")
        need(len(set(iota.values())) == p * p and set(iota.values()) == Hset, "N1: iota injective, image H")
        need(Hset == {y for y in G if pi(y) == (0, 0)}, "setup: H = ker pi")
        # N2, N3 (order = number of distinct multiples)
        order = {y: len({mul(k, y) for k in range(q)}) for y in G}
        for y in G:
            need(mul(p, y) == iota[pi(y)], "N2: pg = iota(pi(g))")
            need((mul(p, y) == (0, 0)) == (y in Hset), "N2: pg = 0 iff g in H")
            if y not in Hset:
                need(order[y] == q, "N3: order p^2 outside H")
        # Lemma D (i)-(iv) for every g outside H; (v) once for each subgroup obtained
        subs = set()
        for g in G:
            if g in Hset:
                continue
            u = pi(g)
            C = {mul(k, g) for k in range(q)}
            pC = {mul(p, c) for c in C}
            need(len(C) == q, "Lemma D (i): |C| = p^2")
            need({pi(c) for c in C} == span(u), "Lemma D (ii): pi(C) = <u>")
            need(C & Hset == pC == {iota[w] for w in span(u)} and len(pC) == p, "Lemma D (iii): C cap H = pC = iota(<u>)")
            need({c for c in C if pi(c) == u} == {add(g, c) for c in pC}, "Lemma D (iv): C cap pi^-1(u) = g + pC")
            fc = frozenset(C)
            if fc not in subs:
                subs.add(fc)
                need(all(order[c] == q for c in C - pC), "Lemma D (v): order p^2 on C minus pC")
        need(subs == {frozenset({mul(k, y) for k in range(q)}) for y in G if order[y] == q}, "setup: cyclic subgroups")
        need(subs == {frozenset(S["C"]) for S in ctx.SUB.values()} and len(subs) == p * (p + 1),
             "setup: the p(p+1) subgroups C(u, r) are all cyclic subgroups of order p^2")
        # last statement of Lemma G: every cyclic C' of order p^2 equals <[w] + iota(a')> for every nonzero
        # w in pi(C') and a suitable a'; and for no other w
        gen_of = {}
        for w in ctx.NZ:
            for a in P:
                gen_of.setdefault(frozenset({mul(k, add(w, iota[a])) for k in range(q)}), set()).add(w)
        for C in subs:
            need(gen_of.get(C, set()) == {pi(c) for c in C} - {(0, 0)}, "Lemma G (last statement)")
        # (3a), (3b), (3d) for every cyclic subgroup, with sets only
        for (u, r), S in ctx.SUB.items():
            C, pC, M, Mlab = S["C"], S["pC"], S["M"], S["Mlab"]
            need(M == {y for y in G if pi(y) in span(u)}, "step 3a: H + C = pi^-1(<u>)")
            Qlab = {}                                                   # Q = G/C: cosets of C
            lab = 0
            for y in G:
                if y not in Qlab:
                    for c in C:
                        Qlab[add(y, c)] = lab
                    lab += 1
            need(len(set(Qlab.values())) == q, "step 3a: |Q| = p^2")
            K = {Qlab[h] for h in Hset}                                 # K = rho(H)
            need(len(K) == p, "step 3a: |K| = p")
            need({y for y in G if Qlab[y] in K} == M, "step 3a: ker(kappa rho) = M")
            theta = {}
            for y in G:
                W = frozenset(((pi(y)[0] + w[0]) % p, (pi(y)[1] + w[1]) % p) for w in span(u))
                need(theta.setdefault(Mlab[y], W) == W, "step 3a: theta well defined")
            need(len(set(theta.values())) == p, "step 3a: theta bijective")
            for y in G:                                                 # (3b): rho(y) outside K has order > p
                if Qlab[y] in K:
                    continue
                need(all(mul(j, y) not in C for j in range(1, p + 1)), "step 3b: order in Q outside K exceeds p")
            cos = {frozenset(add(c, d) for d in pC) for c in C}         # (3d)
            need(len(cos) == p, "step 3d: [C:pC] = p")
            need(all(len({pi(c) for c in X}) == 1 for X in cos), "step 3d: cosets of pC have one image under pi")
        # Lemma E: box total by literal subtraction; |A_w(0)| = 2^n(w) from the carry definition
        box = {((x[0] - y[0]) % q, (x[1] - y[1]) % q) for x in P for y in P}
        need(len(box) == (2 * p - 1) ** 2, "Lemma E: |T_0 - T_0| = (2p-1)^2")
        for w in P:
            Aw = {((-1 if x[0] + w[0] >= p else 0) % p, (-1 if x[1] + w[1] >= p else 0) % p) for x in P}
            need(len(Aw) == 2 ** ((w[0] != 0) + (w[1] != 0)), "Lemma E: |A_w(0)| = 2^n(w)")
        log(f"  p={p}: N1, N2, N3 on all {q * q} elements of G; Lemma D (i)-(iv) for all {q * q - q} g outside H; "
            f"{len(subs)} cyclic subgroups of order p^2: Lemma D (v), Lemma G (last statement), steps 3a, 3b, 3d; "
            f"Lemma E: box {len(box)} = (2p-1)^2, |A_w(0)| = 2^n(w) for all {p * p} w")
    return True


def part_lemmaF(log):
    """Lemma F: Z abelian, K of index q, A, B transversals, every element outside K of order > q
    => at most one residue fibre of A - B is a singleton, and |A - B| >= 2q - 1."""
    def run(mod, kgen, normalise):
        # Z = Z/mod, K = <kgen>
        K = sorted({(kgen * i) % mod for i in range(mod)})
        qq = mod // len(K)
        hyp = True
        for e in range(mod):
            if e in K:
                continue
            order = next(j for j in range(1, mod + 1) if (j * e) % mod == 0)
            if order <= qq:
                hyp = False
        cosets = [[(r + k) % mod for k in K] for r in range(qq)]
        firsts = [[c[0]] for c in cosets] if normalise else cosets
        best = None
        viol = 0
        pairs = 0
        for A in itertools.product(*([firsts[0]] + cosets[1:])) if normalise else itertools.product(*cosets):
            for B in itertools.product(*([firsts[0]] + cosets[1:])) if normalise else itertools.product(*cosets):
                pairs += 1
                fibs = collections.defaultdict(set)
                for x in A:
                    for y in B:
                        e = (x - y) % mod
                        fibs[e % qq].add(e)
                size = sum(len(s) for s in fibs.values())
                single = sum(1 for s in fibs.values() if len(s) == 1)
                best = size if best is None else min(best, size)
                if hyp and (size < 2 * qq - 1 or single > 1):
                    viol += 1
        return qq, hyp, pairs, best, viol

    ok = True
    for mod, kgen, normalise in [(1, 0, False), (4, 2, False), (9, 3, False), (8, 2, False), (25, 5, True),
                                 (27, 3, False), (16, 2, False), (6, 3, False), (8, 4, False)]:
        qq, hyp, pairs, best, viol = run(mod, kgen, normalise)
        line = (f"  Z=Z/{mod} K=<{kgen}> index q={qq} hypothesis(order>q outside K)={hyp} "
                f"pairs={pairs}{' (A,B normalised: translation does not change |A-B|)' if normalise else ''} "
                f"min|A-B|={best} bound 2q-1={2 * qq - 1} violations={viol}")
        log(line)
        if hyp and viol:
            ok = False
    log("  (rows with hypothesis=False are outside Lemma F and are listed only to show that the hypothesis matters)")
    return ok


def part_p2(log):
    ctx = Ctx(2)
    st = {}
    hist = collections.Counter()
    for vals in itertools.product(ctx.P, repeat=3):
        f = {(0, 0): (0, 0)}
        for x, v in zip(ctx.NZ, vals):
            f[x] = v
        total, lines = full_check(ctx, f, st)
        hist[(total, len(lines))] += 1
    log(f"  p=2: 64 normalised f; histogram (|T-T|, number of line-direction subspaces): {dict(sorted(hist.items()))}")
    log(f"  p=2: min |T-T| = {min(k[0] for k in hist)} (source Cor. 5.2, r = 2: 9); stats {st}")
    return min(k[0] for k in hist) == 9


def part_p3class(K, log):
    ctx = Ctx(3)
    st = {}
    hist = collections.Counter()
    nlines_hist = collections.Counter()
    constructed = 0
    t0 = time.time()
    for r in range(3):
        for f in hypothesis_class(ctx, K, r):
            constructed += 1
            t, fib, dmap = analyse(ctx, f)
            lines = line_classes(ctx, dmap)
            need(K in lines, "enumeration: constructed f has the line direction")
            if lines[0] != K:
                continue                      # counted in an earlier shard
            total, lines = full_check(ctx, f, st, t, fib, dmap, lines)
            hist[total] += 1
            nlines_hist[len(lines)] += 1
    res = {"p": 3, "shard": K, "constructed": constructed, "distinct_first_here": sum(hist.values()),
           "hist_total": {str(k): v for k, v in sorted(hist.items())},
           "line_subspaces_hist": {str(k): v for k, v in sorted(nlines_hist.items())},
           "stats": st, "elapsed_s": round(time.time() - t0, 1), "python": sys.version.split()[0]}
    json.dump(res, open(os.path.join(OUT, f"p3class_{K}.json"), "w"), indent=1)
    log(f"  p=3 shard {K}: constructed={constructed} processed={res['distinct_first_here']} hist={res['hist_total']} "
        f"stats={st} elapsed={res['elapsed_s']}s")
    return True


def part_p3merge(log):
    hist = collections.Counter()
    nl = collections.Counter()
    st = {}
    constructed = 0
    cc = 0
    for K in range(4):
        r = json.load(open(os.path.join(OUT, f"p3class_{K}.json")))
        constructed += r["constructed"]
        for k, v in r["hist_total"].items():
            hist[int(k)] += v
        for k, v in r["line_subspaces_hist"].items():
            nl[int(k)] += v
        for k, v in r["stats"].items():
            if k in ("line_f", "column_checks"):
                st[k] = st.get(k, 0) + v
            else:
                st[k] = min(st.get(k, v), v)
    ref = json.load(open(os.path.join(SCRIPTS_OUT, "rows_p3.json")))
    ref_hist = {int(k): v for k, v in ref["hist_some_line_direction"].items()}
    distinct = sum(hist.values())
    log(f"  p=3 complete hypothesis class: constructed (with repeats) = {constructed}; distinct f = {distinct}")
    log(f"  histogram of |T-T| over the class     : {dict(sorted(hist.items()))}")
    log(f"  rows_p3.json hist_some_line_direction : {dict(sorted(ref_hist.items()))}")
    log(f"  number of line-direction subspaces    : {dict(sorted(nl.items()))}")
    log(f"  stats (minima over the class)         : {st}")
    log(f"  rows_p3.json column_min={ref['column_min']} column_checks={ref['column_checks']}")
    same = dict(hist) == ref_hist and distinct == sum(ref_hist.values())
    cols = st.get("min_column") == ref["column_min"] == 10
    log(f"  histogram identical to the exhaustive scan: {same};  column minimum 10 = 4p-2 in both: {cols};  "
        f"column checks here (f, line subspace, nonzero column) = {st.get('column_checks')}")
    summary = {"constructed": constructed, "distinct": distinct, "hist_total": {str(k): v for k, v in sorted(hist.items())},
               "line_subspaces_hist": {str(k): v for k, v in sorted(nl.items())}, "stats": st,
               "matches_rows_p3_hist": same, "matches_rows_p3_columns": cols}
    json.dump(summary, open(os.path.join(OUT, "p3class_merged.json"), "w"), indent=1)
    return same and st.get("min_column") == ref["column_min"] == 10


def part_stored(log):
    ok = True
    # p = 3 stored solutions (totals 25, 27, 29 < 31: all must have a line direction)
    rep = json.load(open(os.path.join(SCRIPTS_OUT, "rowword_p3_L30.json")))
    ctx = Ctx(3)
    st = {}
    hist = collections.Counter()
    for s in rep["solutions"]:
        F = s["f"]
        f = {(i, j): (F[j][i] % 3, F[j][i] // 3) for i in range(3) for j in range(3)}
        total, lines = full_check(ctx, f, st)
        need(total == s["total"], "stored p=3: total recount")
        hist[(total, len(lines))] += 1
    log(f"  rowword_p3_L30.json: {len(rep['solutions'])} solutions; (|T-T|, line subspaces): {dict(sorted(hist.items()))}; stats {st}")
    ok &= all(k[1] >= 1 for k in hist)
    # p = 5 extremals of the 0-branch
    rep = json.load(open(os.path.join(SCRIPTS_OUT, "rowword_p5_L88_0branch.json")))
    ctx = Ctx(5)
    st = {}
    hist = collections.Counter()
    for s in rep["solutions"]:
        F = s["f"]
        f = {(i, j): (F[j][i] % 5, F[j][i] // 5) for i in range(5) for j in range(5)}
        total, lines = full_check(ctx, f, st)
        need(total == s["total"], "stored p=5: total recount")
        hist[(total, len(lines))] += 1
    log(f"  rowword_p5_L88_0branch.json: {len(rep['solutions'])} solutions; (|T-T|, line subspaces): {dict(sorted(hist.items()))}; "
        f"stats {st}  [3p^2-2 = 73, (2p-1)^2 = 81; least number of cosets of a cyclic C of order 25 covering T = {st.get('min_cosets')}]")
    ok &= set(hist) == {(87, 0)}
    # the box f = 0 and the corner-moved box at p = 5
    st = {}
    f = {x: (0, 0) for x in ctx.P}
    total, lines = full_check(ctx, f, st)
    log(f"  p=5 box f=0: |T-T|={total}, line subspaces={len(lines)}, stats {st}")
    ok &= total == 81
    st = {}
    f = {x: (0, 0) for x in ctx.P}
    f[(4, 4)] = (4, 4)
    total, lines = full_check(ctx, f, st)
    log(f"  p=5 box with one corner moved (f(4,4) = (-1,-1)): |T-T|={total}, line subspaces={len(lines)}, stats {st}")
    # triangle_columns.json examples
    for ex in json.load(open(os.path.join(SCRIPTS_OUT, "triangle_columns.json"))):
        p = ex["p"]
        ctx = Ctx(p)
        st = {}
        F = ex["f"]
        f = {(i, j): tuple(F[j][i]) for i in range(p) for j in range(p)}
        total, lines = full_check(ctx, f, st)
        need(total == ex["total"], "stored triangle_columns: total recount")
        log(f"  triangle_columns.json p={p}: |T-T|={total} (box {(2 * p - 1) ** 2}), line subspaces={[ctx.REPS[k] for k in lines]}, stats {st}")
        ok &= (not lines) or total >= (2 * p - 1) ** 2
    return ok


def part_random(p, N, seed, log):
    rng = random.Random(seed)
    ctx = Ctx(p, check_orders=(p <= 7))
    st = {}
    hist = collections.Counter()
    t0 = time.time()
    for i in range(N):
        f = random_in_class(ctx, rng, small_alphabet=(i % 2 == 0))
        total, lines = full_check(ctx, f, st)
        need(lines, "random: constructed f has a line direction")
        hist[total] += 1
    mn = min(hist)
    log(f"  p={p} seed={seed}: {N} random f in the hypothesis class: min |T-T|={mn} (box {(2 * p - 1) ** 2}); stats {st}")
    st2 = {}
    for i in range(N):
        f = {x: rng.choice(ctx.P) for x in ctx.P}
        full_check(ctx, f, st2)
    log(f"  p={p} seed={seed}: {N} uniformly random f (Lemmas A, B, C, G and the 0-branch count): stats {st2}; elapsed {time.time() - t0:.1f}s")
    return mn >= (2 * p - 1) ** 2


def main():
    os.makedirs(OUT, exist_ok=True)
    part = sys.argv[1]
    name = "_".join(sys.argv[1:])
    lines = []

    def log(s):
        print(s, flush=True)
        lines.append(s)

    sha = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()[:16]
    log(f"check_L1.py {' '.join(sys.argv[1:])}   (python {sys.version.split()[0]}, {platform.python_implementation()}, "
        f"{platform.system()} {platform.release()}; standard library only; check_L1.py sha256 {sha}...)")
    try:
        if part == "algebra":
            ok = part_algebra(log)
        elif part == "lemmaF":
            ok = part_lemmaF(log)
        elif part == "p2":
            ok = part_p2(log)
        elif part == "p3class":
            ok = part_p3class(int(sys.argv[2]), log)
        elif part == "p3merge":
            ok = part_p3merge(log)
        elif part == "stored":
            ok = part_stored(log)
        elif part == "random":
            ok = part_random(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), log)
        else:
            raise SystemExit("unknown part")
        log("RESULT: " + ("ALL CHECKS PASS" if ok else "MISMATCH (see above)"))
    except Fail as e:
        log(f"RESULT: STEP FAILED -> {e}")
        ok = False
    open(os.path.join(OUT, f"check_{name}.log"), "w").write("\n".join(lines) + "\n")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
