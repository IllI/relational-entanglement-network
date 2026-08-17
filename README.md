# One Law, and a Witness That Runs Backwards

**A synthesis of two independently-run hardware programmes, with one dedicated
run of its own.** Its contribution is that the two programmes measured the same
law, and that reading that law on a *marginal* — as the relational-time
literature does — produces an observable which is not merely uninformative
about entanglement but **suppressed by it**.

That claim was derived here first, then tested: a purpose-built sweep on
`ibm_marrakesh` measured the witness and CHSH on the same states from a product
state to a Bell pair and found them anti-correlated at **`r = −0.9573`**, with
the witness peaking exactly where the Bell violation vanishes (§2).

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

Every load-bearing claim below is reproducible in under a second:

```bash
python theory/verify_companion_result.py
```

---

## 1. One law, two variables

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

> Entanglement decay and temporal distinguishability are the same bookkeeping.
> Information leaving a subsystem is simultaneously entanglement lost and
> moments becoming distinguishable. One programme measures it against coupling
> angle; the other against time.

## 2. Read on a marginal, the law runs backwards

The relational-time programme's headline observable reads the **clock
marginal** — trace out the system, read the clock in its Fourier basis, measure
the deviation from uniform. One line of standard theory then decides its fate:

> For a bipartite **pure** state, the marginal entropy *is* the entanglement
> entropy.

Entanglement with the system is exactly what mixes the clock marginal, and a
mixed marginal is exactly what flattens the distribution the witness reads.
**Marginal coherence and entanglement across the cut are in direct tension, by
construction.** Evaluated exactly:

| `d` | state | clock-marginal witness | entanglement |
|---|---|---|---|
| 2 | history | **0.000000** | **1.0000 ebits** |
| 2 | product | **0.500000** | 0.0000 ebits |
| 4 | history | 0.176777 | **1.0000 ebits** |
| 4 | product | **0.750000** | 0.0000 ebits |
| 8 | history | 0.496689 | **1.0000 ebits** |
| 8 | product | **0.875000** | 0.0000 ebits |

The witness is *highest* exactly where entanglement is *zero*.

**This predicts a hardware number, retrodictively.** The relational-time
programme's IBM-2 run prepared a zero-entanglement product state as an
adversarial control and measured it scoring **4.2× higher** than the real
history state at `d = 4`. The exact ratio above is `0.750 / 0.176777 = 4.24`.
The adversary did not exploit a loophole — it saturated a quantity that
entanglement necessarily suppresses.

### Measured directly (IBM-11, 2026-08-17)

