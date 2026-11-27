# A line-direction lemma for the odd square-plane conjecture of Barcau, Paşol and Ţurcaş: full proof

*Written 2026-11-27. This is a cleaned, self-contained copy of the proof at commit `1c9f155` of the private working repository (blob `ab179d2387df`), which is the version revised after review round 1. The mathematics of §§1–5 is unchanged from that version. Names were changed (see "Names" below), pipeline references were removed, some sentences were split for readability, and the proof of step (3b) now says in one extra sentence why $y\notin M$.*

**Status.** Every argument in §§1–5 is written in full, and no step is left open. Every step carries the status word `proposed`: written, but not yet accepted under our review rule. Review round 1 is done (one referee accepted with zero issues; the other found one minor issue, which is fixed). Review round 2, with three referees, is pending. **Expert verification required.** Verified so far with: AI referees in review round 1 (Claude Opus 5.5, line by line: one minor issue about the description of the checking script, no mathematical error, issue fixed; Claude Fable, adversarial: accept with zero issues), with round 2 pending; outside AI cross-checks by ChatGPT and Gemini (no mathematical error or gap found); and exact-arithmetic computer checks, which are evidence only. Nothing is formalized in Lean 4 with Mathlib. The machine checks of §7 are `numerical` evidence; **the proof has no computational step**, and no argument depends on them. We claim no priority or novelty (§9).

**Status words** used in this repository: `proved` (a complete argument that passed our two-referee review rule), `certified` (a rigorous computation reproduced by an independent second implementation), `numerical` (finite or floating-point evidence), `proposed` (written but not yet accepted by review).

**Names.** The scripts and logs in `scripts/` use short internal labels. They are: `L1` for Theorem 1, `C1` for Corollary 2, `Cor L1c` for the last sentence of Theorem 1 (c), and `N1`, `N2`, `N3` for Facts 1, 2, 3. The check runs of §7 are called Run 0 to Run 6.

## 0. Summary

