# -*- coding: utf-8 -*-

   
import matplotlib.pyplot as plt


def tonelli(a, p):
    for i in range(2,p):
        if pow(i, (p-1)//2, p) != 1:
            h = i
            break
    
    e1 = (p-1)//2
    e2 = p-1
    while e1%2 == 0:
        e1 = e1//2
        e2 = e2//2
        if (pow(a, e1, p) * pow(h, e2, p))%p != 1:
            e2 = e2 + (p-1)//2
    
    y = (pow(a, (e1+1)//2, p) * pow(h, e2//2, p))%p
    
    return y


# Kurvenparameter
a=1023 
b=696 
p=39509
print("Singularitätskriterium: 4*a**3+27*b**2 = ", (4*a**3+27*b**2)%p)

x = []
y = []
for i in range(0, p):
    s = (i**3 + a*i + b)%p
    if pow(s, (p-1)//2, p) == 1:
        y1 = tonelli(s, p)
        y2 = (-y1)%p
        x.append(i)
        x.append(i)
        y.append(y1)
        y.append(y2)
        

plt.plot(x, y, ".")
plt.grid()
plt.show()
