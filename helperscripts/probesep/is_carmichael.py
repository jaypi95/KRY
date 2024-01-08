import math

####### INPUT #######
n = 2737
#####################

# Constants
RED = "\033[31m"  # Red text
GREEN = "\033[32m"  # Green text
RESET = "\033[0m"  # Reset to default color
BOLD = "\033[1m"  # Bold text

def is_carmichael(n):
    if is_quadratfrei(n) and teiler_von_n_minus_1(n):
        print(f"{BOLD}{n} {GREEN}ist eine Carmichael Zahl{RESET}")
        return True
    else:
        print(f"{BOLD}{n} {RED}ist keine Carmichael Zahl{RESET}")
        return False
def teiler_von_n_minus_1(n):
    sind_teiler = True
    prime_factor_list = prime_factors(n)
    n = n - 1
    for p in prime_factor_list:
        p = p - 1
        if n % p != 0:
            print(f"{p} ist {RED}kein{RESET} Teiler von {n}")
            sind_teiler = False
        else:
            print(f"{p} {GREEN}ist{RESET} Teiler von {n}")
    return sind_teiler

def is_quadratfrei(n):
    original_n = n
    if n % 2 == 0:
        n = n // 2
        if n % 2 == 0:
            print(f"{n} ist {RED}nicht{RESET} Quadratfrei")
            return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            n = n // i
            if n % i == 0:
                print(f"{n} ist {RED}nicht{RESET} Quadratfrei")
                return False
    print(f"{original_n} {GREEN}ist{RESET} Quadratfrei")
    return True

def prime_factors(n):
    """Returns the prime factors of n as a list."""
    if n == 1:
        return []
    for p in range(2, int(n**0.5)+1):
        if n % p == 0:
            return [p] + prime_factors(n//p)
    return [n]

print(f"Prime factors of n: {GREEN}{prime_factors(n)}{RESET}")
is_carmichael(n)