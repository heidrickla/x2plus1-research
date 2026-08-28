# Note C — Requirements table

*Plan §1.3.3. Status: **skeleton — blocked.** This note is the Step 1 checkpoint
(plan §1.5) and cannot be completed from memory. Every `**[VERIFY]**` below must
be filled from the source with a page reference before the note is anything but
a form.*

## Why this note is deliberately empty

The plan's working principle is to locate the *exact* lemma that fails. That
requires the *exact* hypotheses of the asymptotic sieve for primes — not a
remembered approximation of them. Writing plausible-looking exponents here
would defeat the entire purpose of the exercise, so they are left blank.

Sources to quote:
- Friedlander & Iwaniec, "Asymptotic sieve for primes", *Ann. of Math.* **148**
  (1998), 1041–1065.
- Friedlander & Iwaniec, *Opera de Cribro*, Ch. 25.

## The form to fill

Let a_n ≥ 0 be supported on n ≤ Q, A(Q) = Σ a_n, A_d(Q) = Σ_{d | n} a_n.

### Hypothesis R (Type I)

> Σ_{d ≤ D} |A_d(Q) − g(d)A(Q)| ≤ A(Q)·(log Q)^{−E}, for D = Q^{θ₁}.

| slot | value | source |
|---|---|---|
| θ₁ (required Type I level) | **[VERIFY]** | |
| E (log-saving exponent) | **[VERIFY]** | |
| conditions on g (multiplicativity, size) | **[VERIFY]** | |

### Hypothesis B (Type II)

> Σ_{m} \| Σ_{N < n ≤ 2N, (n,m)=1} μ(n) a_{mn} \| ≤ A(Q)·(log Q)^{−F}

| slot | value | source |
|---|---|---|
| range of N required | **[VERIFY]** | |
| F | **[VERIFY]** | |
| is α_m genuinely arbitrary, or structured? | **[VERIFY]** | |
| is β = μ, or a general well-factorable weight? | **[VERIFY]** | |

### Conclusion delivered

| slot | value | source |
|---|---|---|
| form of the prime asymptotic | **[VERIFY]** | |
| whether the conclusion is asymptotic or lower-bound only | **[VERIFY]** | |

## What we already know goes into the form

From [Note B](note-B-type-I.md), for A = {x + i}: **θ₁ = 1/2 and no more**, by a
sharp argument. So the first question this note answers is binary:

> **Is θ₁ = 1/2 enough for the asymptotic sieve for primes?**

If the sieve requires θ₁ > 1/2 (and Q^{2/3} is the figure that needs checking),
then Step 1 has already found a second obstruction, independent of and prior to
the Type II problem — and the plan's Step 2 would be attacking the wrong half.
That would be a significant redirection, which is why this must be checked
before any more Step 2 work.

From [Note H](note-H-numerical-pilot.md), the Type II sum is measured at
≍ √(MX) = Q^{(1+u)/4}·… , which is o(A(Q)) precisely for M = o(X) = o(Q^{1/2}).
So the Type II range available also stops at Q^{1/2}.

**Both hypotheses cap at Q^{1/2}.** Whether the sieve's required ranges overlap
that cap is the whole of Note C.

## Deliverable when unblocked

Per plan §1.5: a precise bilinear inequality, with ranges for m and n and a
target saving, whose proof would imply the theorem. [Note
F](note-F-failure-localisation.md)'s Question F is the current best guess at
its shape; it becomes the deliverable once the ranges above are real.

## Adversarial review

*Not applicable until the note has content. When it does: check specifically
whether the version of the sieve being quoted assumes a_n supported on
squarefree n, or a divisor-bounded majorant — either could silently exclude
x² + 1, whose values are frequently non-squarefree.*
