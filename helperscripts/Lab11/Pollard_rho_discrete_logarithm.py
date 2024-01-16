# Für Aufgaben vom Typ:
# Bestimmen Sie mit Hilfe der Pollard ρ - Methode in Z∗23 den diskreten Logarithmus log5(10).
from math import gcd

import numpy as np

# Gegebene Werte
G1 = [1, 2, 3, 4]
G2 = [5, 6, 7, 8]
G3 = [9, 10, 11, 12]
g = 6  # Generator (logarithm base)
a = 4  # Logarithm value
p = 13  # Group Order


def mod_linear_equation(a, b, p):
    solution = f"--- Modulare Lineare Gleichung ---"
    solution += f"\n{a}x = {b} (mod {p})"
    d = gcd(a, b)
    if d == 1:
        res = (pow(a, -1, p) * b) % (p)
        solution += f"\nx = {a}^(-1) * {b} (mod {p})"
    elif d > 1:
        solution += f"\nDivision durch ggt({a}, {b}) = {d} gibt:"
        a = int(a / d)
        b = int(b / d)
        n = int((p) / d)
        z = pow(a, -1, n)
        solution += f"\nz = {a}^-1 = {z} (mod {n})"
        x = []
        for k in range(d):
            xi = (z * b + k * n) % (p)
            solution += f"\nx{k} = {z} * {b} + {k * n} (mod {p}) = {xi}"
            x.append(xi)
    return x, solution

def pollard_rho_logarithm(p, g, a, G1, G2, G3):
    solution = "--- Pollard Rho für Logarithmus ---"
    r = 0
    s = 0
    xi = 1
    store = np.array([[xi, r, s]])
    not_terminating = True
    while not_terminating:
        if xi in G1:
            solution += f"\nx = {xi}, r = {r}, s = {s}, G = G1"
            solution
            xi = (xi * a) % p
            r += 1
        elif xi in G2:
            solution += f"\nx = {xi}, r = {r}, s = {s}, G = G2"
            xi = pow(xi, 2, p)
            r *= 2
            s *= 2
        elif xi in G3:
            solution += f"\nx = {xi}, r = {r}, s = {s}, G = G3"
            xi = (xi * g) % p
            s += 1
        store = np.append(store, np.array([[xi, r, s]]), axis=0)
        not_terminating = len(store[:, 0]) == len(set(store[:, 0]))
    solution += f"\nx = {xi}, r = {r}, s = {s}"

    indices = np.where(store[:, 0] == store[:, 0][len(store) - 1])
    r1 = store[indices[0][0], 1]
    s1 = store[indices[0][0], 2]
    r2 = store[indices[0][1], 1]
    s2 = store[indices[0][1], 2]
    solution += f"\n\n{a}^{r1} * {g}^{s1} = {a}^{r2} * {g}^{s2} (mod {p})"
    r1 -= r2
    s2 -= s1
    solution += f"\n{a}^{r1} = {g}^{s1} (mod {p})"
    solution += f"\n(einsetzen: {g}^x = {a})"
    solution += f"\n{g}^{r1}x = {g}^{s2} (mod {p - 1})"

    x, mlg_solution = mod_linear_equation(r1, s2, p - 1)
    solution += f"\n\n{mlg_solution}"
    for xi in x:
        if pow(g, xi, p) == a:
            solution += f"\n\nTest:{g}^{xi} = {pow(g, xi, p)} (mod {p})"
            solution += f"\nLösung ist {xi}"
            return solution


print(pollard_rho_logarithm(p, g, a, G1, G2, G3))

