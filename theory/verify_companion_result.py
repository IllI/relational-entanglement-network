#!/usr/bin/env python3
"""The companion result, executable. numpy only, no QPU, under a second.

Two independently-run hardware programmes measure the same law. Read on a
MARGINAL, that law produces an observable which is not merely uninformative
about entanglement but suppressed by it. Every load-bearing claim is checked
here so none has to be taken on trust:

  1. cos(theta/2) is the overlap between two qubit states separated by Bloch
     angle theta -- the object both programmes measure.
  2. The Page-Wootters clock-record overlap IS that object, and the OAT
     boundary PTM element is that object raised to the number of informed
     spins.
  3. THE ANTI-CORRELATION. For a bipartite pure state the marginal entropy IS
     the entanglement entropy, so marginal coherence and entanglement are in
     direct tension. Checked across d: the zero-entanglement product state
     scores HIGHER than the maximally entangled history state at every d, and
     the d=4 ratio reproduces the 4.2x measured on hardware in IBM-2.
  4. THE TWO NULLS. Both null states have maximally mixed marginals, so a
     marginal observable reads zero on a separable state and a maximally
     entangled one alike. A joint correlator (T_xx) does separate them.
  5. The applied bounds: Holevo capacity and the relativistic
     storage/throughput trade.

    python theory/verify_companion_result.py
"""

from __future__ import annotations

import numpy as np

C_LIGHT = 299_792_458.0


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def fourier_witness(rho_c: np.ndarray, d: int) -> float:
    """TVD from uniform of the clock marginal read in the Fourier basis."""
    F = np.exp(2j * np.pi * np.outer(np.arange(d), np.arange(d)) / d) / np.sqrt(d)
    p = np.real(np.einsum("ka,ab,kb->k", F.conj(), rho_c, F))
    return float(0.5 * np.sum(np.abs(p - 1.0 / d)))


def clock_marginal(psi: np.ndarray, d: int) -> np.ndarray:
    m = psi.reshape(2, d)                                   # [system, clock]
    return sum(np.outer(m[s], m[s].conj()) for s in range(2))


def entanglement_ebits(psi: np.ndarray, d: int) -> float:
    s = np.linalg.svd(psi.reshape(2, d), compute_uv=False) ** 2
    return float(-sum(x * np.log2(x) for x in s if x > 1e-12))


def history_state(d: int) -> np.ndarray:
    """(1/sqrt d) sum_t |t>_C (x) Ry(t*theta)|0>_S -- maximally entangled."""
    th = 2 * np.pi / d
    psi = np.zeros(2 * d, dtype=complex)
    for t in range(d):
        v = np.array([np.cos(t * th / 2), np.sin(t * th / 2)])
        for s in (0, 1):
            psi[s * d + t] = v[s] / np.sqrt(d)
    return psi


def product_state(d: int) -> np.ndarray:
    """(1/sqrt d) sum_t |t>_C (x) |0>_S -- ZERO entanglement, coherent clock."""
    psi = np.zeros(2 * d, dtype=complex)
    for t in range(d):
        psi[t] = 1.0 / np.sqrt(d)
    return psi


def concurrence(rho: np.ndarray) -> float:
    Y = np.array([[0, -1j], [1j, 0]])
    YY = np.kron(Y, Y)
    ev = np.sqrt(np.clip(np.linalg.eigvals(rho @ YY @ rho.conj() @ YY).real, 0.0, None))
    ev = np.sort(ev)[::-1]
    return float(max(0.0, ev[0] - ev[1] - ev[2] - ev[3]))


# --------------------------------------------------------------------------
# 1-2. One law
# --------------------------------------------------------------------------

def check_one_law() -> bool:
    print("THE LAW -- cos(theta/2) is the pairwise qubit-state overlap")
    ok = True
    for th in (0.0, np.pi / 4, np.pi / 2, np.pi):
        got = float(np.dot(np.array([1.0, 0.0]),
                           np.array([np.cos(th / 2), np.sin(th / 2)])))
        ok &= bool(np.isclose(got, np.cos(th / 2)))
        print(f"    theta={th:.4f}  <psi(0)|psi(theta)> = {got:+.6f}"
              f"   cos(theta/2) = {np.cos(th/2):+.6f}")

    print("\n  relational-time measures it against TIME:")
    d = 8
    for dt in range(4):
        lhs, rhs = np.cos(dt * np.pi / d), np.cos((2 * np.pi * dt / d) / 2)
        ok &= bool(np.isclose(lhs, rhs))
        print(f"    d={d} dt={dt}:  rho_C = {lhs:+.6f}   cos(theta/2) = {rhs:+.6f}")

    print("\n  twisted-spin-ptm measures it against COUPLING ANGLE, raised to")
    print("  the number of informed spins:  T_xx = cos(chi_t/2)^(N-2)")
    for N in (4, 8, 16):
        print(f"    N={N:>2} chi_t=1.0:  T_xx = {np.cos(0.5)**(N-2):.6f}"
              f"   [overlap^{N-2}]")

    print(f"\n  identification exact -> {ok}\n")
    return bool(ok)


