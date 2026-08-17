# Where this program came from

This repository opens with four structural results and no hardware runs, which
makes it look like a cold theory drop. It is not. Each of those results is the
mature answer to a concrete engineering question asked at the start of a
two-year line of work, and the answers are mostly **no**. This document is the
account of how the questions were asked, what was built to answer them, and
what failed along the way.

It is written from the primary artifacts — run specs, findings documents, and
verdict files produced at the time — not reconstructed from memory.

---

## 1. The founding questions (`mismo_tiempo`, pre-grant, T4 class hardware)

The line began with two practical questions about moving information off a
spacecraft:

1. **Could entangled states encode compressed information** — so a satellite
   could condense a large observational volume into entangled photons and send
   that to Earth?
2. **Could relativistic time dilation buy processing headroom** — if the
   platform is far enough out and fast enough, does it get "extra" local time
   to compute in?

A third, adjacent question motivated the tooling: could **tensor networks plus
a state-space model order vast telescope data**, using JWST spectra as the
test case?

These ran on modest hardware (`ahora_mismo_t4_*`, `tiempu_tpu*` result sets)
and were the basis for the TPU Research Cloud application, which was framed
around **time emission**.

---

## 2. The yin/yang divergence — semantic transport of an image

**`PROGRAM_AQ_YINYANG`, 2026-06-03.** This is question 1 in its original,
testable form: encode a symbolic image into a folded semantic state space,
transport it, and decode it. The ambition was two frames of an animation
compacted into a single transported state.

The target was a 16×16 grayscale tai-chi-tu, tiled into sixteen 4×4 patches,
each encoded as a complex FFT coefficient field. Four runs, each of which
narrowed the failure:

| run | what it changed | result |
|---|---|---|
| **YINYANG-1** | sparse codec, 10 of 16 coefficients | `oracle_psnr = 17.0 dB` — **the codec was the ceiling**, not the transport. Too much edge information discarded before transport began |
| **YINYANG-2** | all 16 coefficients retained | `oracle_psnr = 80.0 dB`, `ifft_psnr = 21.4 dB` — **decisive**: the image is representable losslessly, so capacity is exonerated and *recovery* is the bottleneck |
| **YINYANG-3** | added a direct pixel-space ridge decoder | `21.42 dB` vs `21.42 dB` — **no change**. Rules out "decode in pixel space instead" as the fix |
| **YINYANG-4** | bypassed the codec, raw pixel patches | `30.0 dB` one frame, `25.0 dB` for the ordered two-frame roster — the channel carries raw state well, but this sidesteps the hard problem |

The semantic layer was never the difficulty: motif, source and target recovery
were `1.0000` throughout, and coefficient-field cosines sat at 0.98–0.99. The
problem was that **high cosine similarity does not imply pixel fidelity** —
small structured errors in coefficient amplitude, quadrature orientation and
patch-boundary consistency unfold into visible distortion through the inverse
FFT. `dc_mae = 0.347` was the tell.

A preview-assembly bug also made early reconstructions look scrambled: the
recovery sampler permutes patch states, and the preview writer rendered
permuted order as raster order. The metrics had always been comparing correctly
paired states; only the visualization was wrong. It was found and fixed, and
the corrected previews are in the record.

**The contemporaneous verdict, quoted rather than paraphrased:**

> This should not be described as completed image teleportation.
> The more accurate framing is: the experiment demonstrates semanticized
> image-state transport with strong coefficient recovery, and identifies
> coefficient unfolding/pixel reconstruction as the current bottleneck.

Two things to be precise about, because they matter for what this program
concludes. This was **simulated transport through a state-space model, not
physical quantum teleportation** — no entangled photons were involved. And the
result is a **partial success with a named bottleneck**, not a null.

---

## 3. The TPU campaign (TRC grant, 2026-04-21 → 2026-06-21)

### D-LinOSS as a quantum-dynamical instrument

