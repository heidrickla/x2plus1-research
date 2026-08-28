# Note G — Spectral attempt

*Plan §2.4.3. Status: **premise corrected, deliverable not written.** The note's
original blocker — that the spectral route has nothing to act on — is refuted
below: Duke–Friedlander–Iwaniec's proof is spectral and is about exactly this
repo's residues. What is *not* done is the plan's actual deliverable, a
conjectural inequality with a quantitative statement of how far current bounds
fall short. This note plus [Note F](note-F-failure-localisation.md) form the
Step 2 checkpoint (plan §2.5), so the checkpoint is still not met.*

## What this note is supposed to do

Reformulate the sum of [Note F](note-F-failure-localisation.md) via Kuznetsov
for PSL₂(Z[i]), determine what bound on Fourier coefficients or Kloosterman
sums would suffice, and compare against what is known (Motohashi,
Bruggeman–Motohashi, Sarnak).

## Corrected premise: spectral methods already reach these residues

*This note previously said the spectral route had nothing to act on, because
dispersion produces no Kloosterman sums here. That is true of **dispersion** and
false as a verdict on **spectral methods**, and the difference matters.*

*Page numbers here were off by one until checked against 300 dpi rasterisations
of the Duke scan rather than its OCR layer. The quotations were verbatim; the
citations were not. Anything else in this repo taken from that PDF's text layer
should be re-checked the same way — `pymupdf.open(path)[n].get_pixmap(dpi=300)`,
where scan index n is article page n + 422.*

Duke–Friedlander–Iwaniec's proof is spectral, and it is about exactly this
repo's residues — the roots of ν² + 1 ≡ 0. They relate the roots directly to the
Laplacian spectrum via Poincaré series, quoting from the paper:

> "For the proof of Proposition 1 we could transform C_d(M) into sums of
> Kloosterman sums (using Hooley's idea of relating the solutions of quadratic
> congruences to representations of the modulus by quadratic forms) and then
> employ estimates from the spectral theory of automorphic forms." (p. 426)

> "…roots of the congruence to the spectrum of the Laplacian **without passing
> through Kloosterman sums along the way**, although the Weil bound for the
> latter will ultimately be used." (p. 426)

> "§3. Estimation of the Poincaré series. … we use the spectral expansion which
> leads to the result in a less circuitous fashion. … the spectral theorem gives
> P(z) = Σ(P, u_j)u_j(z) + Σ_a ∫ (P, E_a(·, ½+it)) E_a(z, ½+it) dt, where
> {u_j(z)} is an orthonormal system of **Maass cusp forms**…" (p. 428)

So the machinery does not need dispersion to produce Kloosterman sums for it. It
reaches the arithmetic object directly. **Option (b) below — "the spectral route
is inapplicable" — is refuted.**

## But it delivers the wrong norm, which is the same wall as before

What the spectral argument produces is Proposition 1: a bound on

> L_d(M) = Σ_{M<m≤2M} ρ_h(dm) ≪ (h,d)^{1/20}(d/M)^{1/20}M^{1+ε},

a **signed** sum over the roots. [Note J](note-J-mobius-in-progressions.md)'s
`exp07` measures that the Type II difficulty is entirely in the **absolute
values** — the signed sum is under 2% of the absolute-value sum. So spectral
methods are not an independent route: **they are the engine behind Proposition
1**, which is already filed as the right object in the wrong norm.

Two further cautions, both from DFI themselves:

- **Selberg's eigenvalue conjecture would not extend the range.** "Implicitly …
  we use the fact that the exceptional eigenvalues are few in number and Weil's
  estimate for Kloosterman sums takes care of any that might be there. If we
  knew these did not exist (as conjectured by Selberg) we could arrange our
  arguments differently. This would yield sharper estimates but **the same range
  of uniformity** and hence would be of no advantage for our applications."
  (p. 426). Uniformity in d is precisely what this repo needs — moduli to
  X^{3/4} — so the obvious strengthening buys nothing on the axis that matters.
- **The saving is tiny.** The exponent 1/20 in Proposition 1 indicates heavy
  loss in the argument. Even before the norm question, there is little room.

## Revised verdict

The spectral route is **better positioned than this note assumed** — it reaches
the object, in the literature, already — and **worse positioned than one would
hope**: it yields signed bounds where the difficulty is in the absolute values,
and its natural strengthening does not extend uniformity in d.

The well-posed question it leaves is narrow and worth stating:

> **Is there a spectral route to Σ_d |Σ_m ρ_h(dm)|, rather than to the signed
> sum?** That is not a question about Kuznetsov versus Bruggeman–Motohashi; it
> is the question of whether the absolute values can be handled at all, which is
> [Note F](note-F-failure-localisation.md)'s obstruction in spectral clothing.

## Background still to master (plan §2.3)

- [ ] Kloosterman sums for Z[i]; the Weil bound in that setting.
- [ ] Spectral theory on hyperbolic 3-space; Bianchi groups PSL₂(Z[i]).
- [ ] Kuznetsov / Bruggeman–Motohashi trace formula over Z[i].
- [ ] Whether well-factorable weights and Deligne bounds (Zhang, Polymath 8,
      Maynard) have Z[i] analogues.

## Deliverable when unblocked

Per plan §2.5: a clean conjectural inequality over Z[i] — an estimate for a
specific sum of Kloosterman sums or spectral coefficients — that implies the
theorem, **together with a quantitative statement of how far current bounds
fall short**. Note F supplies a candidate inequality (Question F) but not the
second half; supplying it is this note's job.

## Adversarial review

*Not applicable — no content yet.*
