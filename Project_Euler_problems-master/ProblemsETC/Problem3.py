from math import sqrt

divisor = 2
factors = []
n = 600851475143

while divisor <= sqrt(n):
    if n%divisor == 0:
        factors.append(divisor)
        n = n/divisor
    else:
        divisor+=1

factors.append(int(n))

print(max(factors))