**Source.** M. Barcau, V. Paşol and G. C. Ţurcaş, *Transversal Difference Numbers in Finite Abelian Quotients*, [arXiv:2606.27961v1](https://arxiv.org/abs/2606.27961) (submitted 2026-06-26; the only version on 2026-11-27), §6. We read the [HTML version](https://arxiv.org/html/2606.27961v1) on 2026-11-27. Its Conjecture 6.2 says that for every odd prime $p$ the transversal difference number of $(\mathbb{Z}/p^2\mathbb{Z})^2$ modulo $p(\mathbb{Z}/p^2\mathbb{Z})^2$ equals $(2p-1)^2$. All terms are defined in §1.

| Result | Statement (short) | Status |
| --- | --- | --- |
| Theorem 1 (line-direction lemma) | If, for some nonzero $u$, the set $A_u(f)$ lies in an affine line, then $\lvert T_f-T_f\rvert\ge(2p-1)^2$. Moreover every column sum next to $u$ is at least $4p-2$, and $T_f$ is covered by $p$ cosets of a cyclic subgroup of order $p^2$ | `proposed` (complete argument, §4) |
| Corollary 2 | $\delta\ge3p^2-2$ for every odd prime $p$ (the source proves $3p^2-p-1$) | `proposed` (complete argument, §5) |
| Corollary 3 | Conjecture 6.2 at $p$ is equivalent to the same inequality for the functions $f$ with no line direction | `proposed` (complete argument, §5) |
| Corollary 4 | $\delta=25$ at $p=3$, with no computation | `proposed` (complete argument, §5) |

**Credit first.** The inequality of Theorem 1 (a) was posted publicly earlier on the same day, 2026-11-27, by Robert Leshner with Codex, in [open-math-agents pull request #6492](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/6492) (opened 12:56 UTC; [README at commit `ba804a2`](https://github.com/rleshner/open-math-agents/blob/ba804a2813650e214c5172a1f484b1c1eda5edd8/research/transversal-seven/README.md), section "A projection bound for every odd prime"). Our work was done independently and was posted later the same day. Their proof uses a basis change, a shear, a projection onto a cyclic transversal and Kneser's theorem; ours avoids Kneser's theorem through the two-transversal Lemma F. Their lemma, with the count of §5, also gives Corollaries 2–4. The same pull request claims a computer-assisted proof that $\delta=169$ at $p=7$, which we have not checked. We claim no priority for Theorem 1 (a) or for any corollary. Corollaries 2 and 4 were also within reach of earlier work: the source verifies $\delta=25$ at $p=3$ by computer, and the unpublished automath notes state them as consequences of a special case of Theorem 1 (§9).

**Idea of the proof of Theorem 1.** Suppose $A_u(f)$ lies in an affine line. A short identity (Lemma B) forces that line to be parallel to $u$. This says exactly that every step $t(x+u)-t(x)$ of the transversal lies in one cyclic subgroup $C$ of order $p^2$. So $T$ is a union of $p$ "chains", each inside one coset of $C$. The $p$ cosets form a transversal of a quotient of order $p$, and each chain is a transversal of $C$ modulo its subgroup of order $p$. An elementary one-dimensional bound (Lemma F: two such transversals have at least $2p-1$ differences) is then used twice. It shows that $T-T$ meets at least $2p-1$ cosets of $C$, and that it has at least $2p-1$ elements in each of them.

## 1. Setting, notation, conventions

Notation follows §6.1 of the source.

- $p$ is a prime. In all statements it is odd, as in §6 of the source. (Oddness is never used in the proofs; see §4.5.)
- $\mathbb{F}_p=\mathbb{Z}/p\mathbb{Z}$ is the field with $p$ elements, and $\mathbb{F}_p^2$ is the plane over it.
- $G=G_p=(\mathbb{Z}/p^2\mathbb{Z})^2$, an abelian group of order $p^4$, and $H=H_p=pG$, its subgroup of order $p^2$.
- $\pi:G\to\mathbb{F}_p^2$ is coordinatewise reduction modulo $p$. It is a surjective homomorphism with kernel $H$: a pair of residues modulo $p^2$ reduces to $0$ modulo $p$ exactly when both are multiples of $p$. So $G/H$ is identified with $\mathbb{F}_p^2$.
- A **transversal** for $G/H$ is a set $T\subseteq G$ that contains exactly one element of each coset of $H$; equivalently, $\pi$ restricted to $T$ is a bijection onto $\mathbb{F}_p^2$. A transversal has $p^2$ elements.
- The **difference set** of $T$ is $T-T=\lbrace t-t':t,t'\in T\rbrace$. The **transversal difference number** is $\delta(G,H)=\min_T\lvert T-T\rvert$, the minimum over all transversals $T$.
- For $x\in\mathbb{F}_p^2$, $[x]\in\lbrace0,1,\dots,p-1\rbrace^2\subseteq\mathbb{Z}^2$ is the coordinatewise **standard lift**. The same symbol denotes its class in $G$.
- $\iota:\mathbb{F}_p^2\to G$ is defined by $\iota(a)=pm \bmod p^2$, where $m\in\mathbb{Z}^2$ is any integer vector with $m\equiv a \pmod p$. (The source writes $p[a]$.)
- For a function $f:\mathbb{F}_p^2\to\mathbb{F}_p^2$, put $t_f(x)=[x]+\iota(f(x))\in G$ and $T_f=\lbrace t_f(x):x\in\mathbb{F}_p^2\rbrace$. We write $t$ for $t_f$ when $f$ is fixed.
- For $u,x\in\mathbb{F}_p^2$, the **carry** $c_u(x)$, the **corrected difference** $d_uf(x)$ and its **image** $A_u(f)$ are

```math
c_u(x)=\frac{[x+u]-[x]-[u]}{p}\in\mathbb{F}_p^2,\qquad d_uf(x)=f(x+u)-f(x)+c_u(x),\qquad A_u(f)=\{d_uf(x):x\in\mathbb{F}_p^2\}.
```

  The numerator of $c_u(x)$ is computed in $\mathbb{Z}^2$. Its coordinates are $0$ or $-p$, and the quotient is then read modulo $p$, so each coordinate of $c_u(x)$ is $0$ or $-1$.

- For $s\in\mathbb{F}_p^2$, $\langle s\rangle=\lbrace\lambda s:\lambda\in\mathbb{F}_p\rbrace$. An **affine line** is a set $a+\langle s\rangle$ with $s\ne0$; it has $p$ points. For $u\ne0$, a **$u$-line** is a coset $x+\langle u\rangle$, that is, a line parallel to $u$.
- Any set of at most two points of $\mathbb{F}_p^2$ lies in an affine line. One point $a$ lies in $a+\langle s\rangle$ for any $s\ne0$; two points $a\ne b$ lie in $a+\langle b-a\rangle$.
- A **line direction** of $f$ is a vector $u\ne0$ such that $A_u(f)$ is contained in an affine line.
- For a group element $e$ and an integer $j$, $je$ is the $j$-fold sum. For $g\in G$, $\langle g\rangle$ is the cyclic subgroup generated by $g$. The **order** of $g$ is the size of $\langle g\rangle$.

Three facts about $\iota$ and orders are used throughout.

**Fact 1.** $\iota$ is well defined, additive and injective, and $\iota(\mathbb{F}_p^2)=H$. In particular $\iota(a)=p[a]$.

*Proof.* If $m\equiv m'\pmod p$ then $pm\equiv pm'\pmod{p^2}$, so $\iota$ is well defined. If $m,m'$ lift $a,a'$, then $m+m'$ lifts $a+a'$, so $\iota$ is additive. If $pm\equiv0\pmod{p^2}$ then $m\equiv0\pmod p$, so $\iota$ is injective. The image is $\lbrace pm\bmod p^2\rbrace=pG=H$. ∎

**Fact 2.** $pg=\iota(\pi(g))$ for every $g\in G$. Hence $pg=0$ if and only if $g\in H$.

*Proof.* Write $g=m\bmod p^2$ with $m\in\mathbb{Z}^2$. Then $\pi(g)=m\bmod p$, and $pg=pm\bmod p^2=\iota(\pi(g))$. By Fact 1, $\iota(\pi(g))=0$ exactly when $\pi(g)=0$, that is, when $g\in H$. ∎

**Fact 3.** Every $g\in G\setminus H$ has order $p^2$.

*Proof.* $p^2g=0$, so the order divides $p^2$. And $pg\ne0$ by Fact 2, so the order does not divide $p$. ∎

**Transversals are exactly the sets $T_f$.** Since $\pi(t_f(x))=x$, the set $T_f$ is a transversal. Conversely, let $T$ be a transversal. Its element over $x$ is $[x]+h$ for a unique $h\in H=\iota(\mathbb{F}_p^2)$ (Fact 1), so $T=T_f$ for exactly one $f$. The source also normalises $f(0)=0$, that is, $0\in T$. Nothing below needs this.

**Conventions checked against the source's first values.** For the "box" $f=0$, Lemma E below gives $\lvert T_0-T_0\rvert=(2p-1)^2$. Literal subtraction in $G$ gives $25,81,169,441,625$ for $p=3,5,7,11,13$ (`scripts/out/rows.log`, part [1]) and $9,25,81,169,441$ for $p=2,3,5,7,11$ (`scripts/out/check_algebra.log`). `numerical`.

## 2. Statements

> **Theorem 1 (line-direction lemma).** Let $p$ be an odd prime, $f:\mathbb{F}_p^2\to\mathbb{F}_p^2$ any function and $T=T_f$. Suppose that for some $u\ne0$ the set $A_u(f)$ is contained in an affine line. Then:
>
> **(a)** $\lvert T-T\rvert=\sum_{w\in\mathbb{F}_p^2}\lvert A_w(f)\rvert\ge(2p-1)^2$.
>
> **(b)** For every $v\in\mathbb{F}_p^2\setminus\langle u\rangle$, $\sum_{k\in\mathbb{F}_p}\lvert A_{ku+v}(f)\rvert\ge4p-2$; and $\sum_{k\in\mathbb{F}_p}\lvert A_{ku}(f)\rvert\ge2p-1$.
>
> **(c)** $T$ is contained in a union of $p$ cosets of a cyclic subgroup $C\le G$ of order $p^2$ with $\pi(C)=\langle u\rangle$. Conversely, if a transversal $T_f$ is contained in a union of at most $p$ cosets of a cyclic subgroup $C$ of order $p^2$, then every nonzero $w\in\pi(C)$ is a line direction of $f$. Hence $f$ has a line direction if and only if $T_f$ is contained in a union of at most $p$ cosets of some cyclic subgroup of order $p^2$. Consequently, if $u$ is a line direction of $f$, then so is $ku$ for every $k\in\mathbb{F}_p\setminus\lbrace0\rbrace$.
>
> *(In `paper.tex` these sentences are parts (c), (d) and (e) of Theorem 3.1.)*

We call the sum in (b) the **column sum** of the coset $v+\langle u\rangle$.

> **Corollary 2.** For every odd prime $p$ and every transversal $T$ for $G_p/H_p$, $\lvert T-T\rvert\ge\min\lbrace(2p-1)^2,3p^2-2\rbrace=3p^2-2$. Hence $\delta(G_p,H_p)\ge3p^2-2$.

> **Corollary 3.** For each odd prime $p$ the following are equivalent.
> (i) $\delta(G_p,H_p)=(2p-1)^2$ (Conjecture 6.2 of the source at $p$).
> (ii) $\sum_u\lvert A_u(f)\rvert\ge(2p-1)^2$ for every $f:\mathbb{F}_p^2\to\mathbb{F}_p^2$.
> (iii) $\sum_u\lvert A_u(f)\rvert\ge(2p-1)^2$ for every $f$ with no line direction.
> (iv) $\sum_{u\ne0}(\lvert A_u(f)\rvert-3)\ge(p-1)(p-3)$ for every $f$ with no line direction.
> In (ii)–(iv) one may restrict to $f$ with $f(0)=0$.

> **Corollary 4.** $\delta((\mathbb{Z}/9\mathbb{Z})^2,3(\mathbb{Z}/9\mathbb{Z})^2)=25$, with no computation.

A two-element set is collinear, so Theorem 1 applies whenever $\lvert A_u(f)\rvert=2$ for a single $u\ne0$. So Theorem 1 contains the "one-2-direction theorem" of the automath notes and, a fortiori, Lemma 6.4 of the source (two independent such directions). See §9 for credit.

## 3. Lemmas

The lemmas are proved in order. Each proof uses only the facts of §1 and the lemmas before it.

**Lemma A (fibre formula; Lemma 6.1 of the source).** For all $f$ and all $u,x\in\mathbb{F}_p^2$,

```math
t(x+u)-t(x)=[u]+\iota\bigl(d_uf(x)\bigr)\quad\text{in }G .
```

Consequently: (i) $(T_f-T_f)\cap\pi^{-1}(u)=[u]+\iota(A_u(f))$, a set with $\lvert A_u(f)\rvert$ elements; (ii) $\lvert T_f-T_f\rvert=\sum_{u}\lvert A_u(f)\rvert$; (iii) $A_0(f)=\lbrace0\rbrace$.

*Proof.* In each coordinate $c$, the standard lifts satisfy $x_c+u_c\in\lbrace0,\dots,2p-2\rbrace$, and $[x+u]_c$ equals $x_c+u_c$ or $x_c+u_c-p$. So $[x+u]=[x]+[u]+p\tilde c$ in $\mathbb{Z}^2$ with $\tilde c\in\lbrace0,-1\rbrace^2$, and $\tilde c\bmod p=c_u(x)$ by definition. Hence, in $G$, using Fact 1 three times,

```math
t(x+u)-t(x)=[u]+p\tilde c+\iota(f(x+u))-\iota(f(x))=[u]+\iota\bigl(c_u(x)+f(x+u)-f(x)\bigr)=[u]+\iota\bigl(d_uf(x)\bigr).
```

(i) Every element of $T_f-T_f$ is $t(y)-t(x)$ for some $x,y$, and $\pi(t(y)-t(x))=y-x$. So the part of $T_f-T_f$ over $u$ is $\lbrace t(x+u)-t(x):x\rbrace=[u]+\iota(A_u(f))$. Translation and $\iota$ are injective, so this set has $\lvert A_u(f)\rvert$ elements. (ii) The sets $\pi^{-1}(u)$ partition $G$. (iii) $c_0(x)=0$, so $d_0f(x)=0$. ∎

**Lemma B (cycle identity; Lemma 6.3 of the source).** For all $f$ and all $u,x\in\mathbb{F}_p^2$, $\sum_{i=0}^{p-1}d_uf(x+iu)=-u$.

*Proof.* In $G$ the sum $\sum_{i=0}^{p-1}\bigl(t(x+(i+1)u)-t(x+iu)\bigr)$ telescopes to $t(x+pu)-t(x)=0$, because $pu=0$ in $\mathbb{F}_p^2$. By Lemma A and Fact 1 the same sum equals $p[u]+\iota\bigl(\sum_id_uf(x+iu)\bigr)=\iota\bigl(u+\sum_id_uf(x+iu)\bigr)$. As $\iota$ is injective, $u+\sum_id_uf(x+iu)=0$. ∎

**Lemma C (a line containing $A_u$ is parallel to $u$).** Let $u\ne0$ and suppose $A_u(f)\subseteq a+\langle s\rangle$ with $s\ne0$. Then $\langle s\rangle=\langle u\rangle$, so $A_u(f)\subseteq a'+\langle u\rangle$ for every $a'\in A_u(f)$. In particular $\lvert A_u(f)\rvert\ge2$ for every $u\ne0$.

*Proof.* Write $d_uf(iu)=a+\lambda_is$ with $\lambda_i\in\mathbb{F}_p$, for $i=0,\dots,p-1$. By Lemma B with $x=0$, $-u=\sum_i(a+\lambda_is)=pa+\Lambda s=\Lambda s$, where $\Lambda=\sum_i\lambda_i$ and $pa=0$ in $\mathbb{F}_p^2$. Since $u\ne0$, $\Lambda\ne0$ and $u=-\Lambda s\in\langle s\rangle$. So $\langle u\rangle\subseteq\langle s\rangle$. Both sets have $p$ elements, hence they are equal. Then $a+\langle s\rangle=a+\langle u\rangle=a'+\langle u\rangle$ for each $a'\in A_u(f)$. Finally, suppose $A_u(f)$ were a single point $a$. It would lie in $a+\langle s\rangle$ for some $s\notin\langle u\rangle$ (such $s$ exists since $p^2>p$), contradicting what we just proved. ∎

For $\lvert A_u(f)\rvert\le2$ this is Lemma 6.3 (1)–(2) of the source; the proof is the same for any collinear image.

**Lemma D (the cyclic subgroup over a direction).** Let $g\in G\setminus H$, $u=\pi(g)$ (so $u\ne0$) and $C=\langle g\rangle$. Then:
(i) $\lvert C\rvert=p^2$;
(ii) $\pi(C)=\langle u\rangle$;
(iii) $C\cap H=pC=\iota(\langle u\rangle)$, a subgroup of order $p$;
(iv) $C\cap\pi^{-1}(u)=g+pC$;
(v) every element of $C\setminus pC$ has order $p^2$.

*Proof.* (i) is Fact 3. (ii) $\pi(kg)=ku$. (iii) $kg\in H$ if and only if $ku=0$, if and only if $p$ divides $k$. So $C\cap H=\lbrace jpg:j\in\mathbb{Z}\rbrace=pC$. By Fact 2, $jpg=\iota(ju)$, so $pC=\iota(\langle u\rangle)$, which has $p$ elements by Fact 1. (iv) $\pi(kg)=u$ if and only if $k\equiv1\pmod p$, if and only if $(k-1)g\in pC$ (by (iii)), that is, $kg\in g+pC$. (v) $C\setminus pC=C\setminus H\subseteq G\setminus H$ by (iii); apply Fact 3. ∎

**Lemma E (box; the first two statements are Proposition 5.3 of the source).** For $f=0$, $\lvert T_0-T_0\rvert=(2p-1)^2$. Hence $\delta(G_p,H_p)\le(2p-1)^2$. Moreover $\lvert A_w(0)\rvert=2^{n(w)}$, where $n(w)$ is the number of nonzero coordinates of $w$.

*Proof.* $T_0=\lbrace[x]\rbrace$ is the set of classes of $\lbrace0,\dots,p-1\rbrace^2$. So $T_0-T_0$ is the set of classes of $\lbrace-(p-1),\dots,p-1\rbrace^2$. The $2p-1$ integers $-(p-1),\dots,p-1$ are pairwise incongruent modulo $p^2$, because two of them differ by at most $2p-2<p^2$. So $\lvert T_0-T_0\rvert=(2p-1)^2$. For the last claim, $A_w(0)=\lbrace c_w(x)\rbrace$. In a coordinate with $w_c=0$ the carry is always $0$. In a coordinate with $w_c\ne0$ it is $0$ for $x_c=0$ and $-1$ for $x_c=p-1$, and it is never anything else. The two coordinates of $x$ vary independently. ∎

**Lemma F (one-dimensional cross-transversal bound).** Let $Z$ be an abelian group, $K\le Z$ a subgroup of finite index $q\ge1$, $\sigma:Z\to Z/K$ the quotient map, and $A,B\subseteq Z$ two transversals for $Z/K$ (each contains exactly one element of each coset of $K$). Assume

> **(O)** every $e\in Z\setminus K$ has order greater than $q$ (the order may be infinite).

For $r\in Z/K$ put $F_r=(A-B)\cap\sigma^{-1}(r)$. Then:
(i) each $F_r$ is non-empty, and $A-B$ is the disjoint union of the sets $F_r$;
(ii) at most one of the sets $F_r$ is a singleton;
(iii) $\lvert A-B\rvert\ge2q-1$;
(iv) if $A=B$, then $F_0=\lbrace0\rbrace$ and $\lvert F_r\rvert\ge2$ for every $r\ne0$.

*Proof.* Let $\alpha,\beta:Z/K\to Z$ be the sections with $\alpha(Z/K)=A$ and $\beta(Z/K)=B$.

(i) For $x\in Z/K$, $\alpha(x+r)-\beta(x)\in F_r$, so $F_r\ne\emptyset$. An element $\alpha(y)-\beta(x)$ of $A-B$ lies in $\sigma^{-1}(y-x)$ only. So $F_r=\lbrace\alpha(x+r)-\beta(x):x\in Z/K\rbrace$, and the sets $F_r$ partition $A-B$.

(ii) Suppose $r\ne r'$, $F_r=\lbrace c\rbrace$ and $F_{r'}=\lbrace c'\rbrace$. Then $\alpha(x+r)-\beta(x)=c$ and $\alpha(x+r')-\beta(x)=c'$ for all $x$. Subtracting, $\alpha(x+r)-\alpha(x+r')=e$ for all $x$, where $e=c-c'$. Here $\sigma(e)=r-r'\ne0$, so $e\notin K$. Putting $y=x+r'$ gives $\alpha(y+(r-r'))=\alpha(y)+e$ for all $y\in Z/K$. So $a+e\in A$ whenever $a\in A$, and by induction $a+je\in A$ for all $a\in A$ and $j\ge0$. Fix $a\in A$. The $q+1$ elements $a,a+e,\dots,a+qe$ lie in $A$, which has $q$ elements. So $a+je=a+j'e$ for some $0\le j<j'\le q$. Then $(j'-j)e=0$ with $1\le j'-j\le q$, which contradicts (O).

(iii) By (i) and (ii), $\lvert A-B\rvert=\sum_r\lvert F_r\rvert\ge1+2(q-1)=2q-1$.

(iv) If $A=B$ then $\alpha=\beta$, and $F_0=\lbrace\alpha(x)-\alpha(x)\rbrace=\lbrace0\rbrace$ is a singleton. By (ii) no other $F_r$ is a singleton, and by (i) none is empty. ∎

*Smallest examples.* $q=1$: $A=\lbrace a\rbrace$, $B=\lbrace b\rbrace$, and $\lvert A-B\rvert=1$. $Z=\mathbb{Z}/4$, $K=\lbrace0,2\rbrace$, $A=B=\lbrace0,1\rbrace$: $A-B=\lbrace0,1,3\rbrace$, three elements. $Z=\mathbb{Z}/9$, $K=3Z$, $A=B=\lbrace0,1,2\rbrace$: five elements.

*Hypothesis (O) cannot be dropped.* In $Z=\mathbb{Z}/6$ with $K=\lbrace0,3\rbrace$, the transversal $A=B=\lbrace0,2,4\rbrace$ has $\lvert A-B\rvert=3<5$.

*Relation to the source.* For $Z$ cyclic of order $p^2$ and $K=pZ$, one has $m(Z,K)=1$ (Proposition 5.3 of the source, $r=1$), where $m(Z,K)$ is the largest order of a subgroup meeting $K$ only in $0$. So part (iii) is the case $\lvert G/H\rvert=p$, $m(G,H)=1$ of Theorem 4.2 of the source, which gives $\lvert A-B\rvert\ge2\lvert G/H\rvert-m(G,H)$ and is proved there with Kneser's theorem. For $A=B$, part (iv) is contained in Propositions 3.2–3.3 of the source. The proof above adapts the source's singleton argument to two transversals and does not use Kneser's theorem.

## 4. Proof of Theorem 1

The proof has three parts. First, Lemma G turns the hypothesis "$A_u(f)$ lies in a line parallel to $u$" into a covering of $T$ by $p$ cosets of a cyclic subgroup $C$. Second, §4.2 builds two quotient groups in which Lemma F applies. Third, Lemma F is applied twice and the differences are counted coset by coset.

### 4.1 The covering criterion

**Lemma G (covering criterion).** Let $u\ne0$, $a\in\mathbb{F}_p^2$, $g=[u]+\iota(a)$ and $C=\langle g\rangle$. Then $C$ is cyclic of order $p^2$ with $\pi(C)=\langle u\rangle$, and for every $f$:

```math
A_u(f)\subseteq a+\langle u\rangle\quad\Longleftrightarrow\quad T_f\ \text{is contained in a union of at most } p \text{ cosets of } C .
```

When this holds, $t$ maps each $u$-line into one coset of $C$, and different $u$-lines go to different cosets. So $T_f$ meets exactly $p$ cosets of $C$, each in exactly $p$ elements. Moreover, every cyclic subgroup $C'$ of $G$ of order $p^2$ equals $\langle[w]+\iota(a')\rangle$ for each nonzero $w\in\pi(C')$ and a suitable $a'$ (depending on $w$).

*Proof.* $\pi(g)=u\ne0$, so $g\notin H$, and Lemma D applies to $g$ and $C$.

*Step 1 (one step of a chain).* Assume $A_u(f)\subseteq a+\langle u\rangle$. For every $x$, by Lemma A, Fact 1 and Lemma D (iii),

```math
t(x+u)-t(x)=[u]+\iota(d_uf(x))=g+\iota\bigl(d_uf(x)-a\bigr)\in g+\iota(\langle u\rangle)=g+pC\subseteq C .
```

*Step 2 (chains).* For $x\in\mathbb{F}_p^2$ and an integer $i\ge0$, $t(x+iu)-t(x)=\sum_{j<i}\bigl(t(x+(j+1)u)-t(x+ju)\bigr)\in C$ by Step 1. So $t$ maps the $u$-line $x+\langle u\rangle$ into the coset $t(x)+C$. There are $p$ $u$-lines, so $T_f$ lies in at most $p$ cosets of $C$. This proves "$\Rightarrow$".

*Converse.* Assume $T_f$ lies in a union of at most $p$ cosets of $C$. If $t(x)$ and $t(x')$ lie in the same coset of $C$, then $x-x'=\pi(t(x)-t(x'))\in\pi(C)=\langle u\rangle$, so $x$ and $x'$ are on the same $u$-line. Hence the elements of $T_f$ in one coset of $C$ are images of points of a single $u$-line, and there are at most $p$ of them. As $\lvert T_f\rvert=p^2$, exactly $p$ cosets are met, each contains exactly $p$ elements of $T_f$, and these are the images of a full $u$-line. Different cosets correspond to different $u$-lines. In particular, for every $x$ the points $x$ and $x+u$ are on one $u$-line, so $t(x+u)-t(x)\in C$. Its image under $\pi$ is $u$. So by Lemma D (iv), Lemma D (iii) and the definition of $g$,

```math
[u]+\iota(d_uf(x))=t(x+u)-t(x)\in g+pC=[u]+\iota\bigl(a+\langle u\rangle\bigr).
```

Since $\iota$ is injective, $d_uf(x)\in a+\langle u\rangle$ for all $x$. This proves "$\Leftarrow$". It also proves the "exactly $p$ cosets" statement, because in the "$\Rightarrow$" situation the converse argument applies.

*Last statement.* Let $C'$ be cyclic of order $p^2$ with generator $g_0$. Then $g_0\notin H$, since otherwise $pg_0=0$ by Fact 2. Put $u_0=\pi(g_0)\ne0$, so $\pi(C')=\langle u_0\rangle$. Let $w=ku_0$ with $k\in\lbrace1,\dots,p-1\rbrace$ and put $g'=kg_0\in C'$. Then $\pi(g')=w\ne0$, so $g'\notin H$ has order $p^2$ by Fact 3 and generates $C'$. As $g'-[w]\in H=\iota(\mathbb{F}_p^2)$, $g'=[w]+\iota(a')$ for some $a'$. ∎

### 4.2 Proof of (a)

Let $u\ne0$ with $A_u(f)$ contained in an affine line. By Lemma C, $A_u(f)\subseteq a+\langle u\rangle$ for a fixed $a\in A_u(f)$. Let $g=[u]+\iota(a)$ and $C=\langle g\rangle$, as in Lemma G. Fix $v_0\in\mathbb{F}_p^2\setminus\langle u\rangle$. Since $u,v_0$ is a basis, the map $(n,i)\mapsto nv_0+iu$ is a bijection of $\mathbb{F}_p\times\mathbb{F}_p$ onto $\mathbb{F}_p^2$. So the $u$-lines are $L_n=nv_0+\langle u\rangle$, $n\in\mathbb{F}_p$. Put

```math
\tau_n=t(nv_0),\qquad R_n=t(L_n)\subseteq\tau_n+C,\qquad T=\bigsqcup_{n\in\mathbb{F}_p}R_n,\qquad \lvert R_n\rvert=p .
```

The inclusion is Step 2. The union is disjoint and $\lvert R_n\rvert=p$ because $t$ is injective ($\pi\circ t$ is the identity) and the lines $L_n$ partition $\mathbb{F}_p^2$.

*Step 3 (two quotients).* Let $M=H+C$. Let $\rho:G\to Q=G/C$ be the quotient map, $K=\rho(H)\le Q$, and $\kappa:Q\to Q/K$ the quotient map.

**(3a)** $M=\pi^{-1}(\langle u\rangle)$, and $\kappa\circ\rho:G\to Q/K$ is a surjective homomorphism with kernel $M$. So there is an isomorphism $\theta:Q/K\to\mathbb{F}_p^2/\langle u\rangle$ with $\theta(\kappa\rho(y))=\pi(y)+\langle u\rangle$, and $[Q:K]=p$.

*Proof.* $\pi(M)=\pi(H)+\pi(C)=\langle u\rangle$ by Lemma D (ii). Conversely, if $\pi(y)=ku$, then $\pi(y-kg)=0$, so $y-kg\in H$ and $y\in H+C$. Next, $\kappa\rho(y)=0$ if and only if $\rho(y)\in\rho(H)$, if and only if $y\in H+C=M$. Both $\kappa\rho$ and $y\mapsto\pi(y)+\langle u\rangle$ are surjective homomorphisms from $G$ with kernel $M$, which gives $\theta$. Finally, $\mathbb{F}_p^2/\langle u\rangle$ has $p$ elements. ∎

**(3b)** Hypothesis (O) of Lemma F holds for $(Z,K)=(Q,K)$ with $q=p$: every $e\in Q\setminus K$ has order greater than $p$.

*Proof.* Let $e\in Q\setminus K$ and write $e=\rho(y)$. Then $y\notin M$: otherwise $y=h+c$ with $h\in H$ and $c\in C$, and $e=\rho(y)=\rho(h)\in K$. Suppose $je=0$, that is, $jy\in C$, for some $1\le j\le p$. If $j<p$: $j\pi(y)=\pi(jy)\in\pi(C)=\langle u\rangle$, and $j$ is invertible in $\mathbb{F}_p$, so $\pi(y)\in\langle u\rangle$ and $y\in M$ by (3a), a contradiction. If $j=p$: $py\in H$ because $\pi(py)=p\pi(y)=0$, so $py\in C\cap H=pC$ by Lemma D (iii). Write $py=pc$ with $c\in C$. Then $p(y-c)=0$, so $y-c\in H$ by Fact 2, and $y\in H+C=M$, a contradiction. ∎

**(3c)** Put $y_n=\rho(\tau_n)$ and $Y=\lbrace y_n:n\in\mathbb{F}_p\rbrace$. Then $\rho(R_n)=\lbrace y_n\rbrace$, and $Y$ is a transversal for $Q/K$.

*Proof.* $R_n\subseteq\tau_n+C$ gives $\rho(R_n)=\lbrace y_n\rbrace$. By (3a), $\theta(\kappa(y_n))=\pi(\tau_n)+\langle u\rangle=nv_0+\langle u\rangle$. These $p$ cosets are pairwise different: if $(n-n')v_0\in\langle u\rangle$ then $n=n'$, because $v_0\notin\langle u\rangle$. And $\mathbb{F}_p^2/\langle u\rangle$ has $p$ elements. So $\kappa$ maps $Y$ bijectively onto $Q/K$. ∎

**(3d)** $[C:pC]=p$; for each $n$ the set $A_n=R_n-\tau_n$ is a transversal for $C/pC$; and hypothesis (O) holds for $(Z,K)=(C,pC)$ with $q=p$.

*Proof.* $\pi$ restricted to $C$ is a homomorphism onto $\langle u\rangle$ with kernel $C\cap H=pC$ (Lemma D (ii), (iii)). So $[C:pC]=p$, and two elements of $C$ are in the same coset of $pC$ if and only if they have the same image under $\pi$. By Step 2, $A_n=\lbrace t(nv_0+iu)-t(nv_0):i\in\mathbb{F}_p\rbrace\subseteq C$, and the element with index $i$ has image $iu$. These images are pairwise different and exhaust $\langle u\rangle$. So $A_n$ has exactly one element in each coset of $pC$. Hypothesis (O) is Lemma D (v), since $p^2>p$. ∎

*Step 4 (the one-dimensional bound, twice).* By (3a), (3b), (3c) and Lemma F (iii), (iv) applied to $(Z,K,A,B)=(Q,K,Y,Y)$:

```math
\lvert Y-Y\rvert\ge2p-1,\qquad \bigl\lvert(Y-Y)\cap\kappa^{-1}(r)\bigr\rvert\ge2\ \text{ for every } r\in Q/K,\ r\ne0 .
```

By (3d) and Lemma F (iii) applied to $(Z,K,A,B)=(C,pC,A_n,A_m)$: $\lvert A_n-A_m\rvert\ge2p-1$ for all $n,m\in\mathbb{F}_p$.

*Step 5 (count).* For $n,m\in\mathbb{F}_p$, since $R_n=\tau_n+A_n$ and $A_n,A_m\subseteq C$,

```math
R_n-R_m=(\tau_n-\tau_m)+(A_n-A_m)\subseteq(T-T)\cap\rho^{-1}(y_n-y_m),\qquad \lvert R_n-R_m\rvert=\lvert A_n-A_m\rvert\ge2p-1 .
```

Every $z\in Y-Y$ is $y_n-y_m$ for some $n,m$. So $\lvert(T-T)\cap\rho^{-1}(z)\rvert\ge2p-1$ for every $z\in Y-Y$. The sets $\rho^{-1}(z)$ are pairwise disjoint. Therefore

```math
\lvert T-T\rvert\ \ge\sum_{z\in Y-Y}\bigl\lvert(T-T)\cap\rho^{-1}(z)\bigr\rvert\ \ge\ (2p-1)\cdot\lvert Y-Y\rvert\ \ge\ (2p-1)^2 .
```

With Lemma A (ii) this is (a). ∎

### 4.3 Proof of (b)

We count the part of $T-T$ that lies over one coset of $\langle u\rangle$, using the two fibre bounds of Step 4.

Let $W$ be a coset of $\langle u\rangle$ in $\mathbb{F}_p^2$. By Lemma A (i), $\sum_{w\in W}\lvert A_w(f)\rvert=\lvert(T-T)\cap\pi^{-1}(W)\rvert$. By (3a), $\pi^{-1}(W)=(\kappa\rho)^{-1}(r)$ with $r=\theta^{-1}(W)$, and $r\ne0$ exactly when $W\ne\langle u\rangle$.

If $W=v+\langle u\rangle$ with $v\notin\langle u\rangle$, then $r\ne0$. By Step 4 the set $(Y-Y)\cap\kappa^{-1}(r)$ contains two different elements $z,z'$. The sets $(T-T)\cap\rho^{-1}(z)$ and $(T-T)\cap\rho^{-1}(z')$ are disjoint, each has at least $2p-1$ elements (Step 5), and both lie in $(\kappa\rho)^{-1}(r)=\pi^{-1}(W)$. Hence $\sum_{k\in\mathbb{F}_p}\lvert A_{ku+v}(f)\rvert\ge2(2p-1)=4p-2$.

If $W=\langle u\rangle$, then $R_0-R_0\subseteq(T-T)\cap\rho^{-1}(0)\subseteq(T-T)\cap M$, and it has at least $2p-1$ elements (Step 5). As $M=\pi^{-1}(\langle u\rangle)$ by (3a), $\sum_{k\in\mathbb{F}_p}\lvert A_{ku}(f)\rvert\ge2p-1$. ∎

(Summing over the $p$ cosets: $(2p-1)+(p-1)(4p-2)=(2p-1)^2$, which is (a) again.)

### 4.4 Proof of (c)

The first statement is Lemma G "$\Rightarrow$", with the subgroup $C$ of §4.2. For the converse, let $T_f$ lie in a union of at most $p$ cosets of a cyclic subgroup $C'$ of order $p^2$, and let $0\ne w\in\pi(C')$. By the last statement of Lemma G, $C'=\langle[w]+\iota(a')\rangle$ for some $a'$. Lemma G "$\Leftarrow$", with $u,a$ replaced by $w,a'$, gives $A_w(f)\subseteq a'+\langle w\rangle$, which is an affine line. For the "if and only if": the first statement gives one direction. For the other, $\pi(C')\ne\lbrace0\rbrace$, since otherwise $C'\subseteq H$, a generator $g'$ of $C'$ satisfies $pg'=0$ (Fact 2), and $C'$ has at most $p$ elements; so the converse gives a line direction. Finally, if $u$ is a line direction, then $T_f$ lies in $p$ cosets of a cyclic $C$ of order $p^2$ with $\pi(C)=\langle u\rangle$, and by the converse every nonzero $ku\in\langle u\rangle$ is a line direction. ∎

