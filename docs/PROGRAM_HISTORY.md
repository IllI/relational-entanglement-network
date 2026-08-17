# Where this program came from

This repository opens with four structural results and no hardware runs. That
is not a cold start — each result is the mature form of a question asked at the
beginning of a longer line of work, and the line is what makes them meaningful.

The TPU Research Cloud proposal was about **time emission and quantum
information theory**. Both halves matter: one produced the relational-time
hardware program, the other produced this repository.

---

## The practical application: semantic transport

**`PROGRAM_AQ_YINYANG`, 2026-06-03.**

If quantum information theory is going to be useful rather than decorative, a
fair test is whether **semantic content survives transport through a folded
state**. The concrete target: encode a symbolic image into a folded state
space, transport it, decode it — with two animation frames compacted into a
single state as the ambition. The motivating application was a spacecraft
condensing a large observational volume into entangled photons for downlink.

The experiment was built to isolate where such a scheme would break, and it
found the answer in four runs:

| run | question | answer |
|---|---|---|
| **1** | is the codec good enough? | No — sparse retention capped the oracle at 17.0 dB before transport began |
| **2** | is *capacity* the limit? | **No.** All-coefficient retention gives `oracle = 80.0 dB` — essentially lossless — while transport delivers 21.4 dB |
| **3** | is it the decoder? | No — a pixel-space ridge decoder moved 21.42 → 21.42 dB |
| **4** | does the channel work at all? | Yes — raw patch transport reaches 30.0 dB one-frame, 25.0 dB for an ordered two-frame roster |

**The finding that carried forward is the shape of the failure, not the
failure.** Semantic identity was recovered *perfectly* — motif, source and
target recovery all `1.0000`, coefficient-field cosines 0.98–0.99, frequency
support exact. Yet the reconstructed image was visibly degraded.

In other words: **a strong single observable was near-perfect while the
quantity that actually mattered was not certified.** High cosine similarity is
forgiving when dominant energy is aligned; pixel reconstruction requires the
local field to be right in value, sign, phase and arrangement.

That is the same structure the quantum program met two months later, and it is
why that program was built the way it was. IBM-2 prepared a zero-entanglement
product state that scored *higher* on the clock-coherence witness than the
history state did; IBM-3 did the same to the replacement witness. The lesson is
identical — **a single observable can look excellent and certify nothing** —
and the response in both cases was the same: stop trusting one number, and
demand agreement across incompatible measurements.

The contemporaneous verdict is worth keeping as written, because it set the
standard the later work inherited:

> This should not be described as completed image teleportation. The more
> accurate framing is: the experiment demonstrates semanticized image-state
> transport with strong coefficient recovery, and identifies coefficient
> unfolding/pixel reconstruction as the current bottleneck.

Two precisions, so the record is unambiguous: this was **transport through a
state-space model in simulation**, not physical teleportation with entangled
photons; and it is a **partial success with a named bottleneck**, not a null.

---

## The theory line: stationary relative time evolution

The other half of the proposal — time emission — became the question of whether
relational time leaves a signature distinguishable from its classical mimic.
That line ran through a synthetic Page–Wootters ladder on TPU (establishing
that recovery requires entropy-bearing, irreversible histories, and that finite
clock records are provably non-orthogonal, making relational time a *path-level*
observable) and then onto quantum hardware.

Eleven pre-registered runs, 72 jobs, are documented in
[relational-time-ibm-quantum](https://github.com/IllI/relational-time-ibm-quantum).
Its central result is a single 3-qubit preparation certified **entangled,
stationary as a quantum ray, and internally evolving simultaneously** — the
Page–Wootters mechanism's defining conjunction, measured on one state.

The instrument used throughout was **D-LinOSS**, a damped linear oscillatory
state-space model whose complex-diagonal recurrence matches the physics at the
level of the measured phase evolution. On clean quantum dynamics it is
surgical: for the OAT Lindblad witness it returned `γ_dom = 4Γ` exactly, to four
decimal places, across all 50 records spanning `N ∈ {2…64}`. Its limits —
established with pre-registered controls rather than found in review — are what
set the hardware program's independent variable, functional form, and
certification standard.

---

## What the four structural results answer

Both founding questions now have derived answers rather than open ones:

**Can entangled states carry compressed information off a platform?**
Bounded, and the bound is hard. Holevo limits `n` transmitted qubits to `n`
classical bits without pre-shared entanglement; superdense coding reaches `2n`
with it. Compression has to be earned in the classical layer *before* encoding
— which is precisely where the yin/yang codec ceiling appeared, approached from
the opposite direction. The quantum layer's contribution is **transport of
relational structure**, not information density.

**Does relativistic time dilation buy processing headroom?**
No — it is a trade. Earth-frame storage lengthens by γ while local operations
per Earth-second fall by the same γ, leaving operations-per-coherence-time
unchanged. And at achievable velocities `γ − 1 ≈ 10⁻¹⁰`, so the effect is
programmable in a circuit and absent in practice.

The remaining two results — that rate loop closure is automatic rather than
contingent, and that a clock serves as a reference frame only when
`gcd(rate, d) = 1` — follow the rule this line acquired the expensive way:

> **Derive whether a quantity is contingent before designing a run to measure
> it.**

---

## Primary sources

Held in the working repository, cited by date so the chronology is checkable:

- `PROGRAM_AQ_YINYANG_FINDINGS_2026-06-03.md` — semantic transport, the
  80 dB / 21.4 dB gap
- `TPU_EXPERIMENT_PLAN.md` — 2026-05-11, D-LinOSS calibration across four
  physical systems
- `AQ_PAGE_WOOTTERS_DLINOSS_0_RESULTS_2026-06-15.md` — the relational-clock
  ladder and the promoted A10 mechanism
- `mismo_tiempo_results/` — the early T4 and TPU run sets that motivated the
  grant application