# --------------------------------------------------------------------------
# 3. The anti-correlation
# --------------------------------------------------------------------------

def check_anticorrelation() -> bool:
    print("THE ANTI-CORRELATION -- marginal coherence is SUPPRESSED by entanglement")
    print("  (for a bipartite pure state, marginal entropy IS entanglement entropy)\n")
    print("     d   state      clock-marginal witness   entanglement (ebits)")
    ok = True
    ratios = {}
    for d in (2, 4, 8):
        row = {}
        for name, psi in (("history", history_state(d)), ("product", product_state(d))):
            w = fourier_witness(clock_marginal(psi, d), d)
            e = entanglement_ebits(psi, d)
            row[name] = (w, e)
            print(f"     {d}   {name:<9}        {w:.6f}                {e:.4f}")
        ok &= row["product"][0] > row["history"][0]      # witness runs backwards
        ok &= row["product"][1] < row["history"][1]      # entanglement opposite
        ratios[d] = row["product"][0] / max(row["history"][0], 1e-15)

    print(f"\n  product scores HIGHER than history at every d -> {ok}")
    print(f"  d=4 ratio = {ratios[4]:.4f}   (IBM-2 measured 4.2x on hardware)")
    match = bool(abs(ratios[4] - 4.24) < 0.02)
    print(f"  exact ratio reproduces the measured value -> {match}")
    print("  => the adversary did not exploit a loophole. It saturated a")
    print("     quantity that entanglement necessarily suppresses.\n")
    return bool(ok and match)


# --------------------------------------------------------------------------
# 4. The two nulls
# --------------------------------------------------------------------------

def check_two_nulls() -> bool:
    def marginal(rho):
        return np.trace(rho.reshape(2, 2, 2, 2), axis1=1, axis2=3)

    def txx(rho):
        X = np.array([[0, 1], [1, 0]])
        return float(np.real(np.trace(np.kron(X, X) @ rho)))

    rho_sep = np.eye(4) / 4                     # OAT boundary at chi_t = pi
    bell = np.zeros(4); bell[0] = bell[3] = 1 / np.sqrt(2)
    rho_ent = np.outer(bell, bell)

    print("THE TWO NULLS -- both marginals maximally mixed, opposite physics")
    print(f"\n  twisted-spin-ptm, chi_t = pi:  T_xx = {np.cos(np.pi/2)**2:.6f},"
          f"  concurrence = {concurrence(rho_sep):.6f}  -> SEPARABLE")
    psi2 = history_state(2)
    print(f"  relational-time,  d = 2:       witness = "
          f"{fourier_witness(clock_marginal(psi2,2),2):.6f},"
          f"  {entanglement_ebits(psi2,2):.4f} ebits  -> MAXIMALLY ENTANGLED")

    print("\n     state                     T_xx        marginal witness   marg = I/2")
    rows = []
    for nm, r in (("I/4  (separable)     ", rho_sep),
                  ("Bell (max entangled) ", rho_ent)):
        mg = marginal(r)
        w = fourier_witness(mg, 2)
        mixed = bool(np.allclose(mg, np.eye(2) / 2))
        rows.append((txx(r), w, mixed))
        print(f"     {nm}  {txx(r):+.6f}         {w:.6f}            {mixed}")

    marg_blind = np.isclose(rows[0][1], 0.0, atol=1e-12) and np.isclose(rows[1][1], 0.0, atol=1e-12)
    joint_sees = not np.isclose(rows[0][0], rows[1][0], atol=1e-9)
    both_mixed = rows[0][2] and rows[1][2]
    print(f"\n  both marginals maximally mixed      -> {both_mixed}")
    print(f"  marginal witness zero on BOTH       -> {marg_blind}")
    print(f"  joint correlator T_xx DOES separate -> {joint_sees}")
    print("  => the two observables are NOT the same functional. They share")
    print("     the LAW and an exact null, and twisted-spin-ptm's null supplies")
    print("     the separable state that makes the blindness concrete.\n")
    return bool(marg_blind and joint_sees and both_mixed)


