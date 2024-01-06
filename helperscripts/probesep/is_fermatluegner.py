##### INPUT #######
n = 2737
a = {390, 2347, 2579}  # might also be called S
###################

# Constants
RED = "\033[31m"  # Red text
GREEN = "\033[32m"  # Green text
RESET = "\033[0m"  # Reset to default color
BOLD = "\033[1m"  # Bold text


def ggT(a, b):
    a_original = a
    b_original = b
    while b != 0:
        a, b = b, a % b
    print(f"ggT({a_original},{b_original}) = {BOLD}{a}{RESET}")
    if a == 1:
        print(f"{a_original} und {b_original} sind teilerfremd. {RED}MAYBE FERMAT-LÜGNER{RESET}")
    return a


def pseudo_prime(a, n):
    if pow(a, n - 1, n) == 1:
        print(f"{a}^{n-1} = 1 mod {n}")
        print(f"{a} ist {RED}Pseudo-Primzahl{RESET} von {n}, {RED}MAYBE FERMAT-LÜGNER{RESET}")
        return True
    else:
        res = pow(a, n - 1, n)
        print(f"{a}^{n-1} = {res} mod {n}")
        print(f"{a} ist {GREEN}keine{RESET} Pseudo-Primzahl von {n}")
        return False


def is_fermatluegner(n, a):

    if ggT(a, n) == 1 and pseudo_prime(a, n):
        print(f"{BOLD}{a} {RED}ist eine Fermat-Lügner Zahl{RESET}")
        return True
    else:
        print(f"{BOLD}{a} {GREEN}ist keine Fermat-Lügner Zahl{RESET}")
        return False


for a in a:
    print(f"{BOLD}a = {a}{RESET}")
    is_fermatluegner(n, a)
    print("\n")
