from math import floor

m = 1101
a = 4
b = 8
p = 23677
bit = 4


def message_to_point(m, a, b, p, bit):
    solution = f"Nachricht {m} auf Punkt der Elliptischen Kurve x^3 + {a}x + {b} mit Bitshift von {bit} bringen."
    j = 0
    while (j <= pow(2, bit) - 1):
        solution += f"\n\n--- j = {j} ---"
        x = pow(2, bit) * m - j
        solution += f"\nx = {pow(2, bit)} * {m} - {j} = {x}"
        if x > p: return "leider keinen Punkt gefunden"
        s = (pow(x, 3) + a * x + b) % p
        solution += f"\ns = {x}^3 + {a}{x} + {b} mod {p} = {s}"
        solution += f"\nQuadratischer Rest modulo p checken:\n{s}^(({p}-1) / 2) = {pow(s, floor((p - 1) / 2), p)} (mod {p})"
        if pow(s, floor((p - 1) / 2), p) == 1:
            solution += f"\nIst quadratischer rest."
            for y in range(2, p):
                if y * y % p == s:
                    solution += f"\nY gefunden als {y}"
                    solution += f"\nM = ({x}, {y})"
                    return solution
        j += 1
    return "leider keinen Punkt gefunden"


print(message_to_point(m, a, b, p, bit))
