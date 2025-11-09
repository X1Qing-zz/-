def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

p, q = 1009, 3643
phi = (p-1) * (q-1)
total = 0
e = 3
while e < phi:
    if gcd(e, phi) == 1 and gcd(e-1, p-1) == 2 and gcd(e-1, q-1) == 2:
        total += e
    e += 2
print("The sum of e is", total)