**`TPU_EXPERIMENT_PLAN`, 2026-05-11**, `chronos-eve` v6e-8. Before any of the
relational-time work, D-LinOSS was calibrated as a fingerprinting tool across
four physical systems, with a pre-registered prediction for each.

The strongest result in the entire corpus is here: for the OAT Lindblad
witness, D-LinOSS returned `K_eff = 1` and `γ_dom = 4Γ` **exactly, to four
decimal places, for all 50 records** spanning `N ∈ {2…64}` and
`Γ ∈ {0.001…0.10}`. On clean, well-conditioned quantum dynamics the model is
surgical.

The same run falsified its own central hypothesis. **H4 predicted the Dicke
model would land between OAT and SYK on a one-dimensional "complexity axis."
It did not** — Dicke clustered with OAT at `K_eff = 1`. The document's own
assessment, written at the time:

> The falsification of H4 is the most scientifically mature outcome. A
> prediction was made, signatures were defined, a held-out system was tested,
> the prediction failed, and the embedding geometry was updated.

It also flagged, unprompted, that `K_eff = 6` saturated for *every* complex
system tested and was therefore **indistinguishable from a truncation
artifact** — with a four-item analysis required before any publication claim.
That is the same failure mode as the later random-telegraph-noise false
positive: the model reads spectral morphology, not quantum structure.

### The Page–Wootters ladder, and the ridge baseline

**June 2026**, roughly twenty runs. The relational-clock work established that
recovery is possible only from entropy-bearing, irreversible histories (arm
`A10`), and that finite-clock records are provably non-orthogonal — making
relational time a *path-level* rather than pointwise observable.

It also established something that must be stated plainly, because a
downstream summary of this work once got it wrong and had to be corrected:

> **D-LinOSS never beat its ridge baseline. Not once, in any configuration,
> at any noise level.**

Every recorded `D-LinOSS − ridge` value is negative: `−0.0055`, `−0.0178`,
`−0.0063`, `−0.0241`, `−0.1566`, `≈−0.40`, `−0.074`, `−0.082`. The gate it
passed was a **competitiveness tolerance** (`≥ −0.05`), not a superiority test.
The event-damped variant's contribution was to narrow the deficit from ≈−0.40
to ≈−0.07 — a real and diagnostic improvement, and still a deficit.

### The late astrophysics deviation

**`TRC_ASTROPHYSICS_MODELING_PROGRAM_CLOSEOUT`, 2026-06-21.** In the final
stretch of the grant, the stack was pointed at real astronomy — TRAPPIST-1e
stellar contamination, DREAMS reproduction, GLIMPSE-17775 — to demonstrate
D-LinOSS plus tensor networks in a practical physics domain.

It did not promote. The verdict was `FAILS_REALDATA_POSITIVE_CONTROL`, and
"D-LinOSS superiority over the promoted linear SSM detector stack" is listed
explicitly under *claims not supported*. On the WASP-39b positive control
D-LinOSS reached 0.9828 while a plain linear SSM reached 0.9997 and even a
smooth-residual baseline reached 0.9887; damping ablation was negligible.

The closeout diagnosed four concrete implementation defects (wavelength bins
treated as independent scalar streams, soft spectral windows standing in for
hard temporal pole constraints, full-spectrum reconstruction rewarding the
static baseline, and hidden state overwritten rather than accumulated), and it
recorded a genuine pipeline error: the first experiments ran at the wrong
reduction stage, on detector-level integration flux rather than extracted
transmission spectra. **The failed injections are therefore not limits on
DREAMS sensitivity** — they are negative results for a different objective.

Its own summary is the right one: *this is a model-selection result, not
evidence that state-space modeling is scientifically inappropriate.*

---

## 4. The quantum bridge (IBM, August 2026)