### 4.5 Remarks

**Sharpness.** Take the box $f=0$ and $u=e_1=(1,0)$. Lemma E gives $A_{e_1}(0)=\lbrace(0,0),(-1,0)\rbrace\subseteq\langle e_1\rangle$ and $\lvert T_0-T_0\rvert=(2p-1)^2$. For $v=(0,m)$ with $m\ne0$, the column sum is $2+4(p-1)=4p-2$. So (a) and (b) are attained for every $p$.

**The prime 2.** The proofs of Lemmas A–G and of Theorem 1 never use that $p$ is odd. At $p=2$, Lemma B gives $d_uf(x+u)=d_uf(x)+u$, so each $A_u(f)$ with $u\ne0$ is a union of cosets of $\langle u\rangle$ and has $2$ or $4$ elements. With Theorem 1 this gives $\lvert T-T\rvert\ge\min\lbrace9,1+3\cdot4\rbrace=9$ for every transversal of $(\mathbb{Z}/4)^2$ modulo $2(\mathbb{Z}/4)^2$. This agrees with Corollary 5.2 of the source ($\delta=9$ for $r=2$). It is used here only as a consistency check.

## 5. Proofs of the corollaries

**Proof of Corollary 2.** We split into the case where $f$ has a line direction and the case where it has none. Let $T$ be a transversal; then $T=T_f$ for some $f$ (§1). If $f$ has a line direction, $\lvert T-T\rvert\ge(2p-1)^2$ by Theorem 1 (a). Otherwise no $A_u(f)$ with $u\ne0$ lies in an affine line. Since every set of at most two points lies in an affine line (§1), $\lvert A_u(f)\rvert\ge3$ for all $u\ne0$. By Lemma A (ii), (iii),

