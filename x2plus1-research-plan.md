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

## Cross-cutting

- **Literature scan** before each note: arXiv (math.NT), search terms "x^2+1 primes", "Gaussian primes thin set", "bilinear forms Gaussian integers", "Landau problems sieve". Confirm nothing supersedes Iwaniec 1978 / Friedlander–Iwaniec 1998.
- **Adversarial review** of every note: what two-parameter freedom is being smuggled in? Where is parity actually being broken?
- **Don't** pursue Green–Tao / nilsequence methods; single-variable polynomials are outside their scope.
- **Don't** expect GRH or zero-density results to substitute for Type II; they control primes in progressions, not in the sparse sequence.

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
