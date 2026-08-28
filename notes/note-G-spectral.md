# Note G — Spectral attempt

*Plan §2.4.3. Status: **premise corrected; checkpoint written.** The note's
original blocker — that the spectral route has nothing to act on — is refuted
below: Duke–Friedlander–Iwaniec's proof is spectral and is about exactly this
repo's residues. The plan §2.5 deliverable, a quantitative statement of how far
current bounds fall short, is now written; it comes out as **two incommensurable
units**, not one number. The conjectural inequality itself is
[Note F](note-F-failure-localisation.md)'s Question F.*

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

## The Step 2 checkpoint: how far current bounds fall short

*Plan §2.5 asks for "a quantitative statement of how far current bounds fall
short". This is it. It is not one number. The shortfall has **two units that are
not commensurable**, and the one that is easiest to quote is the one that
matters least. All quotations below are from 300 dpi rasterisations of the Duke
scan, not its OCR layer.*

### DFI say what breaking parity requires, and it is the arbitrary form

> "It is now well-understood that information about L_d(M) is not sufficient to
> demonstrate asymptotic formulae for primes (or even their existence) due to a
> 'parity problem' [B]. In recent years this problem has been partially
> surmounted by adding new information about general bilinear forms of the type
> (8) B(M,N) = ΣΣ_{(m,n)=1} α_m β_n ρ_h(mn). **Here α_m and β_n are arbitrary
> but bounded complex numbers** with support M < m ≤ 2M and N < n ≤ 2N. In this
> paper we are able to obtain just barely enough information about the sums
> L_d(M) and B(M,N) to wipe out the parity problem in its entirety." (p. 425)

So the parity-breaking input is, in DFI's own statement of it, the
**arbitrary-coefficient** bilinear form. [Note F](note-F-failure-localisation.md)
proves that object admits **zero** cancellation for A = {x+i} at every split.
Note F is therefore not an obstacle *beside* the parity barrier; it is the
statement that DFI's parity-breaking input does not exist here.

Note what they prove versus what they need: Proposition 2, the bilinear estimate
they actually establish, opens "Suppose β_n are supported on primes" — a
restricted class. The arbitrary class is what (8) asks for.

### Unit 1 — the norm. A change of kind at fixed exponent.

DFI record what would be *plausible* and what they *achieve*:

> plausible: L_d(M) ≪ M^{1/2}(hdM)^ε  and  B(M,N) ≪ ‖α‖‖β‖(M+N)^{1/2}(hMN)^ε
> achieved (Prop. 1): L_d(M) ≪ (h,d)^{1/20}(d/M)^{1/20}M^{1+ε}   (p. 425)

Two gaps in one line. The saving is M^{−1/20} against a conjectured M^{−1/2} —
a factor of ten in the exponent — and, more importantly, **both are signed
bounds**. [`exp07`](../experiments/exp07_absolute_values.py) measures that for
this sequence the signed sum is under 2% of the absolute-value sum, so the
entire difficulty lives in a norm neither the achieved nor the plausible bound
addresses.

> **Shortfall: not an exponent. Σ_d |Σ_m ρ_h(dm)| against Σ_d Σ_m ρ_h(dm).**

And the axis that would have to improve is the one DFI single out as hopeless:

> "Here, a small improvement of the trivial estimate suffices for applications,
> but one needs a very large range of uniformity in d. Indeed, **any range that
> can reasonably be conjectured will always be too short**." (p. 425)

That is stronger than the Selberg-eigenvalue caution above, and it is about
exactly the uniformity in d that [Note J](note-J-mobius-in-progressions.md)'s
reduction needs.

### Unit 2 — the kind. Not an exponent at all.

Note J reduces the Type II input to a Bombieri–Vinogradov statement for
μ(x²+1) over progressions. Take the easiest endpoint, θ = 0 — no modulus, no
progression, no uniformity — and the required inequality is already

> |Σ_{x ≤ X} μ(x² + 1)| ≪ X(log X)^{−A}.

Teräväinen (arXiv:2010.07924v4, p. 2) on Chowla's Σ_{n≤x} λ(P(n)) = o(x):
it "is wide open for any polynomials with nonlinear irreducible factors".

> **Shortfall: the trivial bound has never been beaten by any amount, for the
> easiest special case of the statement we need.**

### Why the units matter more than any single figure

They are in increasing order of hopelessness and decreasing order of
measurability. A reader given only the exponent in unit 1 would conclude the
problem is close; a reader given unit 2 would conclude it is untouched. Both
readings come from the same reduction, which is why the checkpoint must state
both and refuse to average them.

**What would close it.** The conjectural inequality plan §2.5 asks for is
[Note F](note-F-failure-localisation.md)'s Question F, now sharpened by the
above: an absolute-value analogue of Proposition 1, uniform in d to moduli
X^{3/4}, with a log-power saving. Every clause of that is beyond current
technique, and the last two are beyond what DFI consider reasonably
conjecturable.

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

- *Two-parameter freedom smuggled in?* No. Everything here is about A = {x+i}.
- *Where is parity broken?* Nowhere, and this note now says why in the sources'
  own words: DFI's parity-breaking input is the **arbitrary-coefficient**
  bilinear form (8), and Note F proves that object has zero cancellation here.
  That is a sharper statement than "the spectral route fails" — it locates the
  failure at the exact hypothesis DFI identify as the one that beats parity.
- *Is the spectral finding over-read?* It was, once. This note originally said
  the spectral route was inapplicable, which was true of dispersion and false of
  spectral methods. The current claim is narrower: spectral methods reach the
  object, produce signed bounds, and the difficulty is in the absolute values.
- *Are the citations trustworthy?* Only after re-checking. Every page number
  here was off by one while the quotations were verbatim — the OCR layer of the
  Duke scan is unreliable and its page mapping was misread. Rasterise before
  citing. Anything in this repo still resting on that PDF's text layer should be
  treated as unverified.
- *Does the two-unit framing hide a third?* A level unit was proposed and
  withdrawn by the parallel session after re-reading Theorem S from the images:
  (34) needs D = x^{1/2−ε}, which Note B permits, so there is no level deficit.
  Both surviving units are bilinear.