```math
\lvert T-T\rvert=1+\sum_{u\ne0}\lvert A_u(f)\rvert\ \ge\ 1+3(p^2-1)=3p^2-2 .
```

Finally $(2p-1)^2-(3p^2-2)=p^2-4p+3=(p-1)(p-3)\ge0$ for $p\ge3$. ∎

For every odd prime $p$ the bound $3p^2-2$ exceeds the bound $3p^2-p-1$ of Theorem 6.5 of the source by $p-1$. At $p=3$ this is $25$ against $23$, which is exactly what gives Corollary 4. For $p=3$ the two terms of the minimum in Corollary 2 coincide.

**Proof of Corollary 4.** At $p=3$, Corollary 2 gives $\delta\ge\min\lbrace25,25\rbrace=25$, and Lemma E gives $\delta\le25$. ∎

**Proof of Corollary 3.** (i) $\Leftrightarrow$ (ii): the transversals are exactly the sets $T_f$ (§1), and $\lvert T_f-T_f\rvert=\sum_u\lvert A_u(f)\rvert$ (Lemma A). So (ii) says $\delta\ge(2p-1)^2$. The reverse inequality always holds (Lemma E). (ii) $\Rightarrow$ (iii) is trivial. (iii) $\Rightarrow$ (ii): if $f$ has a line direction, the inequality is Theorem 1 (a); otherwise it is (iii). (iii) $\Leftrightarrow$ (iv): by Lemma A (iii), $\sum_u\lvert A_u(f)\rvert=1+3(p^2-1)+\sum_{u\ne0}(\lvert A_u(f)\rvert-3)$, and $(2p-1)^2-1-3(p^2-1)=(p-1)(p-3)$. Normalisation: for a constant $b$, $d_u(f-b)=d_uf$, so $f$ and $f-f(0)$ have the same images $A_u$ and the same line directions. ∎

