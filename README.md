# One Law, Two Exact Nulls: what coherence measures, and what it cannot certify

**A synthesis of two independently-run hardware programmes.** It contains no
new measurements. Its contribution is the identification that its two companion
programmes measured the *same function*, and the demonstration that their two
internal nulls — taken together — settle what that function certifies. Neither
companion can make the claim alone.

The companions:

- **[twisted-spin-ptm](https://github.com/IllI/twisted-spin-ptm)** — the
  Pauli-transfer-matrix structure of one-axis-twisting boundary channels.
  Coherence measured against **coupling angle**.
  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21878783.svg)](https://doi.org/10.5281/zenodo.21878783)
- **[relational-time-ibm-quantum](https://github.com/IllI/relational-time-ibm-quantum)**
  — whether relational time leaves a quantum signature distinguishable from its
  classical mimic; eleven pre-registered runs, 72 jobs. Coherence measured
  against **time**.
  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21878786.svg)](https://doi.org/10.5281/zenodo.21878786)

Every load-bearing claim below is checkable in under a second:

```bash
python theory/verify_companion_result.py
```

---

## 1. One law

`cos(θ/2)` is the overlap between two qubit states separated by Bloch angle
`θ`. Both programmes measure coherence surviving as a **product of those
overlaps — one factor for every party that has acquired distinguishing
information.**

| | measured quantity | form | what the exponent counts |
|---|---|---|---|
| **twisted-spin-ptm** | `T_xx = cos(χt/2)^(N−2)` | overlap^(N−2) | the `N−2` bulk spins, each learning partial *which-state* information about the boundary pair |
| **relational-time** | `ρ_C[t,t'] = cos((t−t')·π/d)` | overlap¹ | *which-time* distinguishability between two clock records |
| **relational-time** (IBM-1) | witness `∝ cos(μ/2)^p` | overlap^p | environment modes coupled to the clock at strength `μ` |

The identification is **exact, not analogical**. At `d = 8` adjacent clock
records overlap at `0.923880`; `cos(π/4 / 2) = 0.923880`. The clock-record
overlap *is* the half-angle state overlap, and the OAT boundary element is that
same overlap raised to the number of informed spins.

> **Entanglement decay and temporal distinguishability are the same
> bookkeeping.** Information leaving a subsystem is simultaneously entanglement
> lost and moments becoming distinguishable. One programme measures it against
> coupling angle; the other against time.

## 2. Two exact nulls

Each programme has an exact structural zero. Each was **predicted from theory,
pre-registered, and confirmed on hardware** — these are the internal controls
that validated each apparatus, the results each line trusted most.

```
twisted-spin-ptm, χt = π      relational-time, d = 2
T_xx        = 0.000000        witness TVD  = 0.000000
ρ₂          = I/4 exactly     state        = Bell pair
concurrence = 0.000000        entanglement = 1.0000 ebits
→ SEPARABLE                   → MAXIMALLY ENTANGLED
```

**The same observable reads exactly zero on a separable state and on a
maximally entangled one.**

This is not an argument that the coherence observable is entanglement-blind. It
is a *measurement* of it, at both extremes of the entanglement spectrum, using
each programme's most trusted result. No single reading of this quantity —
however precise, however replicated, however well it fits theory — carries
information about whether the underlying state is entangled.

**Neither repository can demonstrate this alone.** One null shows the observable
vanishing on a separable state; the other shows it vanishing on a maximally
entangled one. The demonstration requires both, which is the reason this
repository exists.

## 3. The convergent resolution

Both programmes then hit the same wall from opposite directions, and neither
anticipated the other's version:

| | how it appeared | how it was resolved |
|---|---|---|
| **twisted-spin-ptm** | entanglement is not identifiable from PTM anisotropy alone | `V_Q` over Haar-random measurement settings |
| **relational-time** | no single local product-basis distribution certifies clock–system entanglement *(proved, then verified adversarially)* | multi-setting fidelity witness exceeding the exact separable bound `λ_max = ½` |

The relational-time programme reached its version the hard way. It built two
adversarial states against its own results — a zero-entanglement product state
scoring **4.2× higher** on the coherence witness than the real history state,
and a separable state scoring **1.7× higher** on the joint witness built to
repair it — before a two-line theorem generalized the failure.

**The combined statement:**

> The survival of entanglement and the distinguishability of moments are the
> same quantity, measured in different variables: a product of state overlaps,
> one factor per informed party. That quantity is measurable to high precision,
> scales as predicted, and has exact structural nulls in both programmes — and
> it certifies nothing. Certification of quantum structure requires agreement
> across incompatible measurements, a conclusion two independent programmes
> reached from opposite directions.

What follows is a **certification threshold**, and it is higher than the
observables usually offered as evidence for relational time can reach.
Conditional evolution is reproduced by a classical clock control. Local clock
coherence is beaten by a state with zero entanglement. Single-basis joint
correlation is beaten by a separable state. What survives is a multi-setting
witness — and, in the relational-time programme's final run, a single 3-qubit
preparation certified **entangled, stationary as a quantum ray, and internally
evolving simultaneously**.

## 4. Why the applied version does not work

This line began with two engineering questions about moving information off a
spacecraft. Both now have derived answers, and both are negative — which is
what makes them useful.

**Can entangled states carry compressed observations for downlink?**
Bounded, hard. Holevo limits `n` transmitted qubits to `n` classical bits
without pre-shared entanglement; superdense coding reaches `2n` with it. No
regime releases terabytes. Compression must be earned in the **classical layer,
before encoding** — which is exactly where the semantic-transport experiments
hit their codec ceiling, approached from the opposite direction. The quantum
layer's contribution is **transport of relational structure**, not information
density.

**Does relativistic time dilation buy processing headroom?**
No — it is a trade. Earth-frame storage lengthens by `γ` while local operations
per Earth-second fall by the same `γ`, leaving operations-per-coherence-time
unchanged. A dilated node computes *less*, not more. At achievable velocities
`γ − 1 ≈ 10⁻¹⁰` (ISS: `3.3 × 10⁻¹⁰`), so the effect is programmable in a
circuit and absent in practice.

Where those questions came from, and the experiments that asked them:
[`docs/PROGRAM_HISTORY.md`](docs/PROGRAM_HISTORY.md).

## 5. The open frontier

The law was established with **spins** as the informed parties
(twisted-spin-ptm), and with **clock registers and environment modes**
(relational-time). The natural next question is whether it holds when the
informed parties are **field modes**.

Status: **open, and barely started.** The Dicke model is the legitimate route —
genuine light–matter coupling, reducing to OAT in the adiabatic limit
(`χ_eff = g²/ω_m`) — and it was characterized once during the TPU campaign,
returning `K_eff = 1, γ_dom ≈ 0` at `N ∈ {2,4,6}`, cleanly separated from OAT
by damping alone. **That is a fingerprint, not a cosine-law test.** Nothing
measured so far tracks how coherence decays against field occupation.

Three further directions are specified but unexecuted in
[`docs/FUTURE_WORK.md`](docs/FUTURE_WORK.md).

## 6. What this does not claim

- **No new measurements.** A synthesis of two completed programmes plus
  derivations. The original contributions are the exact identification, the
  matched-null demonstration, and the applied bounds.
- **Nothing about quantum electrodynamics.** No gauge field, photon, or vacuum
  appears in either programme: OAT is a spin model and the Page–Wootters clock
  is engineered qubits. See §5 for the honest route toward field states.
- **Nothing about time in nature.** Neither companion claims time is emergent,
  tests the Wheeler–DeWitt constraint, or realizes a physical Page–Wootters
  universe. Both states are prepared by externally timed gates, and both
  clock/system splits are imposed rather than derived.
- **Not peer-reviewed.** These are archived research records.

## Repository layout

```
theory/     the companion result, executable end to end
            (verify_companion_result.py) -- numpy only, no QPU
docs/       PROGRAM_HISTORY.md   where the questions came from
            FUTURE_WORK.md       specified but unexecuted directions
```

## Acknowledgments

Research supported with Cloud TPUs from Google's TPU Research Cloud (TRC). The
TRC allocation supported the simulation and hypothesis-development phase of the
companion programmes; their hardware experiments used separate IBM Quantum Open
Plan access.
