import math
from sympy import mod_inverse

# Dieses Script ist für Aufgaben vom Typ "Lösen Sie die Gleichung 78x = 246 (mod 264)"

# Gegebene Werte
a = 78
b = 246
mode = 264

# Herausfinden ob es einen ggT gibt
ggt = math.gcd(a, mode)
if ggt > 1:
    a = a // ggt
    b = b // ggt
    mode = mode // ggt

# Berechnen der Inversen
mod_inv = mod_inverse(a, mode)

x_value = (mod_inv * b) % mode

print(f"x = {x_value}")