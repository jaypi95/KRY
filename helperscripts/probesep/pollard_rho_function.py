import math

from prettytable import PrettyTable

######### INPUT #########
n = 143
x0 = 1
y0 = 1
a = 3
def f(x):
    return (x**2 + a) % n # Die Funktion f(x), falls eine funktion gegeben ist hier einsetzen
#########################

def pollard_rho(n, x, y, f):
    seen = set()
    while True:
        x = f(x)
        y = f(f(y))
        if (x, y) in seen:
            return None
        seen.add((x, y))
        d = math.gcd(abs(x - y), n)
        if d != 1 and d != n:
            return d, x, y



def find_factors(n, x, y, f):
    factors = []
    while n > 1:
        result = pollard_rho(n, x, y, f)
        if not result:
            factors.append(n)
            break
        d, x, y = result
        # checkn, ob wir diesen Faktor bereits gefunden haben
        while n % d == 0:
            n //= d
            if d not in factors:
                factors.append(d)
        x, y = x0, y0
    return factors



table = PrettyTable()
table.field_names = ["i", "xi", "yi", "gcd(xi - yi, n)"]
i = 0
x, y = x0, y0
while True:
    xi = f(x)
    yi = f(f(y))
    d = math.gcd(abs(xi - yi), n)
    table.add_row([i, xi, yi, d])
    if d != 1 and d != n:
        break
    if i > 0 and (x, y) == (xi, yi):
        break
    x, y = xi, yi
    i += 1

print("Start finding factors")
factors = find_factors(n, x, y, f)

print(table)
print("Die Faktoren von", n, "sind:", factors)
