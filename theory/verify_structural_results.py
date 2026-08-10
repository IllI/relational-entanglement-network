#!/usr/bin/env python3
"""Theory layer: what is CONTINGENT and what is forced.

This program's predecessor spent two hardware runs (IBM-6, IBM-8) measuring a
quantity that was fixed by construction -- the constraint eigenvalue of a
cyclic history state is exactly +1 by a two-line argument, so there was never a
phase for hardware to find. The standing rule that came out of it:

    DERIVE WHETHER A QUANTITY IS CONTINGENT BEFORE DESIGNING A RUN TO MEASURE IT.

This file applies that rule to this program BEFORE any circuit exists. It is
executable so the claims can be checked rather than believed. No dependencies
beyond numpy; no QPU; runs in under a second.

    python theory/verify_structural_results.py
"""

from __future__ import annotations

import numpy as np

C_LIGHT = 299_792_458.0


# --------------------------------------------------------------------------
# Result 1 -- rate loop closure is AUTOMATIC, not contingent
# --------------------------------------------------------------------------

def rate_between(x: np.ndarray, y: np.ndarray, d: int) -> int | None:
    """Multiplier m with y = m*x (mod d), or None if no such m exists."""
    for m in range(d):
        if np.all((m * x) % d == y % d):
            return m
    return None


def result1_loop_closure() -> bool:
    """For |Psi> = (1/sqrt d) sum_t |t>_A |a t>_B |b t>_C the pairwise rates are
    a, b/a and 1/b, whose product telescopes to 1 IDENTICALLY.

    A run pre-registering "the loop closes" would therefore be measuring a
    theorem. The contingent content is whether CONTROL networks admit any
    consistent assignment at all -- that is the discriminating test."""
    print("RESULT 1 -- rate loop closure alpha_AB * alpha_BC * alpha_CA")
    print("  symbolically: a * (b/a) * (1/b) = 1  for ALL a, b\n")
    ok = True
    for d in (8, 12, 16):
        t = np.arange(d)
        for a in range(1, d):
            for b in range(1, d):
                A, B, C = t % d, (a * t) % d, (b * t) % d
                rAB, rBC, rCA = (rate_between(A, B, d), rate_between(B, C, d),
                                 rate_between(C, A, d))
                if None in (rAB, rBC, rCA):
                    continue                     # undefined -- see result 2
                prod = (rAB * rBC * rCA) % d
                if prod != 1:
                    print(f"    COUNTEREXAMPLE d={d} a={a} b={b}: product={prod}")
                    ok = False
    print(f"  checked d in (8,12,16), all (a,b): product == 1 wherever defined -> {ok}")
    print("  => NOT a physics gate. Use only as a consistency check on the prep.\n")
    return ok


# --------------------------------------------------------------------------
# Result 2 -- a clock is a usable reference frame only if gcd(alpha, d) = 1
# --------------------------------------------------------------------------

def result2_invertibility() -> bool:
    """A clock B running at rate a can serve as a REFERENCE FRAME only if
    gcd(a, d) = 1.

    Care is needed about which direction is being asked, and a first draft of
    this check got it wrong. The rate FROM the summation label TO B is always
    defined -- it is a, by construction. What can fail is the other direction:
    recovering the shared label from B's readings, which is what "use B as the
    clock" actually requires. That needs t -> a*t mod d to be injective, i.e.
    gcd(a, d) = 1. Equivalently: B->C is expressible as a rate iff a is
    invertible, since b = m*a (mod d) must be solvable for m.

    Distinct from IBM-7 commensurability, which is about exact cycle closure
    after d ticks; this is about whether a clock has the RESOLUTION to index
    the others at all."""
    print("RESULT 2 -- a clock is a usable frame only if gcd(rate, d) = 1")
    ok = True
    for d in (8, 12, 16):
        t = np.arange(d)
        for a in range(1, d):
            readings = (a * t) % d
            injective = len(set(readings.tolist())) == d       # B distinguishes all t
            recoverable = rate_between(readings, t, d) is not None  # t from B
            coprime = int(np.gcd(a, d)) == 1
            if not (injective == recoverable == coprime):
                print(f"    MISMATCH d={d} a={a}: inj={injective} "
                      f"recoverable={recoverable} coprime={coprime}")
                ok = False
        usable = [a for a in range(1, d) if np.gcd(a, d) == 1]
        print(f"  d={d:>2}: usable frame rates {usable}  ({len(usable)} of {d-1})")
    print(f"  injective <=> label-recoverable <=> coprime, exactly -> {ok}")
    print("  => a finite clock cannot serve as a frame at every rate. This is a")
    print("     THEORY constraint on run design (choose coprime rates), not a gate.\n")
    return ok