Retrodiction is weaker than a test, so the sweep was run. One parameter, from a
product state to a Bell pair, measuring the marginal witness **and** CHSH on
each state — 53 circuits, two qubits, `ibm_marrakesh`, 9/9 pre-registered gates
([full results](https://github.com/IllI/relational-time-ibm-quantum/blob/main/docs/AQ_PAGE_WOOTTERS_IBM_11_RESULTS_2026-08-17.md)).

| λ | witness (exact) | CHSH (exact) |
|---|---|---|
| 0.00 | **0.4830** (0.5000) | **1.8605** (2.0000) |
| 0.25 | 0.4480 (0.4619) | 1.9995 (2.1414) |
| 0.50 | 0.3325 (0.3536) | 2.3085 (2.4495) |
| 0.75 | 0.1923 (0.1913) | 2.5500 (2.7229) |
| 1.00 | **0.0100** (0.0000) | **2.6565** (2.8284) |

**Witness–CHSH correlation `r = −0.9573`.**

Two things make this a test rather than a demonstration. **The state that
maximises the witness produced no Bell violation at all** — CHSH `1.8605`,
below the classical bound, at the same λ where the witness peaks. That was the
gate written to falsify the framing, and it held.

And **the anti-correlation was not guaranteed to survive.** For ideal *pure*
states it is forced, because marginal entropy is entanglement entropy — but
hardware states are mixed, where that identity fails and decoherence attacks
marginal coherence and nonlocal correlation through different channels at
different rates. Whether the relationship survived was genuinely open.

The exact trade-off held too, as *structure* rather than value:

```
S² + 16W² :  7.1941  7.2093  7.0981  7.0939  7.0586
             mean 7.1308 (ideal 8.0, attenuation 0.891)
             spread 0.1507 against a ±1.1390 band
```

Decoherence lowers the level; it does not bend the curve. The spread is an
order of magnitude inside tolerance, and *flatter* than the noisy simulator
predicted (0.4994 at attenuation 0.821) — the run beat its own noise model.

## 3. Two exact nulls

Each programme has an exact structural zero, each predicted from theory,
pre-registered, and confirmed on hardware — the internal controls that
validated each apparatus.

```
twisted-spin-ptm, χt = π      relational-time, d = 2
T_xx        = 0.000000        witness TVD  = 0.000000
ρ₂          = I/4 exactly     state        = Bell pair
concurrence = 0.000000        entanglement = 1.0000 ebits
→ SEPARABLE                   → MAXIMALLY ENTANGLED
```

Both share the property driving §2: **maximally mixed marginals.** A maximally
entangled pure state has them; so does a globally maximally mixed state.
Evaluating both observables on both states separates what each can see:

| state | `T_xx` (joint correlator) | clock-marginal witness |
|---|---|---|
| `I/4` — separable | `0.000000` | `0.000000` |
| Bell — maximally entangled | **`+1.000000`** | `0.000000` |

The two observables are **not the same functional**: `T_xx` is a joint
correlator and does separate these states; the marginal witness cannot. What
the programmes share is the *law* and an exact null — and twisted-spin-ptm's
null supplies the separable state that makes the marginal blindness concrete
rather than a single-programme curiosity.

Two cautions. `T_xx` separating these particular states does **not** make it an
entanglement witness — twisted-spin-ptm's own finding is that entanglement is
not identifiable from PTM anisotropy alone. And §2's anti-correlation is stated
for the pure-state family actually tested, not as a claim about every coherence
measure everywhere.

## 4. Independent convergence

Svozil, *Certified Private Relational Time from Entanglement*
([arXiv:2512.09100](https://arxiv.org/abs/2512.09100)), builds a relational
clock from a singlet shared between two separated observers and reaches the
same wall from a fourth direction: **the individual marginal tick rates remain
`1/2` and carry nothing.** Temporal structure exists only in the *joint
coincidence record*, `R(θ) = ½sin²(θ/2)`, which he certifies
device-independently through a CHSH violation.

Same mechanism as §2, arrived at independently — and a concrete protocol for
the device-dependence limitation the relational-time programme records but does
not close.

**And the excess is separably reproducible — measured.** IBM-11 added an arm
for it. Our `|Φ⁺⟩` anti-coincidence reproduces `R(θ)` exactly (six decimals,
verified pre-submission), and at the peak-excess angle:

```
θ = 140.5°     Bell  +0.0650      product  +0.0590      |gap| 0.0060
                                              (3σ empirical = 0.0414)
CHSH           Bell   2.6565      product    1.8605      gap   0.7960
```

**A zero-entanglement product state reproduces the synchronisation excess to
within 0.006, while CHSH separates the same two states by 0.80.** `R(θ)` is a
single-setting joint rate, so the theorem in §5 applies to it directly: such a
distribution is separably reproducible and cannot certify nonclassicality.

This is the **third independent instance** of that theorem — after the
clock-coherence witness and single-basis joint correlation — and the first
demonstrated against an observable from outside the programme. It is not a
criticism of the certification in that paper, which rests on CHSH and agrees
with everything here; it bounds what the excess *alone* supports.

The construction also supplied two exact internal nulls for free: the quantum
and benchmark curves cross identically at `θ = 90°` and `θ = 180°`, so any
measured excess there is instrumental. Their scatter calibrated the error bar —
and caught a real mistake, since gating on shot noise alone failed by 0.0003. A
*rate* measured under readout error carries a bias that `√(p(1−p)/N)` cannot
see.

## 5. The certification threshold

Both programmes hit the wall independently and resolved it the same way:

| | how it appeared | how it was resolved |
|---|---|---|
| **twisted-spin-ptm** | entanglement is not identifiable from PTM anisotropy alone | `V_Q` over Haar-random measurement settings |
| **relational-time** | no single local product-basis distribution certifies clock–system entanglement *(proved, then verified adversarially)* | multi-setting fidelity witness exceeding the exact separable bound `λ_max = ½` |

The relational-time programme got there the hard way, building two adversarial
states against its own results — the product state of §2 scoring 4.2× higher,
and a separable state scoring 1.7× higher on the joint witness built to repair
it — before a two-line theorem generalized the failure.

**The combined statement:**

> The survival of entanglement and the distinguishability of moments are the
> same quantity, measured in different variables: a product of state overlaps,
> one factor per informed party. Read on a marginal, that quantity does not
> merely fail to certify entanglement — it is suppressed by it, so the
> best-scoring states are the least entangled ones. Certification requires
> agreement across incompatible measurements, a conclusion reached
> independently by two hardware programmes here and by a third line elsewhere.

What follows is a **certification threshold** higher than the observables
usually offered as evidence for relational time can reach. Conditional
evolution is reproduced by a classical clock control. Local clock coherence is
*maximized* by a state with zero entanglement — measured, at CHSH 1.86, below
the classical bound. Single-basis joint correlation
is beaten by a separable state. What survives is a multi-setting witness — and,
in the relational-time programme's final run, a single 3-qubit preparation
certified **entangled, stationary as a quantum ray, and internally evolving
simultaneously**.

## 6. Why the applied version does not work

This line began with two engineering questions about moving information off a
spacecraft. Both now have derived answers, and both are negative — which is
what makes them useful.

**Can entangled states carry compressed observations for downlink?** Bounded,
hard. Holevo limits `n` transmitted qubits to `n` classical bits without
pre-shared entanglement; superdense coding reaches `2n` with it. No regime
releases terabytes. Compression must be earned in the **classical layer, before
encoding** — which is exactly where the semantic-transport experiments hit their
codec ceiling, approached from the opposite direction. The quantum layer's
contribution is **transport of relational structure**, not information density.

**Does relativistic time dilation buy processing headroom?** No — it is a
trade. Earth-frame storage lengthens by `γ` while local operations per
Earth-second fall by the same `γ`, leaving operations-per-coherence-time
unchanged. A dilated node computes *less*, not more. At achievable velocities
`γ − 1 ≈ 10⁻¹⁰` (ISS: `3.3 × 10⁻¹⁰`), so the effect is programmable in a
circuit and absent in practice.

Where those questions came from, and the experiments that asked them:
[`docs/PROGRAM_HISTORY.md`](docs/PROGRAM_HISTORY.md).

## 7. The open frontier

The law was established with **spins** as the informed parties
(twisted-spin-ptm), and with **clock registers and environment modes**
(relational-time). Whether it holds when the informed parties are **field
modes** is untested.

Status: **open, and barely started.** The Dicke model is the legitimate route —
genuine light–matter coupling, reducing to OAT in the adiabatic limit
(`χ_eff = g²/ω_m`) — and it was characterized once during the TPU campaign,
returning `K_eff = 1, γ_dom ≈ 0` at `N ∈ {2,4,6}`, cleanly separated from OAT
by damping alone. **That is a fingerprint, not a test of the law against field
occupation.**

**The priority next run** is not on that frontier — it is a direct hardware
test of §2. Sweep a single parameter from the product state to the Bell state
and measure *both* the marginal witness and CHSH on each state. Exactly, the
witness runs `0.5000 → 0.0000` while CHSH runs `2.0000 → 2.8284`: the state
that maximizes the coherence witness sits at the classical Bell boundary, and
the state saturating Tsirelson's bound has a witness of exactly zero. On ideal
pure states that relationship is forced; **on hardware it is contingent**,
because prepared states are mixed and decoherence attacks marginal coherence
and nonlocal correlation through different channels. Two qubits, ~25 circuits —
the cheapest decisive run this line has proposed, and it closes the loop back to
the CHRONOS telemetry nulls:
[`docs/NEXT_RUN_PROPOSAL.md`](docs/NEXT_RUN_PROPOSAL.md).

Three further directions are specified but unexecuted in
[`docs/FUTURE_WORK.md`](docs/FUTURE_WORK.md).

## 8. What this does not claim

- **One new measurement, not a new programme.** This is a synthesis of two
  completed programmes plus derivations, with a single dedicated run (IBM-11,
  53 circuits, two qubits) testing its central claim. That run is archived in
  the relational-time repository, whose numbering it continues. The original
  contributions here are the exact identification, the anti-correlation and its
  hardware test, and the applied bounds.
- **Nothing about quantum electrodynamics.** No gauge field, photon, or vacuum
  appears in either programme: OAT is a spin model and the Page–Wootters clock
  is engineered qubits. See §7 for the honest route toward field states.
- **Nothing about time in nature.** Neither companion claims time is emergent,
  tests the Wheeler–DeWitt constraint, or realizes a physical Page–Wootters
  universe. Both states are prepared by externally timed gates, and both
  clock/system splits are imposed rather than derived.
- **Not peer-reviewed.** These are archived research records.

## Repository layout

```
theory/     the companion result, executable end to end
            (verify_companion_result.py) -- numpy only, no QPU
docs/       COMPANION_RESULT.md  the full statement
            PROGRAM_HISTORY.md   where the questions came from
            FUTURE_WORK.md       specified but unexecuted directions
```

## Acknowledgments

Research supported with Cloud TPUs from Google's TPU Research Cloud (TRC). The
TRC allocation supported the simulation and hypothesis-development phase of the
companion programmes; their hardware experiments used separate IBM Quantum Open
Plan access.
