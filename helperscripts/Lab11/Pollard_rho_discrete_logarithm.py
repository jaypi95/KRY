# Für Aufgaben vom Typ:
# Bestimmen Sie mit Hilfe der Pollard ρ - Methode in Z∗23 den diskreten Logarithmus log5(10).

# Gegebene Werte
base = 5
value = 10
mode = 23


# Hilfsfunktion zur Kategorisierung in G1, G2 oder G3
# Das muss unter Umständen je nach Aufgabenstellung angepasst werden
def kategorie(x):
    if x in range(1, 8):
        return 1
    elif x in range(8, 16):
        return 2
    else:
        return 3


# Pollard-Rho-Algorithmus für diskrete Logarithmen
def pollard_rho_von_hand(base, value, mode):
    x, a1, b1 = 1, 0, 0  # Startwerte für die Sequenz
    y, a2, b2 = 1, 0, 0  # Startwerte für die schnelle Sequenz

    while True:
        # Update x, a1, b1
        k = kategorie(x)
        if k == 1:
            x = (x * base) % mode
            a1 = (a1 + 1) % mode
        elif k == 2:
            x = (x * x) % mode
            a1 = (2 * a1) % mode
            b1 = (2 * b1) % mode
        else:
            x = (x * value) % mode
            b1 = (b1 + 1) % mode

        # Update y, a2, b2 (zwei Schritte)
        for _ in range(2):
            k = kategorie(y)
            if k == 1:
                y = (y * base) % mode
                a2 = (a2 + 1) % mode
            elif k == 2:
                y = (y * y) % mode
                a2 = (2 * a2) % mode
                b2 = (2 * b2) % mode
            else:
                y = (y * value) % mode
                b2 = (b2 + 1) % mode

        # Überprüfung auf Kollision
        if x == y:
            r = (a2 - a1) % mode
            s = (b1 - b2) % mode
            if r == 0:
                return "None"
            else:
                return (s * pow(r, -1, mode)) % mode


print(pollard_rho_von_hand(base, value, mode))
