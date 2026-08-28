# Note G — Spectral attempt

*Plan §2.4.3. Status: **skeleton.** Nothing here is done. This note plus
[Note F](note-F-failure-localisation.md) form the Step 2 checkpoint (plan §2.5),
so the checkpoint is not met.*

## What this note is supposed to do

Reformulate the sum of [Note F](note-F-failure-localisation.md) via Kuznetsov
for PSL₂(Z[i]), determine what bound on Fourier coefficients or Kloosterman
sums would suffice, and compare against what is known (Motohashi,
Bruggeman–Motohashi, Sarnak).

## The problem this note faces before it starts

Note F found that the dispersion route produces **no Kloosterman sums at all**:
the Gram matrix G(n₁, n₂) is identically 0 or 1, so there is no congruence
condition, no additive-character detection, and nothing for a trace formula to
act on. The spectral machinery listed in plan §2.3 exists to estimate sums of
Kloosterman sums, and at present there are none in play.

So Note G cannot be executed as written. Either:

- **(a)** a *different* arrangement of the Type II sum produces genuine
  Kloosterman sums over Z[i] — in which case say which arrangement; or
- **(b)** the spectral route is inapplicable to this sequence, in which case
  that is itself the deliverable and Step 2's checkpoint needs restating.

Deciding between (a) and (b) is the first task. [Note
C](note-C-requirements.md) is now answered and sharpens the question rather
than settling it: the sum ASP actually wants is the one in (B), and at
A(x) = x^{1/2} its coefficient γ(n,C) is annihilated — so there is no
well-posed sum to reformulate spectrally *for ASP*. Any spectral attempt must
therefore first name a different sieve.

Cauchy–Schwarz in n has now been ruled out as an escape (see
[Note E](note-E-naive-dispersion.md)): the Gram matrix is ≤ 1 from that side
too. The only untested rearrangement is a well-factorable or unbalanced
decomposition of m that avoids squaring altogether.

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
