# Specified, unexecuted

Three directions that follow from the companion result. None has been run, and
each is written to be attackable rather than plausible.

> **These are not the priority.** The one direction that bears directly on the
> open question — whether the Aharonov–Anandan geometric phase is on the
> entanglement budget, and therefore whether *any* quantity can be a shared
> temporal reference between two good clocks — is
> [`NEXT_RUN_PROPOSAL.md`](NEXT_RUN_PROPOSAL.md). It is cheap, decisive in both
> directions, and should be run before anything below. The three here are
> broader programme directions rather than tests of the central claim.

A fourth — a three-clock relational network with no privileged frame — belongs
to the relational-time programme rather than here, since it sharpens that
programme's own limitation about the clock being chosen rather than derived. It
lives in
[`AQ_PAGE_WOOTTERS_IBM_11_RELATIONAL_NETWORK_PROPOSAL.md`](https://github.com/IllI/relational-time-ibm-quantum/blob/main/docs/AQ_PAGE_WOOTTERS_IBM_11_RELATIONAL_NETWORK_PROPOSAL.md),
with its two structural constraints executable at
[`theory/verify_clock_structure.py`](https://github.com/IllI/relational-time-ibm-quantum/blob/main/theory/verify_clock_structure.py).

---

## A — Self-timed semantic state

Encode a small semantic alphabet into a history state that carries its own
clock and subclock:

```
|Ψ_m⟩ = Σ_t A_m(t) |t⟩_clock-network ⊗ |φ_m(t)⟩_payload
```

Test held-out semantic recovery **only with the correct relational frame**,
against explicit wrong-frame and swapped-frame controls.

*What makes it non-trivial:* the predecessor's semantic-transport experiments
recovered identity perfectly (motif/source/target all `1.0000`) while numerical
fidelity degraded. The interesting question is whether the same split appears
when the payload is carried by a genuine quantum state rather than a simulated
state-space model — identity surviving where values do not.

## B — Relational-state teleportation

Teleport that logical state and certify four things at the receiver: state
fidelity, semantic identity, the internal clock/subclock trajectory, and
clock–payload entanglement.

The question is whether **relational history itself is transportable as quantum
information**, or whether the temporal structure is exactly what teleportation
fails to preserve.

*Bound to respect:* the payload cannot exceed the Holevo limit. This tests
whether *relational structure* survives transport, not whether information
density can be beaten — see §4 of the README.

## C — Relativistic frame emulation

Program differing proper-time rates, memory decoherence, and phase
accumulation. Compare uncompensated transport against analytic relativistic
correction, linear/Kalman filtering, and D-LinOSS.

The real question is whether a **learned** relational-frame observer improves
fidelity under noisy, time-varying channels.

*Prior to respect:* across the predecessor campaign, **D-LinOSS never beat its
linear baselines on any real-data task** — every recorded `D-LinOSS − ridge`
value is negative, and it was retired from detector duty in the astrophysics
branch. Its value there was diagnostic: its *structured* failures named the
right variables. A run that expects it to win has not read the record. A run
that asks *where the structure of its failure is informative* has.

*And the emulation is emulation:* relativistic rates are programmed into the
circuit. At achievable velocities `γ − 1 ≈ 10⁻¹⁰`, so nothing here is
physically relativistic.

---

## Feasibility, honestly

Any of these needs more qubits and more depth than the relational-time
programme's largest run (IBM-10: 19 circuits, 3 qubits, ≤9 CX). The
three-clock network alone was costed at 7–8 qubits, ~30 CX of
modular-multiplication preparation, and 50–100 circuits — against a free-tier
trial that could not fund it with retry margin.

None of this is scoped to an expiring allocation. The structural results exist
precisely so that whenever hardware time does appear, it is not spent measuring
something a two-line derivation already fixed.
