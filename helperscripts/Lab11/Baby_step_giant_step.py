import math
p = 61 # Gruppenordnung
g = 17 # Erzeuger der Gruppe G (Wenn in der Aufgabe z.B log17(x) vorkommt ist g=17)
m = math.ceil(math.sqrt(p))
#h = g ** (-m) # H ist entweder diese Formel, oder der Wert dessen Logarithmus gesucht ist
h = 42 # Wenn in der Aufgabe z.B logx(42) vorkommt ist h=42

baby_steps = []
giant_steps = []

for j in range(0, m):
    # Berechne (j, g'j) in der Gruppe G
    baby_steps.append((g**j) % p)

g_inv_m = pow(g, -m, p)

for i in range(0, math.ceil(p/m)):
    # Berechne (i, ah^i) in der Gruppe G
    giant_step = (h * pow(g_inv_m, i, p)) % p
    # Prüfe ob es (aus den Baby Steps) ein j gibt mit g^j = ah^i
    if giant_step in baby_steps:
        # Berechne g^j = ah^i
        j = baby_steps.index(giant_step)
        # Berechne x = i*m + j
        x = i * m + j
        print("x = ", x)
        break