# --------------------------------------------------------------------------
# Result 3 -- relativistic "buffering" is a TRADE, and negligible in practice
# --------------------------------------------------------------------------

def result3_relativistic_budget() -> bool:
    """Time dilation does not accelerate computation. If a memory's T2 is
    defined in local proper time, an Earth observer sees coherence decay as
    exp(-t/(gamma*T2)) -- storage lengthened by gamma in EARTH-FRAME seconds --
    while local operations per Earth-second fall by exactly the same gamma.

    Net: no gain in operations-per-coherence-time. The only niche is when the
    figure of merit is Earth-frame duration (e.g. waiting for an orbital pass)
    and no local processing is needed meanwhile.

    And at achievable velocities the effect is ~1e-10, so this is a programmable
    EMULATION target, never a satellite technology."""
    print("RESULT 3 -- relativistic buffering: a trade, and negligible in practice")
    print("  gamma   Earth-frame storage   local ops per Earth-sec   ops per coherence time")
    for g in (2.0, 10.0):
        print(f"  {g:<7.0f} x{g:<19.0f} x{1/g:<23.3f} x{g*(1/g):.3f}  (unchanged)")
    print()
    print("  achievable velocities:")
    rows = [("ISS (LEO)", 7660.0), ("GPS (MEO)", 3874.0), ("Parker Solar Probe", 192_000.0)]
    for name, v in rows:
        b = v / C_LIGHT
        g = 1.0 / np.sqrt(1 - b * b)
        print(f"    {name:<20} beta={b:.3e}  gamma-1={g-1:.3e}  storage gain {(g-1)*100:.2e} %")
    # GPS closure check against the published +38 us/day
    v, b = 3874.0, 3874.0 / C_LIGHT
    sr = -(0.5 * b * b) * 86400 * 1e6
    G, M, R, r = 6.674e-11, 5.972e24, 6.371e6, 2.6561e7
    gr = ((G * M / C_LIGHT**2) * (1 / R - 1 / r)) * 86400 * 1e6
    print(f"\n  GPS check: SR {sr:+.2f} + GR {gr:+.2f} = {sr+gr:+.2f} us/day (published +38)")
    ok = abs((sr + gr) - 38.0) < 1.5
    print(f"  reproduces the standard value -> {ok}")
    print("  => relativistic dynamics are PROGRAMMED in Run D, never physically present.\n")
    return ok


# --------------------------------------------------------------------------
# Result 4 -- information-theoretic ceiling on "semantic compression"
# --------------------------------------------------------------------------

def result4_capacity_ceiling() -> bool:
    """Holevo: n transmitted qubits carry at most n classical bits without
    pre-shared entanglement; superdense coding reaches 2n bits WITH it. There is
    no regime in which a handful of qubits releases terabytes.

    Consequence for this program: 'semantic compression' must earn its
    compression conventionally -- redundancy, low-dimensional latent structure,
    task relevance -- exactly what the D-LinOSS/classical layer is for. The
    quantum layer transports a compact relational state; it does not repeal
    information theory."""
    print("RESULT 4 -- capacity ceiling on the payload")
    print("   qubits   Holevo (no shared ent.)   superdense (shared ent.)")
    for n in (1, 5, 10, 20):
        print(f"   {n:<8} {n:<25} {2*n}")
    print("  => the compression must happen in the CLASSICAL/semantic layer.")
    print("     The quantum layer's claim is transport of relational structure,")
    print("     not information density.\n")
    return True


if __name__ == "__main__":
    print("=" * 74)
    print("relational-entanglement-network -- structural results,")
    print("derived BEFORE any run is designed")
    print("=" * 74 + "\n")
    results = [result1_loop_closure(), result2_invertibility(),
               result3_relativistic_budget(), result4_capacity_ceiling()]
    print("=" * 74)
    print(f"all structural checks pass: {all(results)}")
    print("=" * 74)
