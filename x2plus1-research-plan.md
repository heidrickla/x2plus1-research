# Primes of the form x² + 1 — Research Plan

**Goal.** Build the foundation to attack Landau's fourth problem (x² + 1 prime infinitely often) via the Friedlander–Iwaniec asymptotic sieve for primes, reformulated over the Gaussian integers.

**Status of the problem.** Best known: Iwaniec (1978) — infinitely many x with x² + 1 having at most 2 prime factors. Barrier: parity (Selberg). Successful parity-breaking precedents: Friedlander–Iwaniec (a² + b⁴, density x^{3/4}), Heath-Brown (x³ + 2y³, density x^{2/3}). Target set has density x^{1/2}, thinner than anything yet handled.

**Working principle.** Do not try to prove the theorem. Try to locate the *exact lemma* in the a² + b⁴ argument that fails at density x^{1/2}. That lemma is the research problem.

---

## Step 1 — Reformulation over Z[i]

### 1.1 Objective
Express the problem as counting Gaussian primes on the line Im(z) = 1, and write down the sieve setup (the set A, its expected multiplicative structure, and the Type I / Type II inputs required).

### 1.2 Background to master
- Z[i]: units, UFD, splitting of rational primes (p = 2 ramified; p ≡ 3 mod 4 inert, never divides x²+1; p ≡ 1 mod 4 splits as ππ̄).
- Hecke characters λ_k(z) = (z/|z|)^{4k} and Hecke's theorem: angular equidistribution of Gaussian primes. Hecke L-functions L(s, λ_k).
- Equidistribution of Gaussian primes in sectors and in *thin* regions; understand why Im(z) = 1 is degenerate.
- The asymptotic sieve for primes (Friedlander–Iwaniec, *Opera de Cribro*, Ch. 25; original Annals 1998 paper). Know the exact hypotheses: Type I to level D, Type II bilinear estimate over the middle range, and the "sifting" bound that turns these into an asymptotic for primes.

### 1.3 Deliverables
1. **Note A — Dictionary.** One-page translation: x² + 1 = N(x + i); the set A = {x + i : x ≤ X} ⊂ Z[i]; A(d) := #{a ∈ A : d | a} for Gaussian ideals d; expected main term g(d) X with g the local density; identify ramified/inert/split contributions.
2. **Note B — Type I computation.** Prove the level of distribution for A: for which D does Σ_{N(d) ≤ D} |A(d) − g(d)X| = o(X)? Confirm D = X^{1/2 − ε} is the limit and pinpoint why (counting x ≤ X with x ≡ r mod N(d) loses when N(d) > X^{1/2}).
3. **Note C — Requirements table.** List the Type II range the asymptotic sieve needs *given* Type I level X^{1/2}. This determines exactly how strong a bilinear estimate Step 2 must deliver.
4. **Note D — Comparison ledger.** Same three items computed for a² + b⁴, side by side. Mark every line where the two-parameter freedom of (a, b) is used.

### 1.4 Reading
- Iwaniec–Kowalski, *Analytic Number Theory*: Ch. 3 (characters), Ch. 6 (sieve basics), Ch. 17 (sieve limits, parity).
- Friedlander–Iwaniec, *Opera de Cribro*: Ch. 24–25.
- Friedlander–Iwaniec, "The polynomial X² + Y⁴ captures its primes," Annals 148 (1998).
- Heath-Brown, "Primes represented by x³ + 2y³," Acta Math 186 (2001).

### 1.5 Checkpoint
Step 1 is done when Note C states a precise bilinear inequality (with ranges for m, n and a target saving) whose proof would imply the theorem via the asymptotic sieve.

---

## Step 2 — The bilinear (Type II) estimate

### 2.1 Objective
Prove, or identify the obstruction to, cancellation in
  S = Σ_{m} Σ_{n} α_m β_n · 1[mn ∈ A]
for arbitrary bounded coefficients α, β supported on Gaussian integers with N(m) ~ M, N(n) ~ N, MN ~ X, and M in the range specified by Note C.