*Reformulation of (iv).* For $f$ with no line direction, every $\lvert A_u(f)\rvert\ge3$ ($u\ne0$), and a three-element $A_u(f)$ is a non-collinear triple. Let $N_3$ be the number of $u\ne0$ with $\lvert A_u(f)\rvert=3$, and let $E=\sum_{u:\lvert A_u(f)\rvert\ge4}(\lvert A_u(f)\rvert-4)$. Then $\sum_{u\ne0}(\lvert A_u(f)\rvert-3)=(p^2-1-N_3)+E$, so (iv) reads $N_3-E\le4p-4$. At $p=3$ the right side of (iv) is $0$ and (iv) holds trivially, in agreement with Corollary 4.

## 6. Table of steps

"Argument" gives the place of the full written argument. "Check" says exactly what `scripts/check_L1.py` tests for the step, under which failure labels, and in which runs of §7 (Run 0 to Run 6). All checks are `numerical`. A check is listed only if it computes the step from the definitions (literal subtraction in $G$, carries, subgroups and cosets built as sets), not from another step of the proof. Where a step has no machine check, the table says so. None is needed, because no argument of §§1–5 depends on the script.

| Step | Statement | Status | Argument | Check |
| --- | --- | --- | --- | --- |
| Facts 1–3 | $\iota$ is an injective homomorphism onto $H$; $pg=\iota(\pi(g))$; elements outside $H$ have order $p^2$ | `proposed` | §1 | `N1: ...` (well defined over many lifts, additive, injective, image $H$), `N2: ...` and `N3: ...` (order counted as the number of distinct multiples) on every element of $G$, $p=2,3,5,7,11$ (Run 0) |
| Lemma A | fibre formula (source Lemma 6.1) | `proposed` | §3 | `Lemma A: ...` (fibre equals $[u]+\iota(A_u)$, its size, union of fibres equals the literal $T-T$, sum formula, $A_0=\lbrace0\rbrace$) on every $f$ tested in Runs 1, 3–6 |
| Lemma B | cycle identity (source Lemma 6.3) | `proposed` | §3 | `Lemma B: cycle identity` for every $u\ne0$ and every $x$, on every $f$ tested |
| Lemma C | a line containing $A_u$ is parallel to $u$; $\lvert A_u\rvert\ge2$ | `proposed` | §3 | `Lemma C: ...` on every collinear $A_u$ ($u\ne0$) met in the runs |
| Lemma D | $C=\langle g\rangle$: (i) order $p^2$, (ii) $\pi(C)=\langle u\rangle$, (iii) $C\cap H=pC=\iota(\langle u\rangle)$, (iv) $C\cap\pi^{-1}(u)=g+pC$, (v) orders on $C\setminus pC$ | `proposed` | §3 | `Lemma D (i)` to `Lemma D (iv)` for every $g\in G\setminus H$, and `Lemma D (v)` for every cyclic subgroup of order $p^2$, $p=2,3,5,7,11$ (Run 0); (i)–(iii) again for the generators $[u]+\iota(a)$ at the start of every run (`Lemma D: ...`) |
| Lemma E | box: $\lvert T_0-T_0\rvert=(2p-1)^2$ (source Prop. 5.3); $\lvert A_w(0)\rvert=2^{n(w)}$ | `proposed` | §3 | `Lemma E: ...`: the box total by literal subtraction, and $\lvert A_w(0)\rvert=2^{n(w)}$ from the carry definition for every $w$, $p=2,3,5,7,11$ (Run 0); the $p=5$ box also in Run 4 |
| Lemma F | one-dimensional cross-transversal bound, with "at most one singleton fibre" | `proposed` | §3 | one hand example for each of $q=1,2,3$ (§3, "Smallest examples"); (ii) and (iii) exhaustive over all pairs of transversals of $\mathbb{Z}/1,\mathbb{Z}/4,\mathbb{Z}/8,\mathbb{Z}/9,\mathbb{Z}/16,\mathbb{Z}/25,\mathbb{Z}/27$ (Run 2; cyclic groups only, (i) and (iv) not tested there); the two uses in Step 4, including (iv), as `Lemma F (C)` and `Lemma F (Q)` |
| Lemma G | covering criterion: $A_u\subseteq a+\langle u\rangle$ iff $T_f$ lies in $p$ cosets of $\langle[u]+\iota(a)\rangle$; every cyclic $C'$ of order $p^2$ is $\langle[w]+\iota(a')\rangle$ for each nonzero $w\in\pi(C')$ | `proposed` | §4.1 | equivalence: `Lemma G: ...`, both directions, every cyclic subgroup of order $p^2$, every $f$ tested; last statement: `Lemma G (last statement)`, every cyclic subgroup of order $p^2$, $p=2,3,5,7,11$ (Run 0) |
| Steps 1–2 | steps and chains lie in $C$ | `proposed` | §4.1 | `step 1`, `step 2` on every pair ($f$, line-direction subspace) |
| Step 3a | $M=H+C=\pi^{-1}(\langle u\rangle)$; $\kappa\rho$ has kernel $M$; $\theta$; $[Q:K]=p$ | `proposed` | §4.2 | `step 3a: ...`: $H+C$ built as a set of sums equals $\pi^{-1}(\langle u\rangle)$; $\lvert Q\rvert=p^2$ and $\lvert K\rvert=p$ from the cosets of $C$; the kernel of $\kappa\rho$ is $M$; $\theta$ is well defined and bijective; every cyclic subgroup of order $p^2$, $p=2,3,5,7,11$ (Run 0); `step 3a: [Q:K] = p` at the start of every run |
| Step 3b | (O) in $Q$ with $q=p$ | `proposed` | §4.2 | `step 3b`: $jy\notin C$ for every $y$ outside the set $M$ and $1\le j\le p$; every cyclic subgroup, $p=2,3,5,7,11$ (Run 0), and $p\le7$ at the start of the other runs |
| Step 3c | $Y$ is a transversal for $Q/K$ | `proposed` | §4.2 | `step 3c`: the $p$ chains lie in $p$ different cosets of the set $M=H+C$, on every pair ($f$, line-direction subspace) |
| Step 3d | $[C:pC]=p$; (O) in $C$; each $A_n$ is a transversal for $C/pC$ | `proposed` | §4.2 | `step 3d`: $[C:pC]=p$ and one image under $\pi$ per coset of $pC$ (Run 0); orders on $C\setminus pC$ (Run 0, and $p\le7$ in the other runs); $A_n\subseteq C$ and $A_n$ a transversal, on every pair ($f$, line-direction subspace) |
| Steps 4–5 | $\lvert Y-Y\rvert\ge2p-1$, $\lvert A_n-A_m\rvert\ge2p-1$, count | `proposed` | §4.2 | `Lemma F (C)`, `Lemma F (Q)` (classes in $Q/K$ taken from the set $M$), `step 5` |
| Theorem 1 (a) | $\lvert T-T\rvert\ge(2p-1)^2$ | `proposed` | §4.2 | `L1(a)`; $p=3$ complete class, minimum 25 |
| Theorem 1 (b) | columns $\ge4p-2$, zero column $\ge2p-1$ | `proposed` | §4.3 | `L1(b)`; $p=3$ complete class, minimum 10 |
| Theorem 1 (c) | covering; line directions fill whole lines through $0$ | `proposed` | §4.4 | `Lemma G: ...` and `Cor L1c` on every $f$ tested |
| Corollary 2 | $\delta\ge3p^2-2$ | `proposed` | §5 | `C1: ...` on every tested $f$ with no line direction |
| Corollary 3 | Conjecture 6.2 $\Leftrightarrow$ the case with no line direction | `proposed` | §5 | no machine check (none needed: a logical consequence of Theorem 1 (a) and Lemmas A, E) |
| Corollary 4 | $\delta=25$ at $p=3$ | `proposed` | §5 | no machine check of the argument; the value agrees with the exhaustive value 25 (`scripts/out/rows.log`, part [3]) and with the source's own computation (§6.4 of the source) |
| Runs 0–6 | data checks of §7 | `numerical` | §7 | `scripts/out/` |

Not tested by the script at all: Lemma F for non-cyclic $Z$; the summing identity after §4.3; the remark on $p=2$ in §4.5 beyond the 64 functions of Run 6. None of these, and no other step, is used in the form of a computation.

**No step is open.** No step is known to fail, and no step rests on a computation.

## 7. Checks against data (`numerical`)

Script: `scripts/check_L1.py` (Python 3.12.10, standard library only, exact integer arithmetic, no floating point except in elapsed-time stamps). Each log starts with a header that gives the Python version and implementation, the platform, and the first 16 hex digits of the SHA-256 of the script that wrote it (`6be5f43954a27c0a`). The script shares no code with `scripts/rows.py` or with the source's companion repository.

The part `algebra` (Run 0) tests the statements that do not depend on $f$, directly from the definitions. For each $f$, the other parts recompute $T_f-T_f$ by literal subtraction in $(\mathbb{Z}/p^2)^2$ and the maps $d_uf$ from the definition with carries. They then run the checks listed in the "Check" column of §6, exactly as described there. This is not every step of §§3–5, and §6 names the steps with no machine check. The first failing check would be printed as `STEP FAILED -> <label>`. All runs ended with `RESULT: ALL CHECKS PASS`. No argument of §§1–5 depends on these runs. They show only that the written statements and the code agree on the data below.

| Run | What was run | Result (from the log) | Log |
| --- | --- | --- | --- |
| 0 | `algebra`: the statements that do not depend on $f$, for $p=2,3,5,7,11$ | Facts 1–3 on all $p^4$ elements of $G$; Lemma D (i)–(iv) for all $p^4-p^2$ elements outside $H$; for each of the $p(p+1)$ cyclic subgroups of order $p^2$ (6, 12, 30, 56, 132 of them, which are all of them): Lemma D (v), the last statement of Lemma G, and steps 3a, 3b, 3d; Lemma E: box totals 9, 25, 81, 169, 441, and $\lvert A_w(0)\rvert=2^{n(w)}$ for every $w$ | `scripts/out/check_algebra.log` |
| 1 | $p=3$, the **complete** class of functions covered by Theorem 1: every $f$ with $f(0)=0$ and at least one line direction, built constructively (for each of the 4 lines $\langle u\rangle$ through $0$ and each of the 3 cosets of $\langle u\rangle$: all offsets and all words) | 708,588 constructions, 704,214 distinct $f$; every check of §6 that applies to $f$ passes on every $f$. Histogram of $\lvert T-T\rvert$: 25: 4374, 27: 17496, 29: 17496, 31: 34992, 33: 52488, 35: 157464, 37: 244944, 39: 174960. Minima over the class: $\lvert T-T\rvert$ 25, column sum 10, $\lvert Y-Y\rvert$ 5, $\lvert A_n-A_m\rvert$ 5, differences per coset of $C$ 5. Line-direction subspaces per $f$: one for 699,840 functions, two for 4,374 | `scripts/out/check_p3class_0.log`, `check_p3class_1.log`, `check_p3class_2.log`, `check_p3class_3.log`, `check_p3merge.log`, `p3class_merged.json` |
| 1′ | comparison of Run 1 with an exhaustive scan of all $9^8$ functions with $f(0)=0$ by a separate program (`scripts/rows.py`, which uses NumPy) | the count 704,214 and the whole histogram are identical to `hist_some_line_direction` in `scripts/out/rows_p3.json`; column minimum 10 in both. Two independent code paths (scan and filter there, direct construction here) | `scripts/out/check_p3merge.log` |
| 2 | Lemma F, exhaustive over all pairs of transversals | $\mathbb{Z}/1$ (trivial): minimum 1; $\mathbb{Z}/4$, $\mathbb{Z}/8$, $\mathbb{Z}/16$ modulo the subgroup generated by $2$: minimum 3; $\mathbb{Z}/9$, $\mathbb{Z}/27$ modulo the subgroup generated by $3$: minimum 5; $\mathbb{Z}/25$ modulo the subgroup generated by $5$ (pairs normalised to contain 0): minimum 9; no violation of (ii) or (iii). Outside the hypothesis (O): $\mathbb{Z}/6$ modulo $\lbrace0,3\rbrace$ has minimum 3, below $2q-1=5$; $\mathbb{Z}/8$ modulo $\lbrace0,4\rbrace$ has minimum 7 | `scripts/out/check_lemmaF.log` |
| 3 | 70 stored functions at $p=5$ found by an earlier search (`scripts/out/rowword_p5_L88_0branch.json`; the search program is not part of this package and has not been reviewed) | all 70: literal $\lvert T-T\rvert=87$, no line direction, all $\lvert A_u\rvert\ge3$; the least number of cosets of a cyclic subgroup of order 25 covering $T$ is 6 (more than 5, as Lemma G requires for a function with no line direction). $87\ge73=3p^2-2$ | `scripts/out/check_stored.log` |
| 4 | stored functions with a line direction: 756 functions at $p=3$ (`rowword_p3_L30.json`); the box and the box with one corner moved at $p=5$; the two examples of `triangle_columns.json` | $p=3$: totals 25 (216 functions, two line subspaces), 27 (486), 29 (54), every check passes. $p=5$ box: 81, two line subspaces, least column sum 18. Corner-moved box ($f(4,4)=(-1,-1)$, else $0$): 97, no line direction. $p=5$ example with a column sum of 17 next to a direction whose image has three non-collinear points: total 85, line subspace $\langle(1,2)\rangle$, least column sum next to that line direction 19. $p=7$ example: total 191, line subspace $\langle(1,3)\rangle$, least column sum 29 | `scripts/out/check_stored.log` |
| 5 | random $f$ covered by Theorem 1 (half with 2 or 3 letters), seed 20261127, and as many uniformly random $f$ | $p=5$: 1500 + 1500, least total in the class 93; $p=7$: 200 + 200, least total 411; $p=11$: 10 + 10, least total 2765 (the order checks of steps 3b, 3d are skipped at $p=11$ in this run; Run 0 covers them); every other check passes on every $f$; all uniformly random $f$ had no line direction | `scripts/out/check_random_5_1500_20261127.log`, `check_random_7_200_20261127.log`, `check_random_11_10_20261127.log` |
| 6 | $p=2$, all 64 functions with $f(0)=0$ | 48 functions with $\lvert T-T\rvert=9$ (two line subspaces each), 16 with 13 (no line direction); minimum 9, as in Corollary 5.2 of the source | `scripts/out/check_p2.log` |

The class of Run 1 is restricted to $f(0)=0$. This loses nothing, because $f$ and $f-f(0)$ have the same images $A_u$ (proof of Corollary 3). Exact commands, versions and runtimes are in `REPRODUCE.md`.

## 8. What needs certification

**For Theorem 1 and Corollaries 2, 3, 4: nothing.** The arguments of §§1–5 contain no computation, no numerical constant other than integers produced by the displayed algebra, and no appeal to the data of §7. The runs of §7 stay `numerical`. They could be raised to `certified` only by an archived independent rebuild, which has not been done.

## 9. Sources, what is used from them, and credit

**From the source** ([arXiv:2606.27961v1](https://arxiv.org/abs/2606.27961), Barcau, Paşol, Ţurcaş):
- the setting, notation and Conjecture 6.2 (§6.1), including its equivalent function form;
- Lemma 6.1 (fibre decomposition): used, and re-proved above as Lemma A;
- Lemma 6.3: its cycle identity is used and re-proved as Lemma B; its consequences (1)–(2) are the case $\lvert A_u\rvert\le2$ of Lemma C;
- Proposition 5.3 (box upper bound): used, and re-proved as Lemma E;
- Theorem 4.2 and Propositions 3.2–3.3: not used; they are cited as an alternative reference for Lemma F in the cyclic case, and the proof of Lemma F adapts the singleton-direction argument of Proposition 3.2;
- Lemma 6.4 (two independent directions with $\lvert A_u\rvert=2$): **not used**; its conclusion is the special case of Theorem 1 (a) noted in §2;
- Theorem 6.5 ($\delta\ge3p^2-p-1$): **not used**; Corollary 2 follows its dichotomy (a strong case, else count three per direction) with Theorem 1 in place of Lemma 6.4;
- Corollary 5.2 ($\delta=9$ for $(\mathbb{Z}/4)^2$): used only as a consistency check (§4.5, Run 6);
- §6.4: the source states that it verified the conjecture for $p=3$ and $p=5$ by deterministic Python computations ($\delta=25$ and $\delta=81$), with code and certificates in the authors' repository [georgeturcasubb/transversals](https://github.com/georgeturcasubb/transversals). **So the value in Corollary 4 is already in the source**; what Corollary 4 adds is a proof without computation.

**From Leshner with Codex** ([open-math-agents pull request #6492](https://github.com/GuillaumeBAUD-coder/open-math-agents/pull/6492), opened 2026-11-27 at 12:56 UTC, head commit `ba804a2`; [README](https://github.com/rleshner/open-math-agents/blob/ba804a2813650e214c5172a1f484b1c1eda5edd8/research/transversal-seven/README.md), read as data on 2026-11-27): section "A projection bound for every odd prime" proves that if some $A_u$ lies in an affine line, then $\lvert T-T\rvert\ge(2p-1)^2$, by a basis change, a shear, a projection onto a cyclic transversal and Kneser's theorem. This is Theorem 1 (a), posted earlier on the same day as our work, which was done independently. Corollaries 2–4 follow from it by the count of §5. The pull request also claims a computer-assisted proof that $\delta=169$ at $p=7$ (not checked by us). **We claim no priority for Theorem 1 (a) or for the corollaries.**

**From the automath notes** ([chy4pro/automath, problems/tdn_2606_27961](https://github.com/chy4pro/automath/tree/5542184180d014b68637851941109dd5e584e920/problems/tdn_2606_27961); unpublished working notes, marked "park" in their [status sweep of 2026-09-25](https://github.com/chy4pro/automath/blob/5542184180d014b68637851941109dd5e584e920/notes/STATUS_SWEEP_20260925.md); read as data on 2026-11-27: [tdn_r4_column.out](https://github.com/chy4pro/automath/blob/5542184180d014b68637851941109dd5e584e920/problems/tdn_2606_27961/tdn_r4_column.out), the eleven-step chain quoted in [E42](https://github.com/chy4pro/automath/blob/5542184180d014b68637851941109dd5e584e920/engine/briefs/archive_v4/E42_tdn_r17_adversarial_chain.md), and the summary in [selection_0824.md](https://github.com/chy4pro/automath/blob/5542184180d014b68637851941109dd5e584e920/notes/selection/selection_0824.md)). They consist of a numerical log, an unreviewed proof sketch (written as a brief for a reviewer) and a status note; the status note (lines 36–40) calls the first item below a "provisional THEOREM". We located no complete written proof. Their round 4 states:
- the **one-2-direction theorem**: if some $u\ne0$ has $\lvert A_u\rvert=2$, then $\lvert T_f-T_f\rvert\ge(2p-1)^2$;
- in that case, the column bound $4p-2$ and a "per-coset budget" $2p-1$, obtained from the aperiodicity of a binary word of prime length (at most one exceptional shift); Lemma F (ii) and Theorem 1 (b) are the same kind of argument;
- the count $1+3(p^2-1)$ for the remaining branch with no direction of size 2, which is $25$ at $p=3$; their selection note records a hand proof of the case $p=3$, a trichotomy by the number (0, 1 or 2) of lines carrying directions of size 2, and that only their "0-branch" (all $\lvert A_w\rvert\ge3$) is open.

So **Corollaries 2 and 4 already follow from the statement in the automath notes by the same two-line count, and the reduction to a residual branch is stated there.** Compared with that line of work, the statement here replaces the hypothesis "$\lvert A_u\rvert=2$" by "$A_u$ lies in a line" (of any size), adds the reformulation Theorem 1 (c) by cosets of a cyclic subgroup, and therefore has a smaller residual class in Corollary 3 (no collinear image, instead of all $\lvert A_w\rvert\ge3$). We have not compared our proof with their sketch in detail. No file of theirs was executed or copied.

**From trureturing** ([issue #8487](https://github.com/the-omega-institute/trureturing/issues/8487), opened 2026-09-17, still open with no comments when checked on 2026-11-27): the residual inequality in the case where the directions with $\lvert A_u\rvert=2$ lie on one line through $0$, and a bounded, non-exhaustive local search at $p=7$ that found nothing below 169.

**Draft credit lines** (drafted for the human's approval; not yet approved, and the final release gate has not run):
- "The setting, the fibre decomposition, the cycle identity, the two-direction lemma, the bound $3p^2-p-1$ and the conjecture are due to Barcau, Paşol and Ţurcaş (arXiv:2606.27961)."
- "That a single direction with $\lvert A_u\rvert=2$ forces $(2p-1)^2$, with the column bound $4p-2$, the count $1+3(p^2-1)$ for the remaining branch (which gives $3p^2-2$ and settles $p=3$) and the reduction to a residual '0-branch', appears in the unpublished working notes of the chy4pro/automath project (round 4, 2026). The line-direction lemma extends that statement to every collinear image."
- "The residual inequality for collinear 2-directions was isolated in the-omega-institute/trureturing issue #8487."
- Proposed addition (not approved): "The line-direction lemma (if some $A_u$ lies in an affine line, then $\lvert T-T\rvert\ge(2p-1)^2$), and with it $\delta\ge3p^2-2$, was posted earlier on 2026-11-27 by Robert Leshner with Codex (open-math-agents pull request #6492); the proof here was found independently and avoids Kneser's theorem."

We make **no claim of priority or novelty**. The priority check must be re-run against both groups and the source's authors before any use of this text outside the private repository (`LITERATURE_CHECK.md`).

## 10. Formalization

Nothing is formalized in Lean yet. `LEAN.md` gives the plan: Lemma F, an intrinsic form of Theorem 1, the bridge to the source's notation, and Corollaries 2–4, with size estimates. All of §§1–5 is elementary finite group theory and counting, with no appeal to Kneser's theorem or to analysis.

## 11. Files

- `PROOF.md`: this file.
- `paper.tex`, `paper.pdf`: the same mathematics as an `amsart` paper (DOI [10.5281/zenodo.24594748](https://doi.org/10.5281/zenodo.24594748)). It numbers results by section; the correspondence of names is in `README.md`, "Names in the paper".
- `scripts/check_L1.py`: the checker of §7 (copy of the archived script, SHA-256 prefix `6be5f43954a27c0a`).
- `scripts/rows.py`: the separate exhaustive scan at $p=3$ used in Run 1′ (copy).
- `scripts/lint_proof.py`: formatting lint of this file (GitHub math rules, and that every log named here exists).
- `scripts/out/`: archived logs and JSON of the runs in §7, and the four input data files `rows_p3.json`, `rowword_p3_L30.json`, `rowword_p5_L88_0branch.json`, `triangle_columns.json`.
