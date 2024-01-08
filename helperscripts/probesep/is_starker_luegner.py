##### INPUT #######
n = 2737
a = {390, 2347, 2579}  # might also be called S
###################

# Constants
RED = "\033[31m"  # Red text
GREEN = "\033[32m"  # Green text
RESET = "\033[0m"  # Reset to default color
BOLD = "\033[1m"  # Bold text


def find_r_and_u(n):
    r = 0
    u = n - 1

    if n % 2 == 0 or n < 2:
        print(f"{RED} input ist gerade oder kleiner als 2{RESET}")
        return 0, 0

    while u % 2 == 0:
        u = u // 2
        r += 1
    print(f"n-1 = {n - 1} = 2^{r}*{u}")
    print(f"r = {r}, u = {u}")
    print("\n")
    return r, u


def kriterium_1(a, n, u):
    if pow(a, u, n) == 1:
        print(f"{a}^{u} = 1 mod {n}")
        print(f"{RED}{a} erfüllt Kriterium 1{RESET}")
        return True
    else:
        res = pow(a, u, n)
        print(f"{a}^{u} = {res} mod {n}")
        print(f"{GREEN}{a} erfüllt Kriterium 1 nicht{RESET}")

        return False


def kriterium_2(a, n, r, u):
    for i in range(0, r):
        if pow(a, 2 ** i * u, n) == n - 1:
            print(f"{a}^{2 ** i * u} = -1 mod {n}")
            print(f"{RED}{a} erfüllt Kriterium 2{RESET}")
            return True
    print(f"{a}^2 ** k * {u} gibt für kein k -1 mod {n}")
    print(f"{GREEN}{a} erfüllt Kriterium 2 nicht{RESET}")
    return False


r, u = find_r_and_u(n)
for element in a:
    print(f"{BOLD}a = {element}{RESET}")
    kriterium1 = kriterium_1(element, n, u)
    kriterium2 = kriterium_2(element, n, r, u)
    if kriterium1 or kriterium2:
        print(f"{BOLD}{element} {RED}ist ein starker Lügner{RESET}")
    else:
        print(f"{BOLD}{element} {GREEN}ist kein starker Lügner{RESET}")
    print("\n")
