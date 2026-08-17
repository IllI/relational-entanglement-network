# Relational Clock Networks and Self-Timed Quantum States

A second research line, deliberately separate from the
Page–Wootters program in
[relational-time-ibm-quantum](https://github.com/IllI/relational-time-ibm-quantum),
which is complete at eleven hardware runs and stands on its own.

**Status: theory layer only. No hardware run has been executed.** What exists
here is a four-run progression, its honest boundaries, and four structural
results derived at zero QPU cost — three of which constrain the run designs
before any circuit is written.

> **This is not a cold start.** Two of those four results are the mature
> answers to concrete engineering questions asked at the beginning of a
> two-year line of work — *can entangled states carry compressed data off a
> satellite*, and *does time dilation buy processing headroom* — and both
> answers are **no**, for reasons now derivable rather than discoverable by
> another expensive run. [`docs/PROGRAM_HISTORY.md`](docs/PROGRAM_HISTORY.md)
> is the account: the yin/yang semantic-transport experiments, the TPU
> campaign and its falsified hypotheses, the astrophysics deviation where
> D-LinOSS failed its promotion gates, and the eleven QPU runs that followed.

---

## The thesis

> Temporal information in an engineered quantum network can be represented
> entirely by **relations among physical clocks**, with no privileged master
> clock required by the model.

The predecessor program established what relational-time observables certify,
and closed with a history state shown entangled, ray-stationary, and internally
evolving on a single preparation. But it always **chose** its clock. That was
limitation 2 of that paper, and it is the target here.

The operational claim this program could support — not a claim about nature:

```
local states alone      ⇏   temporal order
network of relations     ⇒   recoverable temporal order
```

Concretely: hold every local marginal `ρ_A, ρ_B, ρ_C` fixed, alter **only** the
relational correlations, and show the reconstructable temporal ordering
changes. Then switch among reference clocks and recover mutually consistent
descriptions. Then certify the network correlations are genuinely quantum.

This is closely aligned with existing spacetime quantum-reference-frame theory,
where dynamics are described from the proper time of physical quantum clocks
and superpositions of proper times can arise
([arXiv:2101.11628](https://arxiv.org/abs/2101.11628)).

---

## Structural results, derived before any run

`python theory/verify_structural_results.py` — no dependencies beyond numpy,
no QPU, under a second. These exist because the predecessor program **spent two
hardware runs measuring a quantity that was fixed by construction** (IBM-6 and
IBM-8, chasing an eigenvalue that was `+1` by a two-line argument). The rule
that came out of it governs this repository:

> **Derive whether a quantity is contingent before designing a run to measure
> it.**

### 1. Rate loop closure is automatic — do not make it a gate

For `|Ψ⟩ = (1/√d) Σ_t |t⟩_A |αt⟩_B |βt⟩_C`, the pairwise rates telescope:

```
α_AB = α        α_BC = β/α        α_CA = 1/β
α_AB · α_BC · α_CA = 1        identically, for all α, β
```

Verified exhaustively for `d ∈ {8, 12, 16}` over all `(α, β)`. **A run
pre-registering "the loop closes" would be measuring a theorem.** The
contingent content is whether *control* networks admit any consistent
assignment at all — that is the discriminating test, and the claim must be a
comparison rather than a verification.

### 2. A clock is a usable reference frame only if `gcd(rate, d) = 1`

Using B as the clock requires recovering the shared label from B's readings,
which requires `t ↦ αt mod d` to be injective. At `d = 12` only **4 of 11**
rates qualify (`α ∈ {1, 5, 7, 11}`). This is a hard design constraint on Run A,
and it is distinct from the predecessor's commensurability result — that one is
about exact cycle closure after `d` ticks, this is about whether a clock has
the **resolution** to index the others at all.

*(A first draft of this check tested the wrong direction and reported a false
mismatch. It is written as executable code precisely so that such errors
surface. The corrected form is in the file.)*

### 3. Relativistic time dilation is a trade, not an accelerator

| γ | Earth-frame storage | local ops per Earth-second | ops per coherence time |
|---|---|---|---|
| 2 | ×2 | ×0.5 | **×1 — unchanged** |
| 10 | ×10 | ×0.1 | **×1 — unchanged** |

If a memory's `T₂` is defined in local proper time, an Earth observer sees
`exp(−t/(γT₂))` — storage lengthened by γ in *Earth-frame* seconds — while
local operations per Earth-second fall by exactly the same γ. **A dilated node
does not compute more; it computes less, more slowly.** The only niche is when
the figure of merit is Earth-frame duration (waiting for an orbital pass) and
no local processing is needed meanwhile.

And the magnitude kills it as a technology:

| platform | β | γ−1 | storage gain |
|---|---|---|---|
| ISS (LEO) | 2.6×10⁻⁵ | 3.3×10⁻¹⁰ | 3×10⁻⁸ % |
| GPS (MEO) | 1.3×10⁻⁵ | 8.3×10⁻¹¹ | 8×10⁻⁹ % |
| Parker Solar Probe | 6.4×10⁻⁴ | 2.1×10⁻⁷ | 2×10⁻⁵ % |

The machinery reproduces the standard GPS budget as a check
(SR −7.21 + GR +45.72 = **+38.50 µs/day**, published +38). **Run D therefore
programs relativistic rates into a circuit; it never contains relativity.**

### 4. Capacity ceiling — the compression must be classical

Holevo bounds `n` transmitted qubits at `n` classical bits without pre-shared
entanglement; superdense coding reaches `2n` with it. There is no regime where
a handful of qubits releases terabytes. **"Semantic compression" must earn its
compression conventionally** — redundancy, low-dimensional latent structure,
task relevance — which is exactly the classical/D-LinOSS layer's job. The
quantum layer's claim is *transport of relational structure*, not information
density.

---

## The four runs

Each is a separate pre-registered experiment, hardest last. **None has been
executed.**

### Run A — Relational network
Three clocks, no master clock anywhere in the measurements. Reconstruct
mutually consistent histories from pairwise correlations alone; then rewire or
sever correlations **while preserving every local marginal** and show
reconstruction fails. Result 2 constrains the rate choices; result 1 says loop
closure is a prep consistency check, never a physics gate.

Controls, following the predecessor's adversarial method: shuffle `A↔B`
pairing; sever `B↔C`; reverse one edge; substitute a classically correlated
mixture; detune one rate; randomly rewire labels.

### Run B — Self-timed semantic state
Encode a small semantic alphabet into a history state carrying a clock and
subclock:

```
|Ψ_m⟩ = Σ_t A_m(t) |t⟩_clock-network ⊗ |φ_m(t)⟩_payload
```

Test held-out semantic recovery **only with the correct relational frame**,
against explicit wrong-frame and swapped-frame controls.

### Run C — Relational-state teleportation
Teleport that logical state and certify four things at the receiver: state
fidelity, semantic identity, the internal clock/subclock trajectory, and
clock–payload entanglement. The question is whether **relational history itself
is transportable as quantum information**.

### Run D — Relativistic frame emulation
Program differing proper-time rates, memory decoherence, and phase
accumulation. Compare uncompensated transport against analytic relativistic
correction, linear/Kalman filtering, and D-LinOSS. The real question is whether
a *learned* relational-frame observer improves fidelity under noisy,
time-varying channels — which is where D-LinOSS's structural role from the
predecessor program carries over.

---

## What this program could and could not claim

**Could**, if all four succeeded:

> In this engineered system, all experimentally recoverable temporal
> information is carried by a self-consistent network of relations among
> subsystems. No single subsystem contains the ordering, no privileged master
> clock is needed to reconstruct it, and rewiring the relations destroys the
> common temporal description while leaving every local marginal unchanged.

**Could not**, under any outcome:

- That this is how time works in nature. The relativistic dynamics are
  programmed into the circuit; the state is prepared by externally timed gates
  in ordinary laboratory time.
- That the clock is *derived*. Even full success shows no **unique** master
  clock is needed among clocks we chose and engineered.
- Any information-density advantage. See result 4.
- Any computational speedup from time dilation. See result 3.

The right framing for the applied end of this program is:

> A distributed system compresses raw observations into task-relevant semantic
> representations, encodes selected information into self-timed relational
> quantum states, and uses quantum memories plus relativistic reference-frame
> tracking to preserve and route those states asynchronously between moving
> nodes.

For ordinary classical datasets, classical compression and networking remain
the sensible baseline and this scheme would have to beat them to justify
itself. The genuine motivation is **quantum-generated data**: distributed
quantum sensors whose states you would rather move than measure and
classicalize at the remote node.

---

## Repository layout

```
theory/     structural results, executable (verify_structural_results.py)
docs/       per-run specifications as they are written
```

## Relationship to the other programs

- **Paper 1** — [twisted-spin-ptm](https://github.com/IllI/twisted-spin-ptm):
  OAT / bi-twistor PTM. Source of the `V_Q` many-settings certification
  standard.
- **Paper 2** — [relational-time-ibm-quantum](https://github.com/IllI/relational-time-ibm-quantum):
  the Page–Wootters program, complete at 11 runs / 72 jobs. This program begins
  where its limitation 2 ends.

## Acknowledgments

Google TPU Research Cloud (TRC) funded the simulation phase of the predecessor
program (`v6e`, 2026-04-21 → 2026-06-21), which produced the D-LinOSS lineage
and the certification standard this program inherits. IBM Quantum Open Plan
provided the hardware for the predecessor's eleven runs.
