from sympy.ntheory.residue_ntheory import discrete_log

# Für Aufgaben vom Typ:
# Bestimmen Sie in Z∗23 den diskreten Logarithmus log5(10).
# Diese Methode wählt automatisch einen passenden Algorithmus aus der Liste Trial multiplication, Baby-Step-Giant-Step, Pollard-Rho und Pohlig-Hellman aus.

# Gegebene Werte
base = 5
value = 10
mode = 23

log_value = discrete_log(mode, value, base)

print(f"Discrete logarithm: {log_value}")
