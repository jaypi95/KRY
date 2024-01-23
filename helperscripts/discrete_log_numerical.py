# Berechnung der fehlenden diskreten Logarithmen zur Basis 2 und 3 in Z_11*

# Basiswerte für die Berechnungen
bases = [2, 3]
modulus = 11


# Funktion zur Berechnung des diskreten Logarithmus
def discrete_log(base, modulus):
    # Ergebnis-Dictionary initialisieren
    log_results = {}
    # Durchlaufe alle möglichen Exponenten
    for exponent in range(1, modulus):
        # Berechne die Potenz base^exponent mod modulus
        result = pow(base, exponent, modulus)
        # Wenn das Ergebnis bereits im Dictionary ist, überspringen (da wir den kleinsten Exponenten wollen)
        if result not in log_results:
            log_results[result] = exponent
    return log_results


# Berechne die diskreten Logarithmen für die gegebenen Basen und Modulus
for base in bases:
    print(f"Logs for base {base}: {discrete_log(base, modulus)}")
