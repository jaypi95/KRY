from sympy import symbols, Eq, solve
from sympy.abc import x, y

# Für Aufgaben vom Typ:
# Alice will mit ECDSA ein Dokument bzw. dessen Hash-Wert h(m) = 121 signieren. Sie
# verwendet dazu die elliptische Kurve E : y 2 = x3 + 8x + 102 über GF (179) und daraus
# den Punkt P = (73, 60) mit Ordnung |P | = 167. Ihr geheimer Schlüssel lautet d = 37 und
# zum Signieren wählt sie die Zufallszahl k = 94.

# Definiere die elliptische Kurve und den Körper GF(179)
p = 179  # Primzahl für GF(179)
E = Eq(y**2 % p, (x**3 + 8*x + 102) % p)  # Elliptische Kurve E: y^2 = x^3 + 8x + 102 über GF(179)

P = (73, 60)  # Punkt P = (73, 60)
d = 37  # Geheimer Schlüssel d = 37
n = 167  # Ordnung |P| = 167
h_m = 121  # Hash-Wert h(m) = 121
k = 94  # Zufallszahl k = 94

# Funktion zur Addition zweier Punkte auf der elliptischen Kurve
def add_points(A, B):
    if A == B:  # Punktverdopplung
        m = (3*A[0]**2 + 8) * pow(2*A[1], -1, p) % p
    else:  # Punktaddition
        m = (B[1] - A[1]) * pow(B[0] - A[0], -1, p) % p

    x3 = (m**2 - A[0] - B[0]) % p
    y3 = (m*(A[0] - x3) - A[1]) % p
    return (x3, y3)

# Funktion zur Berechnung von n*P auf der elliptischen Kurve
def multiply_point(P, n):
    result = P
    for _ in range(n - 1):
        result = add_points(result, P)
    return result

# Berechnung des öffentlichen Schlüssels Q = d*P
Q = multiply_point(P, d)

# Signaturerzeugung
def sign_ecdsa(h_m, k, P, d, n):
    kP = multiply_point(P, k)
    r = kP[0] % n
    if r == 0:
        return None
    s = (pow(k, -1, n) * (h_m + d * r)) % n
    if s == 0:
        return None
    return r, s

# Funktion zur Berechnung von u und v für die Signaturüberprüfung
def calculate_u_v(h_m, r, s, n):
    w = pow(s, -1, n)
    u = (h_m * w) % n
    v = (r * w) % n
    return u, v

# Erweiterte Signaturüberprüfungsfunktion mit Ausgabe von Zwischenergebnissen
def verify_ecdsa_extended(h_m, Q, P, r, s, n):
    if not (1 <= r < n and 1 <= s < n):
        return False, None, None, None
    u, v = calculate_u_v(h_m, r, s, n)
    u1P = multiply_point(P, u)
    u2Q = multiply_point(Q, v)
    a_b = add_points(u1P, u2Q)
    return a_b[0] % n == r, u, v, a_b

# Berechne Signatur und führe erweiterte Überprüfung durch
signature = sign_ecdsa(h_m, k, P, d, n)
signature_valid, u, v, a_b = verify_ecdsa_extended(h_m, Q, P, signature[0], signature[1], n)

# Ausgabe der Ergebnisse und Zwischenergebnisse
print(f"Öffentlicher Schlüssel Q: {Q}")
print(f"Signatur (r, s): {signature}")
print(f"u: {u}")
print(f"v: {v}")
print(f"(a, b): {a_b}")
print(f"Signatur ist gültig: {signature_valid}")
