# Next run: is the geometric phase on the budget?

**Priority proposal.** The previous proposal in this file — measure the
anti-correlation directly — was executed as **IBM-11** (9/9 gates,
`r = −0.9573`), and its across-clocks counterpart as **IBM-12** (6/6,
`r = −0.9833`). Both are archived in the relational-time repository. This
replaces it.

---

## Why this run

README §4 closes the magnitude class: every correlation magnitude either
programme measured is drawn on one conserved unit, spent against local
coherence within a pair (Jakob–Bergou) and against every other partner across
pairs (Coffman–Kundu–Wootters). A Page–Wootters clock earns its quality by
spending that budget on its own system, which leaves nothing to spend on
agreeing with another clock.

The Aharonov–Anandan phase is **not a magnitude**. It is a property of the path
traced in projective Hilbert space, and it is reparameterisation-invariant — it
depends on the loop, not on the rate at which the loop is traversed. That is
exactly the invariance a shared time between two clocks running at different
rates would need.

**Whether it is also on the budget is unknown to us**, and appears not to be
settled in the literature (README §8). This run is designed to answer it in
either direction.

## The observable, chosen to avoid the obvious confound

The naive design — drive a loop on clock `A` in IBM-12's family and watch the
phase across `μ` — **does not work, and the reason is worth recording.** In
that family `ρ_A` is maximally mixed at every `μ` (that is precisely why the
CKW identity saturates), so the interferometric visibility on `A` is zero and
no phase is readable. Driving the loop on `Sₐ` or `B` instead reintroduces a
different confound: their Bloch-vector lengths are `sin²μ` and `cos²μ`, so the
mixed-state geometric phase varies with `μ` *through the marginal purity alone*
(Sjöqvist *et al.*, Phys. Rev. Lett. **85**, 2845, 2000, gives it in closed
form). A sweep of that quantity would be measuring a known function of a
quantity already measured — the IBM-6 / IBM-8 mistake for a third time.

So the run does not sweep phase against entanglement. **It tests the
invariance directly.**

## The design

Four qubits: interferometric ancilla `R`, clock `A`, clock `B`, and system `Sₐ`
for the budget arm. One job.

1. Prepare the two clocks and put `R` in `|+⟩`.
2. **Trace the same loop at two different rates.** A closed loop `L(Ω)` of
   solid angle `Ω` in projective Hilbert space is decomposed into `n` segments
   on `A` and into `n' = α·n` segments on `B`. Same loop, same `Ω`, different
   parameterisation — one clock runs `α` times faster than the other.
3. **Kill the dynamical phase by construction.** The loop is built as an
   echoed composite sequence with `⟨H⟩ = 0` segment by segment, the standard
   superconducting Berry-phase construction (Leek *et al.*, *Science* **318**,
   1889, 2007). Verified in statevector before submission, per standing
   discipline, so the measured Pancharatnam phase *is* the geometric phase.
4. Read `⟨X_R⟩` and `⟨Y_R⟩` to recover `arg⟨Ψ|L|Ψ⟩` and the interferometric
   visibility.

Sweep `α ∈ {1, 1.5, 2, 2.5, 3}` — deliberately IBM-7's range, including the
non-integer values where that run measured the *dynamical* constraint failing
to close — and `Ω ∈ {π/2, π, 3π/2}`.

Roughly 150 circuits at 2 000 shots, one job, comparable to IBM-12.

## Pre-registered gates

1. **Non-vacuity (must pass first).** The *dynamical* phases of the two clocks
   must differ by the programmed factor `α`, measured, at every `α ≠ 1`. If
   they agree, the two arms are not actually running at different rates and
   every other gate is meaningless. This gate exists because a test where both
   quantities agree trivially is the failure mode this programme has fallen
   into before.
2. **Reparameterisation invariance.** `|γ_A − γ_B| < 3σ` at every `α`, with σ
   from a setting-wise multinomial bootstrap. This is the claim.
3. **Solid-angle tracking.** At fixed `α`, `γ` tracks `Ω` and not the segment
   count `n`, across at least three values of each. Invariance means depending
   on the loop, not on how it was cut up.
4. **Budget independence.** Repeat gates 2–3 at `μ = 0` (`C(A:B) = 0.0000`,
   measured in IBM-12) and at `μ = π/2` (`C(A:B) = 0.9017`). Agreement must
   hold at both. If it holds only where the clocks are correlated, the phase is
   on the budget after all.
5. **Noise-matched reference.** All gates evaluated as excess over an Aer
   reference at the live calibration, computed in-process before submission —
   the IBM-11 / IBM-12 pattern, not against ideal values.

## Both outcomes are informative

**If `γ_A ≠ γ_B` off the integer points**, or agreement collapses at `μ = 0`,
the geometric phase is on the budget. The magnitude class and the geometric
class are one class, the exhaustion argument extends, and the answer to "can
two Page–Wootters clocks share a time" is no more broadly than §4 currently
supports. That would very likely be a known theorem — the seventh — and worth
finding out cheaply.

**If `γ_A = γ_B` at non-integer `α`, including at `μ = 0`**, then this
programme has measured a quantity that is *not* drawn on the budget: two clocks
with exactly zero mutual correlation agreeing on a phase, at rates where IBM-7
showed the dynamical constraint does not close. That is the first candidate for
a shared temporal reference this line has found, and it would be the thing to
write up.

## What it would still not show

The loops are **externally programmed**, as every state in this programme is.
Two uncorrelated clocks agreeing on the phase of a loop they were each
independently instructed to trace is not, by itself, a shared time in any
observer-free sense — it is two systems computing the same function of the same
instruction. What the run establishes is narrower and worth having: whether the
geometric phase possesses the *invariance* a shared time would require, and
whether that invariance survives independently of the entanglement budget.

Closing the external-timing gap is limitation 1 of the relational-time
programme and is not closed by this run, or by any run in it.

## Prior to respect

Six times in this programme a derived "discovery" turned out to be a known
theorem — most recently `(2W)² + C² = 1`, which is Jakob–Bergou (2003). Before
this run is built, the literature sweep in README §8 should be repeated against
the specific gate-2 statement rather than the general topic. The searches
performed so far cover the AA phase of entangled states, relational and
Page–Wootters time, geometric-phase metrology in clock interferometers, and
entanglement-assisted clock synchronisation; none addresses rate-invariant
phase agreement between clocks that have spent their entanglement locally. That
is suggestive and not conclusive.
