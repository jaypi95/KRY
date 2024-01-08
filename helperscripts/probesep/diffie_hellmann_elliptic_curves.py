from sympy import Eq
from sympy.abc import x, y

###### INPUT ######
# 1. Finite field parameters
p = 107  # Primzahl für GF(103)
# 2. coefficients of the elliptic curve
a = 29
b = 32
# 3. Point P
P = (102, 61)
# 4. Secret key ka and kb
ka = 3
kb = 3

###### YOU USUALLY DON'T NEED TO CHANGE THIS ######
#Elliptic curve
E = Eq(y**2 % p, (x**3 + a*x + b) % p)
###################

###### CONSTANTS ######
RED = "\033[31m"  # Red text
GREEN = "\033[32m"  # Green text
RESET = "\033[0m"  # Reset to default color
BOLD = "\033[1m"  # Bold text
#######################

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
        m = (3 * A[0]**2 + a) * pow(2 * A[1], -1, p) % p
    else:  # Point addition
        m = (B[1] - A[1]) * pow(B[0] - A[0], -1, p) % p

    x3 = (m**2 - A[0] - B[0]) % p
    y3 = (m * (A[0] - x3) - A[1]) % p
    return (x3, y3)

# Funktion zur Berechnung von n*P auf der elliptischen Kurve
def multiply_point(P, n):
    result = P
    for _ in range(n - 1):
        result = add_points(result, P)
    return result


# Calculate public keys
A = multiply_point(P, ka)
B = multiply_point(P, kb)

# Calculate shared secret
shared_secret_A = multiply_point(B, ka)
shared_secret_B = multiply_point(A, kb)

print(f"{BOLD}Elliptic curve:{RESET} {E}")
print(f"{BOLD}Point P:{RESET} {P}")
print(f"{BOLD}Secret a:{RESET} {ka}")
print(f"{BOLD}Secret b:{RESET} {kb}")
print(f"{BOLD}Public key A (ka · P):{RESET} {A}")
print(f"{BOLD}Public key B (kb · P):{RESET} {B}")
if shared_secret_A == shared_secret_B:
    print(f"{BOLD}{GREEN}Shared secret (ka · B or kb · A): {shared_secret_A}{RESET}")
else:
    print(f"{RED}Shared secret calculation failed!{RESET}")
