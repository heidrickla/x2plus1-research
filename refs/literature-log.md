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
| 2026-08-27 | C | `Friedlander Iwaniec asymptotic sieve for primes hypotheses`; `X^2+Y^4 captures its primes arXiv` | Both 1998 Annals papers located as arXiv preprints and read directly. See below. | not checked |

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

### Still not done

- **The supersession check has not been run.** Nothing above confirms that
  Iwaniec 1978 or FI 1998 remains the state of the art; only that the 1998
  hypotheses are as quoted. Run the scan properly before treating
  [Note C](../notes/note-C-requirements.md)'s conclusion as current.
- Candidates spotted in passing and not read: *"On the theory of prime
  producing sieves"* ([arXiv:2407.14368](https://arxiv.org/abs/2407.14368)),
  and *"The polynomials X²+(Y²+1)² and X²+(Y³+Z³)² also capture their primes"*
  ([arXiv:2112.03617](https://arxiv.org/abs/2112.03617)). The second is
  directly relevant: it handles sequences built from **one-variable** inner
  polynomials and may bear on the density threshold.
