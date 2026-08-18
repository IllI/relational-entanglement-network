# One Budget: Why Correlation Magnitude Cannot Be a Shared Clock

**A synthesis of two independently-run hardware programmes, with two dedicated
runs of its own.**

The two programmes measure the same law from different directions. Placed
together they show something neither states alone: **every correlation
magnitude either programme measured is drawn on a single conserved unit, and
that unit is spent twice over** — once between a subsystem's local coherence
and its entanglement with a partner, once between its entanglement with one
partner and with another. Both totals are exactly 1.

The consequence is the point. A Page–Wootters clock is a good clock in
proportion to its entanglement with its own system. Any magnitude offered as a
*shared time* between two good clocks is therefore already spent. **No quantity
on this budget can be a shared clock** — and fifteen hardware runs are the
record of that budget being exhausted, observable by observable.

Both trade-offs were derived here, then measured on `ibm_marrakesh`:

| | measured | correlation |
|---|---|---|
| **within a pair** — local coherence vs entanglement | IBM-11, 53 circuits, 9/9 gates | **`r = −0.9573`** |
| **across two clocks** — own-system vs other-clock | IBM-12, 135 circuits, 6/6 gates | **`r = −0.9833`** |

The companions:

- **[twisted-spin-ptm](https://github.com/IllI/twisted-spin-ptm)** — the
  Pauli-transfer-matrix structure of one-axis-twisting boundary channels.
  Coherence measured against **coupling angle**.
  [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21878783.svg)](https://doi.org/10.5281/zenodo.21878783)
- **[relational-time-ibm-quantum](https://github.com/IllI/relational-time-ibm-quantum)**
  — whether relational time leaves a quantum signature distinguishable from its
  classical mimic; fifteen pre-registered runs, 77 jobs. Coherence measured
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
the deviation from uniform. For a bipartite **pure** state the marginal entropy
*is* the entanglement entropy, so entanglement with the system is exactly what
mixes the clock marginal, and a mixed marginal is exactly what flattens the
distribution the witness reads.

**This is not a new relation.** It is the `P = 0` slice of the Jakob–Bergou
complete complementarity relation

```
V² + P² + C² = 1        Jakob & Bergou, Phys. Rev. A 68, 022107 (2003)
```

with `V` the single-party visibility, `P` the predictability, `C` the
concurrence. The clock-marginal witness is `W = V/2`, and `P = 0` for this
family because the clock's populations are flat by construction — so
`(2W)² + C² = 1`. Stated here because the programme derived that relation
independently and it would be easy to present it as a finding. It is a known
theorem; **what is new is the hardware curve.**

| `d` | state | clock-marginal witness | entanglement |
|---|---|---|---|
| 2 | history | **0.000000** | **1.0000 ebits** |
| 2 | product | **0.500000** | 0.0000 ebits |
| 4 | history | 0.176777 | **1.0000 ebits** |
| 4 | product | **0.750000** | 0.0000 ebits |
| 8 | history | 0.496689 | **1.0000 ebits** |
| 8 | product | **0.875000** | 0.0000 ebits |

The witness is *highest* exactly where entanglement is *zero* — which
retrodicts a hardware number. The relational-time programme's IBM-2 run
prepared a zero-entanglement product state as an adversarial control and
measured it scoring **4.2× higher** than the real history state at `d = 4`. The
exact ratio above is `0.750 / 0.176777 = 4.24`. The adversary did not exploit a
loophole; it saturated a quantity that entanglement necessarily suppresses.

### Measured (IBM-11, 2026-08-17)

One parameter, from a product state to a Bell pair, measuring the marginal
witness **and** CHSH on each state — 53 circuits, two qubits, `ibm_marrakesh`,
9/9 pre-registered gates
([full results](https://github.com/IllI/relational-time-ibm-quantum/blob/main/docs/AQ_PAGE_WOOTTERS_IBM_11_RESULTS_2026-08-17.md)).

| λ | witness (exact) | CHSH (exact) |
|---|---|---|
| 0.00 | **0.4830** (0.5000) | **1.8605** (2.0000) |
| 0.25 | 0.4480 (0.4619) | 1.9995 (2.1414) |
| 0.50 | 0.3325 (0.3536) | 2.3085 (2.4495) |
| 0.75 | 0.1923 (0.1913) | 2.5500 (2.7229) |
| 1.00 | **0.0100** (0.0000) | **2.6565** (2.8284) |

**Witness–CHSH correlation `r = −0.9573`.** The state that maximises the
witness produced **no Bell violation at all** — CHSH `1.8605`, below the
classical bound, at the same λ where the witness peaks. That was the gate
written to falsify the framing, and it held.

The anti-correlation was **not guaranteed to survive**. For ideal pure states
it is forced; hardware states are mixed, where the marginal-entropy identity
fails and decoherence attacks marginal coherence and nonlocal correlation
through different channels at different rates. The trade-off held as
*structure* rather than value:

```
S² + 16W² :  7.1941  7.2093  7.0981  7.0939  7.0586
             mean 7.1308 (ideal 8.0, attenuation 0.891)
             spread 0.1507 against a ±1.1390 band
```

Decoherence lowers the level; it does not bend the curve — and the spread is
*flatter* than the noisy simulator predicted (0.4994 at attenuation 0.821). The
run beat its own noise model.

## 3. Across two clocks, it runs backwards again

Section 2 is a statement about one clock and its system. The question that
matters for relational time is different: **can two clocks share a time?**

A clock is a good Page–Wootters clock in proportion to its entanglement with
its **own** system — that is what makes it stationary and internally evolving.
It is a *synchronisable* clock in proportion to its entanglement with **another
clock**. Coffman–Kundu–Wootters monogamy makes those compete:

```
C²(A:Sₐ) + C²(A:B) + τ_ABC = 4·det ρ_A      Coffman, Kundu & Wootters,
                                             Phys. Rev. A 61, 052306 (2000)
```

For the family measured, `ρ_A` is maximally mixed and `τ_ABC = 0`, so the two
concurrences sum to exactly 1. **Again, the identity is not the claim** —
measuring a quantity fixed by construction is the mistake this programme made
twice already (IBM-6, IBM-8, both published as failures). It is asserted in
preflight and excluded from the gates. The claim is the **curve**, and the
**deficit** that mixedness introduces.

### Measured (IBM-12, 2026-08-17)

Three qubits — clock `A`, its system `Sₐ`, second clock `B` — with one
excitation-transfer angle `μ` moving `A`'s entanglement partner from `Sₐ` to
`B`. Full three-qubit tomography at each setting; 135 circuits, 6/6 gates
([full results](https://github.com/IllI/relational-time-ibm-quantum/blob/main/docs/AQ_PAGE_WOOTTERS_IBM_12_RESULTS_2026-08-17.md)).

| μ | C(A:Sₐ) | C(A:B) | S(A:Sₐ) | S(A:B) |
|---|---|---|---|---|
| 0.0000 | **0.8980** | **0.0000** | 2.6812 | 0.1239 |
| 0.3927 | 0.8056 | 0.2141 | 2.4368 | 1.0545 |
| 0.7854 | 0.5156 | 0.5315 | 1.8060 | 1.8350 |
| 1.1781 | 0.2282 | 0.7716 | 1.0093 | 2.4146 |
| 1.5708 | **0.0000** | **0.9017** | 0.1022 | 2.6780 |

**Clock-quality vs synchronisability correlation `r = −0.9833`, with both
endpoints reaching exactly zero.** A clock maximally entangled with its own
system has *no* measurable correlation with the second clock, and the converse
holds at the other end. That is the no-go — a perfect Page–Wootters clock is
uncorrelated with every other clock — measured rather than argued.

The CHSH columns cross cleanly: `2.68 → 0.10` on one pair while `0.12 → 2.68`
on the other. At the balance point **both sit at ≈1.8, below the classical
bound simultaneously.** Where the two clocks share time best, neither pair
violates Bell.

The mixedness deficit bows at the balanced point — but **that bow is an
estimator artifact**, since concurrence is `max(0, λ₁−λ₂−λ₃−λ₄)` and noise
biases it hardest at intermediate entanglement. A gate against the ideal `1.0`
would have manufactured a result. Against a noise-matched Aer reference run
through the same estimator, computed in-process before submission:

```
excess:  −0.0716  −0.0755  −0.0024  −0.0554  −0.0783
         spread 0.0760   against a 3σ bar of 0.2420
```

The spread collapses by a factor of 3.5 and sits well inside tolerance. **The
trade-off structure survives; only the level attenuates.** Every excess is
negative — hardware outperformed its own noise model at all five settings, the
second consecutive run to do so.

## 4. One budget, spent twice

Sections 2 and 3 are the same accounting seen from two sides. Run the verifier
and the two families print the *same numbers*:

```
lam    V (local coherence)         mu       C(A:Sa)
0.00   1.000000                    0.0000   1.000000
0.25   0.923880                    0.3927   0.923880
0.50   0.707107                    0.7854   0.707107
0.75   0.382683                    1.1781   0.382683
1.00   0.000000                    1.5708   0.000000
```

Two different three-qubit constructions, two different physical questions, one
curve. That is what "the same budget" means concretely.

**And mixedness never creates headroom.** If decoherence could push either
total above 1 there would be slack to spend, and the argument would be a
pure-state artifact. It cannot — verified under depolarizing noise at
`p ∈ {0, 0.05, 0.2, 0.5, 1}`, where both totals fall monotonically and neither
ever exceeds 1. **The exhaustion is stronger on hardware than on paper**, not
weaker.

> **The combined statement.** The survival of entanglement and the
> distinguishability of moments are the same quantity, measured in different
> variables. That quantity is conserved and it is spent twice: against the
> clock's own local coherence, and against every partner other than its own
> system. A Page–Wootters clock earns its quality by spending the budget on
> itself, which leaves nothing to spend on agreeing with anyone else.
> Therefore **no correlation magnitude can serve as a shared temporal
> reference between two good clocks.**

**What is and is not new here.** Both identities are standard, and the
obstruction for Page–Wootters clocks specifically is stated by
[Kuypers & Rijavec, *Measuring time in a timeless universe*](https://journals.aps.org/prd/pdf/10.1103/qfns-48vq)
(Phys. Rev. D **112**, 063544, 2025), who resolve it by adding an interaction
so the timer can read the clock. What appears not to have been done is
measuring either trade-off as a continuous hardware curve, or noting that the
two are one budget and that this exhausts the magnitude class.

**The scope of "exhausts".** The argument covers functions of the pairwise
correlation magnitudes — which is every observable either programme measured.
It does **not** cover genuine multipartite invariants: `τ_ABC` was zero by
construction in this family and is untouched by the argument. Nor does it cover
quantities that are not magnitudes at all, which is §8.

## 5. Two exact nulls

Each programme has an exact structural zero, predicted from theory,
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
correlator and does separate these states; the marginal witness cannot.
twisted-spin-ptm's null supplies the separable state that makes the marginal
blindness concrete rather than a single-programme curiosity.

Two cautions. `T_xx` separating these particular states does **not** make it an
entanglement witness — twisted-spin-ptm's own finding is that entanglement is
not identifiable from PTM anisotropy alone. And §2's anti-correlation is stated
for the pure-state family actually tested, not as a claim about every coherence
measure everywhere.

## 6. Independent convergence

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
single-setting joint rate, so the theorem in §7 applies to it directly: such a
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

## 7. The certification threshold

Both programmes hit the wall independently and resolved it the same way:

| | how it appeared | how it was resolved |
|---|---|---|
| **twisted-spin-ptm** | entanglement is not identifiable from PTM anisotropy alone | `V_Q` over Haar-random measurement settings |
| **relational-time** | no single local product-basis distribution certifies clock–system entanglement *(proved, then verified adversarially)* | multi-setting fidelity witness exceeding the exact separable bound `λ_max = ½` |

The relational-time programme got there the hard way, building two adversarial
states against its own results — the product state of §2 scoring 4.2× higher,
and a separable state scoring 1.7× higher on the joint witness built to repair
it — before a two-line theorem generalized the failure.

What follows is a **certification threshold** higher than the observables
usually offered as evidence for relational time can reach. Conditional
evolution is reproduced by a classical clock control. Local clock coherence is
*maximized* by a state with zero entanglement — measured, at CHSH 1.86, below
the classical bound. Single-basis joint correlation is beaten by a separable
state. What survives is a multi-setting witness — and, in IBM-10, a single
3-qubit preparation certified **entangled, stationary as a quantum ray, and
internally evolving simultaneously**.

## 8. The open door: a quantity that is not a magnitude

Section 4 closes the magnitude class. It does not close the question, because
**the geometric phase is not a magnitude.**

The Aharonov–Anandan phase is a property of the *path* traced in projective
Hilbert space, and it is **reparameterisation-invariant by construction** — it
depends on the loop, not on the rate at which the loop is traversed. That is
precisely the invariance a shared time between two clocks running at different
rates would have to possess. It is also the one property no magnitude in §4
has: concurrence and visibility are functions of the instantaneous state, blind
to the path that produced it.

**Why this is a question and not a claim.** Whether the AA phase is *also* on
the budget is not something we know. The geometric phase of entangled states is
well studied — Sjöqvist's two-particle geometric phase for entangled spins
depends on the degree of entanglement, so the phase is certainly not
*independent* of it. What is unclear is whether that dependence is a **trade**
in the §4 sense — a conserved total that spending on one pair removes from
another — or merely a functional dependence with no monogamy structure. Those
are different, and only the first would close the door.

**What the literature appears to contain, and not.** The three neighbouring
areas are each active: the AA phase of entangled states; relational /
Page–Wootters time; and geometric-phase metrology, including recent work on
geometric-phase amplification in clock interferometers. Quantum clock
synchronisation via pre-shared entanglement (Jozsa *et al.*, 2000, and
successors) *consumes* entanglement and classical communication — it does not
address clocks that have already spent their budget on their own systems. The
specific combination — magnitude is monogamy-constrained and therefore cannot
synchronise two perfect Page–Wootters clocks, while the AA phase is
reparameterisation-invariant and path-dependent and therefore might — does not
appear to have been developed as a concrete proposal under the obvious search
terms. **Stated as a survey result, not a priority claim:** absence under
search terms is weak evidence, and six times in this programme a "discovery"
turned out to be a known theorem. The first job of the next run is to be
attackable.

**The run that would settle it** is specified in
[`docs/NEXT_RUN_PROPOSAL.md`](docs/NEXT_RUN_PROPOSAL.md): take IBM-12's
three-qubit family around a closed loop at each `μ` and measure the AA phase of
both pairs interferometrically, with the loop built so the dynamical phase
vanishes by construction. It is decisive in both directions. If the phase
tracks `C²`, it is on the budget and the door closes — which would be the
seventh known theorem and worth knowing. If it stays flat while the
concurrences swap completely, it is the first quantity this programme has
measured that is **not** drawn on the budget.

Three further directions are specified but unexecuted in
[`docs/FUTURE_WORK.md`](docs/FUTURE_WORK.md).

## 9. Why the applied version does not work

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

## 10. What this does not claim

- **A synthesis with two runs, not a new programme.** Two completed programmes
  plus derivations, with two dedicated runs (IBM-11 and IBM-12, 188 circuits
  total) testing its central claims. Both are archived in the relational-time
  repository, whose numbering they continue. The original contributions here
  are the exact identification, the one-budget statement and its exhaustion
  consequence, the two hardware curves, and the applied bounds.
- **The identities are not ours.** Jakob–Bergou complementarity (2003) and
  Coffman–Kundu–Wootters monogamy (2000) are standard, and the Page–Wootters
  obstruction is stated by Kuypers & Rijavec (2025). The measured curves are
  ours; the theorems are not.
- **Substrate-blind.** The budget identities hold for *any* pure state, so
  nothing here is evidence for a common generative structure underlying
  different physical paradigms. Stated because that reading is tempting and
  wrong.
- **Nothing about quantum electrodynamics.** No gauge field, photon, or vacuum
  appears in either programme: OAT is a spin model and the Page–Wootters clock
  is engineered qubits.
- **Nothing about time in nature.** Neither companion claims time is emergent,
  tests the Wheeler–DeWitt constraint, or realizes a physical Page–Wootters
  universe. Both states are prepared by externally timed gates, and both
  clock/system splits are imposed rather than derived. The endpoints measured
  at exactly zero are a statement about correlation between engineered
  registers, not about simultaneity in nature.
- **Not peer-reviewed.** These are archived research records.

## Repository layout

```
theory/     the companion result, executable end to end
            (verify_companion_result.py) -- numpy only, no QPU
docs/       COMPANION_RESULT.md   the full statement
            NEXT_RUN_PROPOSAL.md  the geometric-phase run
            PROGRAM_HISTORY.md    where the questions came from
            FUTURE_WORK.md        specified but unexecuted directions
```

## Acknowledgments

Research supported with Cloud TPUs from Google's TPU Research Cloud (TRC). The
TRC allocation supported the simulation and hypothesis-development phase of the
companion programmes; their hardware experiments used separate IBM Quantum Open
Plan access.
