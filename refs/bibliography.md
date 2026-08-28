# Bibliography

Ordered as in the plan's reading list. PDFs are gitignored (`refs/pdf/`);
this file carries the citations and what each source is needed *for*.

## Primary

1. **Iwaniec & Kowalski**, *Analytic Number Theory*, AMS Colloq. Publ. 53 (2004).
   Ch. 3 (characters), Ch. 6 (sieve basics), Ch. 11–12 (large sieve, Kloosterman
   sums), Ch. 17 (sieve limits, parity).
2. **Friedlander & Iwaniec**, *Opera de Cribro*, AMS Colloq. Publ. 57 (2010).
   Ch. 24–25. The book version of the asymptotic sieve for primes; Note C
   quotes the 1998 Annals papers instead, so this is a cross-check rather than
   a dependency.
3. **Friedlander & Iwaniec**, "The polynomial X² + Y⁴ captures its primes",
   *Ann. of Math.* **148** (1998), 945–1040.
   [arXiv:math/9811185](https://arxiv.org/abs/math/9811185). **Read** (§2 axioms
   pp. 953–954; Prop. 3.5 level of distribution p. 962; Prop. 4.1 bilinear range
   p. 963).
4. **Friedlander & Iwaniec**, "Asymptotic sieve for primes",
   *Ann. of Math.* **148** (1998), 1041–1065. The sieve axioms themselves.
   [arXiv:math/9811186](https://arxiv.org/abs/math/9811186). **Read**
   (hypotheses (R), (R1), (B), (B1–3) pp. 1042–1044; Theorem 1 p. 1044;
   Theorem 2 and (9.1)–(9.3), (R3) p. 1059). Quoted in
   [Note C](../notes/note-C-requirements.md).
5. **Heath-Brown**, "Primes represented by x³ + 2y³", *Acta Math.* **186**
   (2001), 1–84. **Read** via the open
   [Oxford ORA copy](https://ora.ox.ac.uk/objects/uuid:ebb25eb4-a19e-4049-8117-3269e140b0fe)
   (76-pp. preprint; page numbers cited from it, not the Acta pagination).
   Load-bearing: the α(f) density exponent and the 1 / ¾ / ⅔ / ½ hierarchy
   (p. 2); the statement that FI's (R1) "is not quite met in our case" and
   "might be relaxed" (p. 3); level of distribution X^{2−ε} (Lemmas 2.1–2.2,
   p. 5); Type II range X^{1+ε} ≪ V ≪ X^{3/2−ε} (p. 5).
6. **Iwaniec**, "Almost-primes represented by quadratic polynomials",
   *Invent. Math.* **47** (1978), 171–188. The current record for x² + 1: P₂.
   **Original not obtained** — paywalled ([Springer](https://link.springer.com/article/10.1007/BF01578070),
   [EUDML](https://eudml.org/doc/142575)). Statement and method read instead
   from an exposition: V. Kapoor, *Almost-Primes Represented by Quadratic
   Polynomials* (MSc essay, UBC 2006),
   [arXiv:1910.02885](https://arxiv.org/abs/1910.02885). Treat any detail
   sourced from it as second-hand until the original is checked.
7. **Bombieri, Friedlander & Iwaniec**, "Primes in arithmetic progressions to
   large moduli" I, *Acta Math.* **156** (1986); II, *Math. Ann.* **277**
   (1987); III, *J. Amer. Math. Soc.* **2** (1989). **Not obtained** (paywalled)
   and **deprioritised** — see the note on items 7 and 12–14 below.

## Z[i] spectral theory (Step 2, Note G)

8. **Elstrodt, Grunewald & Mennicke**, *Groups Acting on Hyperbolic Space*,
   Springer (1998). Bianchi groups, PSL₂(Z[i]). **Not obtained** (book) and
   **deprioritised** — see the note on items 8–11 below.
9. **Motohashi**, "Trace formula over the hyperbolic upper half space", and
   related work on Kloosterman sums over Z[i].
10. **Bruggeman & Motohashi**, sum formula for PSL₂(Z[i]) / Bianchi groups.
11. **Sarnak**, "Kloosterman, quadratic forms and modular forms",
    *Nieuw Arch. Wiskd.* (2000).

## Level of distribution beyond 1/2

12. **Zhang**, "Bounded gaps between primes", *Ann. of Math.* **179** (2014).
13. **Polymath 8a**, "New equidistribution estimates of Zhang type".
14. **Maynard**, "Small gaps between primes", *Ann. of Math.* **181** (2015).

Needed specifically for: well-factorable weights, Deligne bounds, and whether
either has an analogue over Z[i].

## Post-2001, found by the supersession scan

15. **Green & Sawhney**, "Primes of the form p² + nq²",
    [arXiv:2410.04189](https://arxiv.org/abs/2410.04189) (2024). For n ≡ 0, 4
    (mod 6): infinitely many primes p² + nq² with p, q both prime, with an
    asymptotic; n = 4 settles Friedlander–Iwaniec's "Gaussian primes
    conjecture". Type I/II over **Q(√−n)**; the Type II input is Gowers-norm
    technology. **Unread — highest priority.** Note that it cuts against the
    plan's exclusion of Green–Tao methods (§Cross-cutting).
16. **"On Gaussian primes in sparse sets"**,
    [arXiv:2302.11331](https://arxiv.org/abs/2302.11331). Primes a² + b² with
    b in a set of size X^{1/2−δ}. Our problem is that set having one element.
    Unread.
17. **"On the theory of prime producing sieves"**,
    [arXiv:2407.14368](https://arxiv.org/abs/2407.14368). Likeliest place for a
    restated or relaxed (R1). Unread.
18. **"The polynomials X²+(Y²+1)² and X²+(Y³+Z³)² also capture their primes"**,
    [arXiv:2112.03617](https://arxiv.org/abs/2112.03617). Note the inner
    y² + 1; α is still 3/4. Unread.
19. **Pintz**, "Landau's problems on primes" — survey,
    [renyi.hu](https://www.renyi.hu/~pintz/pjapr.pdf). Not read; the obvious
    place to check the state of the art on all four problems at once.

## Also worth having

- **Hecke**, on the angular equidistribution of Gaussian primes (Note A §1.2).
  Narrow-sector refinements: Ricci (unconditional, width X^{−3/10+ε}) and
  X^{−1/2+ε} under GRH. Figures from a search, not from the sources; they are
  context only — nothing in the repo rests on them.
- **Selberg**, on the parity phenomenon — the barrier being broken.


## PDFs

`refs/pdf/` holds locally fetched copies and is **gitignored** — the papers are
copyrighted. Re-fetch from the arXiv links above. Extract text with `pypdf`;
`pdftoppm` is not installed, so the Read tool cannot render these directly.


---

## Why items 7–11 have not been chased

Recorded so a later reader does not mistake absence for oversight.

**Items 8–11 (EGM; Motohashi; Bruggeman–Motohashi; Sarnak) — spectral theory
over Z[i].** This machinery estimates sums of Kloosterman sums.
[Note F](../notes/note-F-failure-localisation.md) proves that for A = {x + i}
the Gram matrix G(n₁,n₂) = #{m : mn₁, mn₂ ∈ A} is identically 0 or 1, so the
dispersion route produces **no Kloosterman sums to estimate**. Until
[Note G](../notes/note-G-spectral.md) settles whether a *different* arrangement
of the Type II sum generates them, there is nothing for these sources to act on.
Reading them first would be reading a tool before knowing there is a job.

**Items 7 and 12–14 (BFI I–III; Zhang; Polymath 8; Maynard) — level of
distribution beyond 1/2.** These raise the level for **primes in arithmetic
progressions** — BFI to x^{4/7−ε}, and Iwaniec's well-factorable weights to
x^{7/12−ε}. That is a sequence of density x/log x. The cap this project faces
is different in kind: for a sequence of size |A| the number of admissible
moduli of norm ≤ D is ≍ D, so once D exceeds |A| the moduli outnumber the
sequence and Σ|r_d| cannot be small
([Note B](../notes/note-B-type-I.md)). FI state the same thing outright
([ASP] p. 1044): *"for thin sequences A one cannot expect (R) to hold with
D(x) > A(x)"*. Well-factorable weights redistribute moduli; they do not
manufacture sequence elements, so they cannot lift a counting bound.

This is reasoning, not a reading of BFI/Zhang/Maynard — **[VERIFY]** if the
conclusion ever becomes load-bearing. The plan itself makes the parallel point
for GRH and zero-density results (§Cross-cutting, last bullet).