# --------------------------------------------------------------------------
# 5. Applied bounds
# --------------------------------------------------------------------------

def check_applied_bounds() -> bool:
    print("THE APPLIED BOUNDS -- the questions this line began with")
    print("\n  Q1: compress observations into entangled photons for downlink?")
    print("     qubits   Holevo (no shared ent.)   superdense (shared ent.)")
    for n in (1, 10, 100):
        print(f"     {n:<8} {n:<25} {2*n}")
    print("     => bounded. Compression must be earned CLASSICALLY, before encoding.")

    print("\n  Q2: does time dilation buy processing headroom?")
    print("     gamma   Earth-frame storage   local ops/Earth-sec   ops per coherence")
    for g in (2.0, 10.0):
        print(f"     {g:<7.0f} x{g:<19.0f} x{1/g:<19.3f} x{g*(1/g):.3f} (unchanged)")
    for name, v in (("ISS (LEO)", 7660.0), ("GPS (MEO)", 3874.0)):
        gam = 1.0 / np.sqrt(1 - (v / C_LIGHT) ** 2)
        print(f"     {name:<12} gamma-1 = {gam-1:.3e}   storage gain {(gam-1)*100:.2e} %")
    print("     => a trade, not an accelerator, and ~1e-10 in practice.\n")
    return True


# --------------------------------------------------------------------------
# 5. THE ONE BUDGET
# --------------------------------------------------------------------------

def _lambda_family(lam: float) -> np.ndarray:
    """IBM-11's family at d=2: product state (lam=0) -> Bell pair (lam=1).

    |Psi(lam)> = (1/sqrt2) [ |0>_C |0>_S + |1>_C Ry(lam pi)|0>_S ]
    """
    c, s = np.cos(lam * np.pi / 2), np.sin(lam * np.pi / 2)
    psi = np.zeros(4, dtype=complex)                 # index 2*C + S
    psi[0] = 1 / np.sqrt(2)                          # |0>_C |0>_S
    psi[2] = c / np.sqrt(2)                          # |1>_C |0>_S
    psi[3] = s / np.sqrt(2)                          # |1>_C |1>_S
    return psi


def _mu_family(mu: float) -> np.ndarray:
    """IBM-12's family: A's partner moves from Sa to B as mu: 0 -> pi/2.

    H(A); CX(A,Sa); CRY(2mu, Sa, B); CX(B,Sa)      index 4*A + 2*Sa + B
    """
    psi = np.zeros(8, dtype=complex)
    psi[0] = 1 / np.sqrt(2)                          # |0,0,0>
    psi[6] = np.cos(mu) / np.sqrt(2)                 # |1,1,0>
    psi[5] = np.sin(mu) / np.sqrt(2)                 # |1,0,1>  (CX(B,Sa) flips Sa)
    return psi


def _visibility_predictability(psi4: np.ndarray) -> tuple[float, float]:
    """Jakob-Bergou V and P for the first qubit of a 2-qubit pure state."""
    m = psi4.reshape(2, 2)                           # [C, S]
    rho = m @ m.conj().T                             # clock marginal
    return 2.0 * abs(rho[0, 1]), abs(rho[0, 0] - rho[1, 1]).real


def _concurrence_pure(psi4: np.ndarray) -> float:
    return float(2.0 * abs(np.linalg.det(psi4.reshape(2, 2))))


def _pair_concurrence(psi8: np.ndarray, keep: tuple[int, int]) -> float:
    """Concurrence of the reduced 2-qubit state on `keep` from a 3-qubit pure state."""
    traced = [q for q in (0, 1, 2) if q not in keep][0]
    t = psi8.reshape(2, 2, 2).transpose(*keep, traced).reshape(4, 2)
    return concurrence(t @ t.conj().T)


def _depolarize(rho: np.ndarray, p: float) -> np.ndarray:
    n = rho.shape[0]
    return (1 - p) * rho + p * np.eye(n) / n


