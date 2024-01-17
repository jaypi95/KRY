import random


##### INPUT #######
p = 167  # prime number
a = 42  # number in group Z*_p, secret key
b = 93  # This is optional, if None, it will be randomly generated
m = 123  # message
g = 53 # generator of group Z*_p, if None the smallest possible g will be calculated
###################

# Constants
RED = "\033[31m"  # Red text
GREEN = "\033[32m"  # Green text
RESET = "\033[0m"  # Reset to default color
BOLD = "\033[1m"  # Bold text


def prime_factors(n):
    factors = []
    # Überprüfen der Teilbarkeit durch 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Überprüfen der Teilbarkeit durch ungerade Zahlen
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # Wenn n eine Primzahl größer als 2 ist
    if n > 2:
        factors.append(n)
    return factors


def find_smallest_possible_generator(p):
    factors = prime_factors(p - 1)
    for g in range(2, p):
        is_generator = True
        for f in factors:
            if g ** ((p - 1) // f) % p == 1:
                is_generator = False
                print(f"{RED}{g}^2 % {f} = 1, {g} is not a generator{RESET}")
                break
        if is_generator:
            return g


def calculate_A(g, a, p):
    """Calculate A = g^a mod p"""
    return g ** a % p


def encrypt_message(g, p, A, m, b):
    if b is None:
        b = random.randint(1, p)  # not sure where upper bound should be

    B = g ** b % p
    c = (A ** b) * m % p
    return B, c


def decrypt_message(g, p, b, B, c):
    m = (B ** (p - 1 - b)) * c % p
    return m

if g is None:
    g = find_smallest_possible_generator(p)
print(f"Smallest possible g in group Z*_p: {BOLD}{GREEN}{g}{RESET}")
print(f"Public key {BOLD}{GREEN}({p}, {g}, {calculate_A(g, a, p)}){RESET}")
B, c = encrypt_message(g, p, calculate_A(g, a, p), m, b)
print(f"Encrypted message: {BOLD}{GREEN}({B}, {c}){RESET}")
