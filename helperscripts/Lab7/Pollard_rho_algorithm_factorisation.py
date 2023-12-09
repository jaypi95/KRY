from math import gcd

n = 59153
x0 = 24712
y0 = x0
a = 1
i = 1

while True:
    x0 = (x0**2 + a) % n
    y0 = ((y0**2 + a)**2 + a) % n
    d = gcd(abs(x0 - y0), n)

    if d > 1 and d < n:
        print("d = ", d)
        break