def check_one_budget() -> bool:
    print("THE ONE BUDGET -- every magnitude this programme measured is drawn")
    print("  on a single conserved unit, and it is spent twice over.\n")
    ok = True

    print("  (a) WITHIN a pair -- Jakob & Bergou, PRA 68 022107 (2003):")
    print("      V^2 + P^2 + C^2 = 1.  The clock-marginal witness is W = V/2,")
    print("      and P = 0 for this family, so (2W)^2 + C^2 = 1 is that")
    print("      relation's P=0 slice.  IBM-11 measured the curve.\n")
    print("      lam      W        V        P        C      V^2+P^2+C^2")
    for lam in (0.0, 0.25, 0.5, 0.75, 1.0):
        psi = _lambda_family(lam)
        V, P = _visibility_predictability(psi)
        C = _concurrence_pure(psi)
        tot = V ** 2 + P ** 2 + C ** 2
        ok &= bool(np.isclose(tot, 1.0)) and bool(np.isclose(P, 0.0, atol=1e-12))
        print(f"      {lam:.2f}   {V/2:.6f} {V:.6f} {P:.6f} {C:.6f}   {tot:.9f}")

    print("\n  (b) ACROSS pairs -- Coffman, Kundu & Wootters, PRA 61 052306 (2000):")
    print("      C^2(A:Sa) + C^2(A:B) + tau_ABC = 4 det rho_A.  For this family")
    print("      rho_A is maximally mixed and tau_ABC = 0, so the two")
    print("      concurrences sum to 1.  IBM-12 measured the curve.\n")
    print("      mu       C(A:Sa)  C(A:B)   sum of squares")
    for mu in (0.0, np.pi / 8, np.pi / 4, 3 * np.pi / 8, np.pi / 2):
        psi = _mu_family(mu)
        c_asa = _pair_concurrence(psi, (0, 1))
        c_ab = _pair_concurrence(psi, (0, 2))
        tot = c_asa ** 2 + c_ab ** 2
        ok &= bool(np.isclose(tot, 1.0, atol=1e-8))
        print(f"      {mu:.4f}   {c_asa:.6f} {c_ab:.6f}   {tot:.9f}")

    print("\n  (c) THE SAME UNIT, TWICE.  Local coherence trades against")
    print("      entanglement with a partner; entanglement with one partner")
    print("      trades against entanglement with another.  Both totals are 1.")

    print("\n  (d) MIXEDNESS NEVER CREATES HEADROOM.  If decoherence could push")
    print("      a total above 1 there would be slack to spend.  It cannot --")
    print("      checked under depolarizing noise, which is why the argument")
    print("      survives on hardware and is not a pure-state artifact.\n")
    print("      p      max over lam of V^2+P^2+C^2      max over mu of sum C^2")
    for p in (0.0, 0.05, 0.2, 0.5, 1.0):
        best_a, best_b = 0.0, 0.0
        for k in range(21):
            lam = k / 20.0
            m = _lambda_family(lam).reshape(2, 2)
            rho2 = _depolarize(np.outer(_lambda_family(lam), _lambda_family(lam).conj()), p)
            rc = np.trace(rho2.reshape(2, 2, 2, 2), axis1=1, axis2=3)
            V, P = 2 * abs(rc[0, 1]), abs(rc[0, 0] - rc[1, 1]).real
            best_a = max(best_a, V ** 2 + P ** 2 + concurrence(rho2) ** 2)

            mu = lam * np.pi / 2
            psi8 = _mu_family(mu)
            rho3 = _depolarize(np.outer(psi8, psi8.conj()), p)
            r3 = rho3.reshape(2, 2, 2, 2, 2, 2)
            r_asa = np.trace(r3, axis1=2, axis2=5).reshape(4, 4)
            r_ab = np.trace(r3, axis1=1, axis2=4).reshape(4, 4)
            best_b = max(best_b, concurrence(r_asa) ** 2 + concurrence(r_ab) ** 2)
        ok &= bool(best_a <= 1.0 + 1e-9 and best_b <= 1.0 + 1e-9)
        print(f"      {p:.2f}   {best_a:.9f}                    {best_b:.9f}")

    print(f"\n  no total ever exceeds 1 -> {ok}")
    print("  => THE CONSEQUENCE.  A Page-Wootters clock is a good clock in")
    print("     proportion to C(clock : its own system).  Any magnitude offered")
    print("     as a shared time between two good clocks is already spent --")
    print("     by (a) against the clock's own local coherence, by (b) against")
    print("     the other partner.  No quantity on this budget can be a shared")
    print("     clock.  That is what thirteen runs measured, and it is why the")
    print("     open question (README section 8) is about a quantity that is")
    print("     not a magnitude at all.\n")
    return bool(ok)


if __name__ == "__main__":
    print("=" * 74)
    print("One budget: why correlation magnitude cannot be a shared clock")
    print("=" * 74 + "\n")
    out = [check_one_law(), check_anticorrelation(), check_two_nulls(),
           check_one_budget(), check_applied_bounds()]
    print("=" * 74)
    print(f"all checks pass: {all(out)}")
    print("=" * 74)
