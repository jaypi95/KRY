from math import floor

"""
Für Aufgaben vom Typ:
Gegeben ist die elliptische Kurve E: y^2 = x^3 + 8x + 102 GF(179)
Codieren Sie die Klartextnachricht m = 10 mit hilfe eines 4-Bit-Shifts als Punkt M = (x,y) Element E mit kleinstmöglicher x-Komponente.
"""
##### INPUT #######
m = 10
a = 8
b = 102
p = 179
bit = 4
###################

# Constants
RED = "\033[31m"  # Red text
GREEN = "\033[32m"  # Green text
RESET = "\033[0m"  # Reset to default color
BOLD = "\033[1m"  # Bold text


def message_to_point(m, a, b, p, bit):
    solution = f"Nachricht {m} auf Punkt der Elliptischen Kurve x^3 + {a}x + {b} mit Bitshift von {bit} bringen."
    x = pow(2, bit) * m
    while x <= p:
        solution += f"\nx = {pow(2, bit)} * {m} = {x}"
        s = (pow(x, 3) + a * x + b) % p
        solution += f"\ns = {x}^3 + {a}{x} + {b} mod {p} = {s}"
        solution += f"\nQuadratischer Rest modulo p checken:\n{s}^(({p}-1) / 2) = {pow(s, floor((p - 1) / 2), p)} (mod {p})"
        if pow(s, (p - 1) // 2, p) == 1:
            solution += f"\n{GREEN}Ist quadratischer rest.{RESET}"
            for y in range(2, p):
                if y * y % p == s:
                    solution += f"\n{GREEN}Y gefunden als {y}{RESET}"
                    solution += f"\n{GREEN}{BOLD}M = ({x}, {y}){RESET}"
                    return solution, (x, y)
        x += 1
    return "leider keinen Punkt gefunden"


def point_to_message(x, y, bit):
    solution = f"\nPunkt ({x}, {y}) auf Nachricht mit Bitshift {bit} bringen."
    m = x // pow(2, bit)
    solution += f"\n{GREEN}{BOLD}m = {x} / {pow(2, bit)} = {m}{RESET}"
    return solution


M, (x, y) = message_to_point(m, a, b, p, bit)
x, y = (x, y)
print(M)
print(point_to_message(x,y, bit))