### 2.2 Method template (dispersion)
1. Cauchy–Schwarz in m to remove α: |S|² ≤ ‖α‖² · Σ_m |Σ_n β_n 1[mn ∈ A]|².
2. Open the square: Σ_{n₁, n₂} β_{n₁} β̄_{n₂} #{m : mn₁ ∈ A, mn₂ ∈ A}.
3. Diagonal n₁ = n₂ gives the trivial bound; off-diagonal must show cancellation.
4. The condition mn₁, mn₂ ∈ A (both of the form x + i) becomes a congruence / lattice-point condition on m. Detect via additive characters → exponential sums over Z[i], or via Poisson summation → dual sums with Kloosterman-type terms.
5. Bound the resulting Kloosterman/Salié-type sums over Z[i] (Weil bound first; Deligne if higher-dimensional varieties appear).
6. Bookkeeping: total the losses; compare to the saving required by Note C.

### 2.3 Background to master
- Dispersion method: Linnik; Bombieri–Friedlander–Iwaniec I–III (Acta Math / Math. Ann. 1986–89); Iwaniec–Kowalski Ch. 11–12 (large sieve, Kloosterman sums).
- Exponential sums over number fields; Kloosterman sums for Z[i]; Weil bound in that setting.
- Shifted-convolution problems and where spectral methods enter.
- Spectral theory on hyperbolic 3-space: Bianchi groups PSL₂(Z[i]), Kuznetsov / Bruggeman–Motohashi trace formula, Kloosterman sums as Fourier coefficients. (Elstrodt–Grunewald–Mennicke; Motohashi's papers on Z[i] Kloosterman sums; Sarnak's "Kloosterman, quadratic forms and modular forms.")
- Level-of-distribution-beyond-1/2 techniques: Zhang (2014), Polymath 8, Maynard — specifically how they exploit *well-factorable* weights and Deligne bounds, and whether analogs exist over Z[i].

### 2.4 Deliverables
1. **Note E — Naïve dispersion run.** Execute 2.2 with the Weil bound only. Record the final exponent. (Prediction: fails; determine by how much.)
2. **Note F — Failure localisation.** State the single off-diagonal sum whose bound is insufficient. Write it in cleanest form (this becomes the "problem statement").
3. **Note G — Spectral attempt.** Reformulate the sum in Note F via Kuznetsov for PSL₂(Z[i]); determine what bound on Fourier coefficients / Kloosterman sums would suffice. Compare with known results (Motohashi, Bruggeman–Motohashi, Sarnak).
4. **Note H — Numerical pilot.** Compute S for moderate X with random bounded coefficients; measure the observed cancellation exponent. Use to sanity-check whether the target saving in Note C is even plausible (i.e., whether the obstruction is technical or structural).
5. **Note I — a² + b⁴ replay.** Run the same dispersion on the a² + b⁴ set and confirm reproduction of the Friedlander–Iwaniec Type II bound. Diff against Note E line by line.

### 2.5 Checkpoint
Step 2 is done when Note F + Note G together give a clean conjectural inequality over Z[i] (an estimate for a specific sum of Kloosterman sums or spectral coefficients) that implies the theorem, together with a quantitative statement of how far current bounds fall short.

---

---

## Where Steps 1 and 2 landed

*Added after Steps 1–2 were worked through. The working principle above — locate
the exact lemma that fails at density x^{1/2}, rather than attempt the theorem —
was followed, and it succeeded. The lemma was found, and it is not repairable
inside the framework.*

**Note F's C₄-free lemma.** For A = {x+i}, G(n₁,n₂) = #{m : mn₁, mn₂ ∈ A} ≤ 1
over Z[i], and Theorem O.12 gives G′ ≤ 1 over Z on the doubly-banded
configuration. So the off-diagonal term in 2.2 step 3 has no main term to
separate from an error term: the quantity a dispersion argument needs to average
is a 0/1 indicator.

**And that configuration is the one the literature quantifies over.**
Ford–Maynard's (II) has arbitrary divisor-bounded coefficients, so it implies its
own doubly-banded restriction; and their J ⊆ (x/2, x] confines the shared
variable to a factor-2 window by their own definition. Their footnote 2 (p. 7)
names this counting function as the barrier. With ν = 0 forced by Selberg,
C⁻ = 0 — which closes *infinitude*, not merely the asymptotic.

