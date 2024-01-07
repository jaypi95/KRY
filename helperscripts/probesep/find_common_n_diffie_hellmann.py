from sympy import Eq
from sympy.abc import x, y

# this script is specifically for the exercise 3 b) from the probesep
# Bestimmen Sie mit Hilfe der Angaben/Resultate aus Teilaufgabe (a) eine Zahl
# n ∈ N, die gleichzeitig n · P = Q (in E) und n · P̃ = Q̃ (in Ẽ) erfüllt.
# Hinweis: Ihr Lösungsweg sollte ohne ”Durchprobieren” auskommen. Tipp: Chinesischer
# Restsatz.


###### INPUT ######

# coefficients of the elliptic curve
a = 21
b = 36
a_schlange = 29
b_schlange = 32

# Point P
P = (96, 24)
P_schlange = (102, 61)

# Feldgrösse p (GF)
p = 103
p_schlange = 107

# Ordnung
Ordnung = 93
Ordnung_schlange = 106

# Secrets
ka = 2
kb = 2
ka_schlange = 3
kb_schlange = 3

###### CONSTANTS ######
RED = "\033[31m"  # Red text
GREEN = "\033[32m"  # Green text
RESET = "\033[0m"  # Reset to default color
BOLD = "\033[1m"  # Bold text


#######################

# Elliptic curve


# Funktion zur Addition zweier Punkte auf der elliptischen Kurve
def add_points(A, B):
    # Check if either point is the identity (point at infinity)
    if A is None:
        return B
    if B is None:
        return A

    # Handle the case where the points are inverses of each other
    if A[0] == B[0] and (A[1] != B[1] or A[1] == 0):
        return None  # This would be the point at infinity

    if A == B:  # Point doubling
        if A[1] == 0:  # This is the tangent line is vertical, so it's the point at infinity
            return None
        m = (3 * A[0] ** 2 + a) * pow(2 * A[1], -1, p) % p
    else:  # Point addition
        m = (B[1] - A[1]) * pow(B[0] - A[0], -1, p) % p

    x3 = (m ** 2 - A[0] - B[0]) % p
    y3 = (m * (A[0] - x3) - A[1]) % p
    return (x3, y3)


# Funktion zur Berechnung von n*P auf der elliptischen Kurve
def multiply_point(P, n):
    result = P
    for _ in range(n - 1):
        result = add_points(result, P)
    return result


def chinese_remainder_theorem_2_equations(a1, a2, m1, m2):
    """
    Solve the system of congruences:
    x = a1 (mod m1)
    x = a2 (mod m2)
    using the Chinese remainder theorem.
    """
    # Calculate the modular inverse of m1 and m2
    m1_inv = pow(m1, -1, m2)
    print(f"u1 = M1^-1 (mod m1) = {m1}^-1 (mod {m2}) = {m1_inv}")
    m2_inv = pow(m2, -1, m1)
    print(f"u2 = M2^-1 (mod m2) = {m2}^-1 (mod {m1}) = {m2_inv}")

    # Calculate the solution
    x = (a1 * m2 * m2_inv + a2 * m1 * m1_inv) % (m1 * m2)
    print(f"{BOLD}a1 · u1 · M1 + a2 · u2 · M2 (Mod M1 · M2) = {a1} · {m2} · {m2_inv} + {a2} · {m1} · {m1_inv} (Mod {m1} · {m2}) = {GREEN}{x} mod {m1 * m2}{RESET}")



# n ∈ N, die gleichzeitig n · P = Q (in E) und n · P̃ = Q̃ (in Ẽ) erfüllt.
# we know: key = (ka · kb) · P --> n = ka · kb
n1 = ka * kb
n2 = ka_schlange * kb_schlange

# Calculate public keys
A = multiply_point(P, ka)
B = multiply_point(P, kb)
A_schlange = multiply_point(P_schlange, ka_schlange)
B_schlange = multiply_point(P_schlange, kb_schlange)

# Calculate shared secret
shared_secret_A = multiply_point(B, ka)
shared_secret_B = multiply_point(A, kb)
shared_secret_A_schlange = multiply_point(B_schlange, ka_schlange)
shared_secret_B_schlange = multiply_point(A_schlange, kb_schlange)

assert shared_secret_A == shared_secret_B
assert shared_secret_A_schlange == shared_secret_B_schlange
print(f"{BOLD}{GREEN}Shared secret A and B: {shared_secret_A}{RESET}")
print(f"{BOLD}{GREEN}Shared secret A_schlange and B_schlange: {shared_secret_A_schlange}{RESET}")

# Calculate common n
chinese_remainder_theorem_2_equations(n1, n2, Ordnung, Ordnung_schlange)
