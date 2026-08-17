# Next run: measure the anti-correlation directly

**Priority proposal.** Cheap, decisive, and it tests this repository's central
claim on hardware rather than leaving it derived. It also closes the loop back
to the CHRONOS telemetry nulls that opened the whole line.

---

## The claim to be tested

Read on a marginal, the coherence law runs *backwards*: the states that score
highest are the least entangled. Derived exactly (README §2), and it already
reproduces IBM-2's measured 4.2× — but it has never been swept as a
**continuous** relationship on hardware.

## The design

One tunable family at `d = 2`, interpolating from product to maximally
entangled:

```
|Ψ(λ)⟩ = (1/√2) Σ_t |t⟩_C ⊗ Ry(λ·t·θ)|0⟩_S        θ = 2π/d
```

`λ = 0` is the zero-entanglement product state; `λ = 1` is the history state,
which at `d = 2` is a Bell pair. On each state measure **two things**:

- the **clock-marginal witness** — Fourier-basis readout, TVD from uniform
- the **CHSH value** — four two-qubit settings, the standard Bell test

Exact predictions:

| λ | marginal witness | entanglement | CHSH |
|---|---|---|---|
| 0.00 | **0.5000** | 0.0000 ebits | **2.0000** |
| 0.25 | 0.4619 | 0.2333 | 2.1414 |
| 0.50 | 0.3536 | 0.6009 | 2.4495 |
| 0.75 | 0.1913 | 0.8916 | 2.7229 |
| 1.00 | **0.0000** | 1.0000 ebits | **2.8284** |

The endpoints are the result in miniature: **the state that maximizes the
coherence witness sits exactly at the classical CHSH boundary of 2, and the
state that saturates Tsirelson's bound has a witness of exactly zero.**

## Is this contingent, or a theorem?

The standing rule of this programme is to ask before designing the run, because
two hardware runs were once spent measuring a quantity fixed by construction.

**For ideal pure states the anti-correlation is forced** — marginal entropy *is*
entanglement entropy, so sweeping it on paper measures a theorem.

**On hardware it is contingent**, and that is the run's content. Prepared
states are mixed, and for mixed states marginal entropy is no longer the
entanglement entropy. Decoherence attacks marginal coherence and nonlocal
correlation through different channels and at different rates. Whether the
anti-correlation survives — and with what slope — is a genuine empirical
question that no derivation settles.

Pre-register accordingly: the gates are about the *measured* relationship, not
about reproducing the ideal curve.

## Pre-registered gates

1. **Monotone witness.** Measured witness decreases across λ, each step beyond
   shot noise.
2. **Monotone CHSH.** Measured CHSH increases across λ, each step beyond shot
   noise.
3. **Anti-correlation.** Pearson `r` between witness and CHSH across the sweep
   is `< −0.9`.
4. **Classical endpoint.** At `λ = 0`: witness is maximal *and* CHSH does not
   exceed 2 by more than 3σ. A violation here would falsify the framing.
5. **Quantum endpoint.** At `λ = 1`: witness consistent with zero *and* CHSH
   exceeds 2 by more than 3σ.

Gate 4 is the honest one — it is the gate this proposal can fail.

## Controls, following the programme's method

- **Relative time shift.** Apply an offset between the two registers before
  readout. This is the quantum analogue of the CHRONOS one-hour-offset control
  that closed the telemetry line, and it should destroy the joint structure
  while leaving both marginals intact.
- **Separable mixture at matched marginals.** Prepare a classically correlated
  mixture engineered to reproduce the λ-sweep's marginals exactly. It should
  track the witness curve and *fail* to track CHSH — the sharpest possible
  demonstration that the two observables see different things.
- **Basis shuffle.** Randomize the CHSH setting assignment; the violation must
  disappear.

## Cost

`d = 2`, two qubits. Five λ points × (4 CHSH settings + 1 witness circuit) = 25
circuits, plus controls — comparable to IBM-10's 19 circuits and far below
IBM-8's fatal depth. **This is the cheapest decisive run in the programme's
history.**

## Why this closes the CHRONOS loop

The TRC proposal was about **time emission**. CHRONOS asked it directly: do two
independent, separated systems share learnable temporal structure? It looked at
each host's **marginal** stream, correlated the features, and found `r ≈ 0.57`
— which then **survived a one-hour artificial offset** at `r ≈ 0.50`. Structural
similarity, not shared time. The line closed.

That null now reads as the classical face of this repository's result.
**Marginals cannot carry relational temporal structure** — not because the
telemetry was bad, but because marginal observables are the wrong object. The
quantum version can carry it, in the joint record, and CHSH certifies that it
is there.

Svozil's construction ([arXiv:2512.09100](https://arxiv.org/abs/2512.09100))
is exactly this: a singlet shared between separated observers, marginal tick
rates pinned at `1/2` and carrying nothing, temporal structure living only in
the joint coincidence record, certified device-independently.

So the next paper's thesis writes itself from both sides:

> Relational temporal structure is carried by joint correlations and is
> invisible — indeed anti-correlated — in the marginals. The classical null and
> the quantum positive are the same statement, measured from opposite
> directions: CHRONOS failed because it read marginals, and a Bell-certified
> quantum clock succeeds because it does not.

## What it would and would not establish

**Would:** the first *device-independent-style* certification in the programme,
addressing the relational-time paper's limitation 5, which currently records
device-dependence as unclosed. A CHSH violation does not assume the measurement
operators are what their labels say; a fidelity witness does.

**Would not:** make it loophole-free. Two qubits on one superconducting
processor are not spacelike separated, so the no-signalling and fair-sampling
assumptions are not enforced by the geometry. That limitation is already stated
in the relational-time paper and this run does not remove it. Genuine
device-independence needs physically separated parties.