**Scope.** This is a theorem about what the Type I/II axioms can prove. It says
nothing about whether x²+1 is prime infinitely often, and the two must never be
conflated. Steps 1 and 2 are therefore complete in the only sense available: the
obstruction is located, named, and shown to be structural rather than technical.

**What is left is one Diophantine question**, below.

---

## Step 3 — The bipartite Diophantine problem

### 3.1 Objective

The incidence underlying Note F is a **bipartite Diophantine tuple**. Writing
a·m = x²+1 for a cofactor a and modulus m, the pair (a, m) satisfies
**a·m − 1 = x²**, so a set of cofactors A and a set of moduli B with every
product a·m of the form x²+1 is exactly a tuple with property **BD₂(−1)** in the
sense of Tsang–Yip. Two targets, and they are not the same problem:

1. **The unrestricted question (the literature's).** Is min{|A|, |B|} bounded by
   an absolute constant for BD₂(−1)? Tsang–Yip's Theorem 1.1 settles k ≥ 3; for
   k = 2 they state plainly that no upper bound on ℓ is known. Measured here:
   ℓ = 3, exhaustively to X = 9000.
2. **The windowed question (this project's).** Conjecture O.2 — can one dyadic
   window hold three shared moduli of a single cofactor pair? This is what the
   Type II obstruction actually needs, and it is weaker than (1) in the shared
   variable and stronger in the constraint on it.

Neither is needed to close Steps 1–2. Both are now the live mathematics.

### 3.2 Background to master

- Diophantine m-tuples and D(n)-sets; M_k(n) and the bounds M_k(n) ≪_k log(|n|+1).
  The resolved cases: M₂(1) = 4 (He–Togbé–Ziegler), **M₂(−1) = 3**
  (Bonciocat–Cipu–Mignotte).
- Bipartite tuples BD_k(n) (Tsang–Yip); the same objects in Bugeaud–Dujella and
  Bugeaud–Gyarmati two decades earlier.
- **Gap principles** — Dujella's; c > 4ab for regular quadruples; the
  by-range extension counts for a triple.
- **Linear forms in logarithms, Baker's method, Baker–Davenport reduction**
  (Dujella–Pethő, "A generalization of a theorem of Baker and Davenport").
  *This is the field's standard tool and this project has never used it.* Note O
  concluded that any proof must be about occupancy rather than congruences, and
  that size arguments cannot reach O.2; Baker's method is neither.
- Nagell, Theorem 108a: solution classes of a generalized Pell equation, with
  bounded fundamental solutions. Note O uses the same decomposition (Prop L.1's
  orbits) and recorded Nagell as "running the wrong way"; Dujella uses it to
  *classify*, not to bound from below.
- The uniformity conjecture (Bombieri–Lang) and what it predicts here: ℓ ≤ 5 for
  k = 2, via hyperelliptic y² = (a₁x+n)···(a₅x+n).

### 3.3 Deliverables

1. **Note P — method record.** *(exists)* The failure taxonomy behind CLAUDE.md's
   rules. Not mathematics; keep it current.
2. **Note Q — the dictionary.** Translate Note O's vocabulary into the m-tuple
   literature's and back: cofactor/modulus ↔ element/extension; multiplier τ ↔ ?;
   automorph ε ↔ the Pell recursion; "window" ↔ a constraint the literature does
   not appear to impose. State precisely which of the two targets each of
   O.4–O.18 bears on.
3. **Note R — literature audit.** For each result in the O-thread, is it known?
   Priority order: the gap principles (O.4, O.13, O.15), the per-prime sign
   criterion (O.17), and the ℓ = 3 structure. **This gates any writing up.**
4. **Note S — Baker attempt.** Set up the linear form in logarithms for two
   solutions of aY² − bX² = M·D lying in one window, and reduce. Determine what
   it gives, even weakly. This is the tool the project has not tried.
5. **Note T — the ℓ = 3 evidence, presented.** The exhaustive K₃,₃ search, the
   sharp K₃,₂ cutoff, the unit-free witness, the mod-4 side constraint — as data
   on an open question, with the searches' populations stated.

### 3.4 Reading

- Tsang–Yip, "Bipartite Diophantine tuples and their applications,"
  arXiv:2512.03441 — definition, Theorem 1.1, Question 1.3.
- Bonciocat–Cipu–Mignotte, "There is no Diophantine D(−1)-quadruple,"
  arXiv:2010.09200.
- Dujella, "An absolute bound for the size of Diophantine m-tuples" — the Pell
  system, Nagell's classification, the congruences mod 2c.
- Dujella–Pethő, "A generalization of a theorem of Baker and Davenport" (1998).
- Bugeaud–Dujella on special bipartite families.
- Dujella's book on Diophantine m-tuples (Tsang–Yip ref. [17]) and his
  bibliography at web.math.pmf.unizg.hr/~duje/ref.html (≈596 entries).

### 3.5 Checkpoint

Step 3 is done when **Note R** reports, result by result, which parts of the
O-thread are known and which are not — because that decides whether there is a
paper — **and** Note S records what a Baker-method attempt yields, even if the
answer is that it does not reach the windowed configuration.

*Not a checkpoint: proving O.2. It is open, nine routes are closed with reasons,
and the honest position is that it needs a tool this project has not used.*

---

## Cross-cutting

- **Literature scan** before each note: arXiv (math.NT), search terms "x^2+1 primes", "Gaussian primes thin set", "bilinear forms Gaussian integers", "Landau problems sieve". Confirm nothing supersedes Iwaniec 1978 / Friedlander–Iwaniec 1998.
- **And for Step 3, a different set of terms**, because the object has a name in another literature: "Diophantine m-tuple", "D(-1)-tuple", "bipartite Diophantine tuple", "gap principle", "simultaneous Pell equations", "Baker–Davenport reduction". *This scan was skipped for two months and the O-thread was built without it; when it was finally run it identified the object immediately.* Run it **before** extending Note O, not after.
- **Adversarial review** of every note: what two-parameter freedom is being smuggled in? Where is parity actually being broken?
- **Don't** pursue Green–Tao / nilsequence methods; single-variable polynomials are outside their scope.
- **Don't** expect GRH or zero-density results to substitute for Type II; they control primes in progressions, not in the sparse sequence.
- **Don't** treat a result in Note O as new until Note R says so. The nine closed routes, the gap principles and the sign criteria all live in an area with ~596 catalogued references and two decades of work on the same equations.
- **Do** state which of the two Step 3 targets any new result bears on. The unrestricted question and the windowed one are different problems, and a result about one is not evidence about the other.

## Reading list (ordered)
1. Iwaniec–Kowalski, *Analytic Number Theory* — Ch. 3, 6, 11, 12, 17.
2. Friedlander–Iwaniec, *Opera de Cribro* — Ch. 24, 25.
3. Friedlander–Iwaniec, Annals 1998 (a² + b⁴).
4. Heath-Brown, Acta Math 2001 (x³ + 2y³).
5. Iwaniec, "Almost-primes represented by quadratic polynomials," Invent. Math. 47 (1978).
6. Bombieri–Friedlander–Iwaniec, "Primes in arithmetic progressions to large moduli" I–III.
7. Elstrodt–Grunewald–Mennicke, *Groups Acting on Hyperbolic 3-Space*.
8. Motohashi, "Trace formula over the hyperbolic upper half space" and related Z[i] Kloosterman papers.
9. Zhang (2014); Polymath 8a/8b; Maynard, "Small gaps between primes."

**Step 3 additions.**
10. Tsang–Yip, "Bipartite Diophantine tuples and their applications," arXiv:2512.03441 — the definition of BD_k(n), Theorem 1.1 (k ≥ 3), and Question 1.3 with its k = 2 gap.
11. Bonciocat–Cipu–Mignotte, "There is no Diophantine D(−1)-quadruple," arXiv:2010.09200.
12. Dujella, "An absolute bound for the size of Diophantine m-tuples" — the Pellian system, Nagell's classification, congruences mod 2c.
13. Dujella–Pethő, "A generalization of a theorem of Baker and Davenport" (1998) — the reduction this project has not attempted.
14. Bugeaud–Dujella; Bugeaud–Gyarmati — the same bipartite objects, two decades earlier.
15. Dujella, *Diophantine m-tuples* (book), and his bibliography web.math.pmf.unizg.hr/~duje/ref.html (≈596 entries).
