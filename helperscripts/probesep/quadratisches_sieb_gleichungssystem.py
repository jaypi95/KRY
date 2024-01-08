"""
Für Aufgaben vom Typ:
Die Durchführung des quadratischen Siebs für n = 250 und B = 5 liefert die
folgenden Gleichungen.
14^2 = (−1) · 2 · 3^3 (mod 250)
15^2 = (−1) · 5^2 (mod 250)
16^2 = 2 · 3 (mod 250)
Stellen Sie das zugehörige Gleichungssystem auf und bestimmen Sie den Faktor von 250, den
der Algorithmus am Schluss ausgeben wird.
"""

from sympy import gcd
# Remark: ChatGPT het das greglet, ich weiss nöd so genau was do gmacht wird

################ INPUT ################
bases = [14, 15, 16]
exponents = [(1, 3, 0), (0, 0, 2), (1, 1, 0)]  # Each tuple corresponds to the exponents of 2, 3, and 5 respectively
n = 250
########################################
def factorize_via_quadratic_sieve(bases, exponents, n):
    """
    :param bases: List of tuples representing the bases on the left side of the congruences.
    :param exponents: List of tuples representing the exponent tuples on the right side of the congruences.
    :param n: The modulus we are factoring.
    :return: A nontrivial factor of n if found, otherwise None.
    """
    assert len(bases) == len(exponents), "The number of base and exponent sets must match."

    # Calculate the product of the bases
    left_product = 1
    for base in bases:
        left_product *= base

    # Calculate the product of the right-hand sides
    right_product = 1
    for exp_tuple in exponents:
        for base, exponent in zip([2, 3, 5], exp_tuple):  # for this example, we are using 2, 3, 5 as the prime bases
            right_product *= base ** exponent

    # Calculate the gcd of n and the difference of the squares
    factor = gcd(n, left_product ** 2 - right_product ** 2)

    # Check if the factor is nontrivial
    if 1 < factor < n:
        return factor
    else:
        return None


factor = factorize_via_quadratic_sieve(bases, exponents, n)
print(f"The factor of {n} is: {factor}")

