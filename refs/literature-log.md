# Literature scan log

The plan requires a scan *before each note* (§Cross-cutting). Record each scan
here so a later reader knows what was and was not checked, and when.

Search terms to run each time (arXiv math.NT, MathSciNet, Google Scholar):
`x^2+1 primes`, `Gaussian primes thin set`, `bilinear forms Gaussian integers`,
`Landau problems sieve`, `asymptotic sieve for primes`, `parity barrier`.

The specific question each scan must answer: **does anything supersede
Iwaniec 1978 (P₂ for x²+1) or Friedlander–Iwaniec 1998?**

| date | before note | terms run | result | superseded? |
|---|---|---|---|---|
| 2026-08-27 | C | `Friedlander Iwaniec asymptotic sieve for primes hypotheses`; `X^2+Y^4 captures its primes arXiv` | Both 1998 Annals papers located as arXiv preprints and read directly. | not checked |
| 2026-08-27 | C (rev.) | `Heath-Brown primes represented by x^3+2y^3 pdf`; `Iwaniec 1978 almost-primes quadratic polynomials`; `relaxing FI hypothesis (R1) level of distribution thin sequences` | [HB] obtained and read (Oxford ORA). Iwaniec 1978 paywalled — read via an MSc exposition. No work found relaxing (R1). | not yet |
| 2026-08-27 | **supersession scan** | `primes x^2+1 Landau progress since Iwaniec 1978`; `Green Sawhney primes p^2+4q^2`; `Hecke Gaussian primes narrow sectors` | **Run.** Iwaniec 1978 still stands for x²+1. Two significant nearby results found — see below. | **no** |

## Standing entries

### 2026-08-27 — sources obtained and read

- **[ASP]** [arXiv:math/9811186](https://arxiv.org/abs/math/9811186) —
  Friedlander & Iwaniec, "Asymptotic sieve for primes", *Ann. of Math.* **148**
  (1998), 1041–1065. Hypotheses read at pp. 1041–1044; Theorem 2 and the
  non-squarefree conditions at p. 1059.
- **[X2Y4]** [arXiv:math/9811185](https://arxiv.org/abs/math/9811185) —
  Friedlander & Iwaniec, "The polynomial X²+Y⁴ captures its primes",
  *Ann. of Math.* **148** (1998), 945–1040. Applied axioms at pp. 953–954;
  level of distribution (Prop. 3.5) at p. 962; bilinear range (Prop. 4.1) at
  p. 963.

PDFs are in `refs/pdf/` and are **gitignored** (copyright). Re-fetch from arXiv
if missing. Text extraction: `pypdf`, e.g.

```bash
python -c "from pypdf import PdfReader; print(PdfReader('refs/pdf/FI-asymptotic-sieve-for-primes.pdf').pages[2].extract_text())"
```

### 2026-08-27 (second pass) — reading list items 4–9

- **[HB]** Heath-Brown, *Primes represented by x³+2y³* — **read**. Answered the
  standing [VERIFY] in [Note C](../notes/note-C-requirements.md): he does *not*
  use [ASP], because (R1) "is not quite met", and he judged it likely relaxable.
  This reversed the previous turn's conclusion that Step 2 was the wrong half.
- **Iwaniec 1978** — original paywalled; statement and method taken from
  V. Kapoor's MSc exposition ([arXiv:1910.02885](https://arxiv.org/abs/1910.02885)).
  Second-hand; flagged as such in the bibliography.
- **BFI I–III, EGM, Motohashi, Zhang/Polymath/Maynard** — not obtained, and
  deliberately deprioritised. The reasoning is written out at the end of
  [refs/bibliography.md](bibliography.md); it is reasoning, not a reading.

### 2026-08-27 (third pass) — the supersession scan, run

**Iwaniec 1978 is not superseded for x² + 1.** Landau's fourth problem is open;
P₂ remains the record. Two nearby results matter, and one search summary had to
be discarded:

- ⚠️ **A search summary asserted that Green–Sawhney (2024) proved "infinitely
  many primes of the form n²+1 with n ≡ 4 (mod 6)".** That is false, and would
  have been a solution to Landau's fourth problem. It garbled the actual
  theorem, which quantifies over the *parameter* n in p² + nq². Recorded here
  because the claim is superficially plausible and will resurface in searches.
- **Green & Sawhney**, *Primes of the form p² + nq²*,
  [arXiv:2410.04189](https://arxiv.org/abs/2410.04189) (2024). For n ≡ 0 or 4
  (mod 6): infinitely many primes p² + nq² with **p and q both prime**, with an
  asymptotic; n = 4 settles Friedlander–Iwaniec's "Gaussian primes conjecture".
  Method: Type I/II sums over **Q(√−n)** — for n = 4, Q(i) — with the Type II
  input from Gowers-norm technology (quantitative concatenation theorems of
  Kuca and Kuca–Kravitz–Leng; the quasipolynomial inverse theorem of Leng, Sah
  and Sawhney). **Unread. Highest-value item in the repo** — see the note on the
  plan's exclusion below.
- **On Gaussian primes in sparse sets**,
  [arXiv:2302.11331](https://arxiv.org/abs/2302.11331). Infinitely many primes
  a² + b² with b ∈ B, for B of size X^{1/2−δ}. This is the same shape as our
  problem with B = {1} — i.e. the maximally sparse case, far outside its range —
  but it is the nearest frame in the literature. Unread.

### The plan's Green–Tao exclusion needs re-arguing

Plan §Cross-cutting says: *"**Don't** pursue Green–Tao / nilsequence methods;
single-variable polynomials are outside their scope."* Green–Sawhney obtain a
Type II estimate over Q(i) using exactly that toolkit. Their sequence is
two-variable with α = 1 and both variables prime, so the exclusion is still
defensible on its stated grounds — but it was written before this result and
should be re-argued explicitly rather than left standing. **Do not treat the
exclusion as settled.**

### Still not done

- Reading the three unread arXiv items above, Green–Sawhney first.
- The scan was three searches, not a database sweep. It is enough to say
  nothing obvious supersedes Iwaniec 1978; it is not a literature review.
- Candidates spotted in passing and not read:
  - [arXiv:2112.03617](https://arxiv.org/abs/2112.03617) — *X²+(Y²+1)² and
    X²+(Y³+Z³) also capture their primes*. Note the inner **y²+1**. Most
    directly relevant of the three; α is still 3/4, so it is not the same
    problem, but its handling of a one-variable inner polynomial may transfer.
  - [arXiv:2111.04136](https://arxiv.org/abs/2111.04136) — *Prime values of
    f(a,b²) and f(a,p²), f quadratic*.
  - [arXiv:2407.14368](https://arxiv.org/abs/2407.14368) — *On the theory of
    prime producing sieves*. The likeliest place for a restated or relaxed
    version of (R1).