The TPU work had established what could not be settled classically. The
question moved to quantum hardware: **eleven pre-registered runs, 72 jobs**,
documented in
[relational-time-ibm-quantum](https://github.com/IllI/relational-time-ibm-quantum).

The short version is that the naive signature of relational time fell to a
classical mimic; two replacement witnesses fell to adversarial states the
program built against its own results; and only a multi-setting fidelity
witness survived, after which a single 3-qubit preparation was certified
entangled, ray-stationary and internally evolving simultaneously. Two runs are
reported as failures, and a later derivation showed they had been chasing a
quantity fixed by construction.

---

## 5. How the founding questions were finally answered

This repository's four structural results, derived at zero compute cost, are
where the two founding questions land:

| founding question (`mismo_tiempo`) | answer, and where it comes from |
|---|---|
| **Compress large data into entangled photons for downlink?** | **No, not beyond a hard bound.** Holevo limits `n` transmitted qubits to `n` classical bits without pre-shared entanglement; superdense coding reaches `2n` with it. No regime releases terabytes. Any compression must be earned classically, before encoding — which is exactly where the yin/yang codec ceiling appeared, from the other direction. |
| **Buy processing headroom from time dilation?** | **No — it is a trade, not an accelerator.** Earth-frame storage lengthens by γ while local operations per Earth-second fall by the same γ, leaving operations-per-coherence-time unchanged. A dilated node computes *less*, not more. And at achievable velocities `γ − 1 ≈ 10⁻¹⁰`, so the effect is ~10⁻⁸ percent — programmable in a circuit, absent in practice. |

Both answers are negative, and both were reached by derivation rather than by
another expensive run. That is the discipline the program spent two years
acquiring, and the reason this repository leads with what it already knows it
cannot do.

The remaining two structural results — that rate loop closure is automatic
rather than contingent, and that a clock is a usable reference frame only when
`gcd(rate, d) = 1` — exist for the same reason. The predecessor program spent
two hardware runs measuring a quantity that its own construction had fixed at
`+1`. The rule that came out of it governs everything here:

> **Derive whether a quantity is contingent before designing a run to measure
> it.**

---

## 6. What actually transfers

Across `mismo_tiempo`, the TPU campaign, the astrophysics deviation and eleven
QPU runs, the durable findings are methodological:

- **D-LinOSS is a precise instrument on clean simulated quantum dynamics
  (`γ_dom = 4Γ` exactly, 50/50 records) and loses to linear baselines on every
  noisy real-data task tested.** Both halves of that sentence are load-bearing,
  and the boundary between them was mapped with pre-registered controls rather
  than discovered in review.
- **Its failures were structured enough to be informative.** The entropy
  requirement, the record-overlap functional form, and the
  measurement-diversity certification standard each came from a specific
  D-LinOSS negative, and each became a design parameter of the hardware program
  that followed.
- **A model that reads spectral morphology will confidently mislabel classical
  noise as quantum structure.** Identified twice — the `K_eff` saturation in
  May, the random-telegraph false positive later — and it is why the quantum
  program insists on measurement diversity rather than a single observable.
- **Large accelerators are the right place to fail, and quantum hardware is the
  right place to arbitrate.** The QPU work cost 72 jobs of seconds each on a
  free tier. The expensive month-scale work that made those runs worth
  submitting was classical.

---

## Primary sources

Held in the working repository rather than here, and cited by date so the
chronology can be checked:

- `TPU_EXPERIMENT_PLAN.md` — 2026-05-11, D-LinOSS quantum fingerprinting, H4
  falsification, `K_eff` saturation caveat
- `PROGRAM_AQ_YINYANG_FINDINGS_2026-06-03.md` — semantic image transport, the
  80 dB / 21.4 dB gap
- `AQ_PAGE_WOOTTERS_DLINOSS_0_RESULTS_2026-06-15.md` — the relational-clock
  ladder, ridge comparisons, A10 event-damped confirmation
- `TRC_ASTROPHYSICS_MODELING_PROGRAM_CLOSEOUT_2026-06-21.md` — grant-cycle
  closeout and D-LinOSS model-selection result
- `mismo_tiempo_results/` — the pre-grant T4 and early TPU run sets
