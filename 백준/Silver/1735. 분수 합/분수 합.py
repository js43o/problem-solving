import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

denominator = (b1 * b2) // math.gcd(b1, b2)
a1 *= denominator // b1
a2 *= denominator // b2
numerator = a1 + a2
gcd = math.gcd(numerator, denominator)

print((a1 + a2) // gcd, denominator // gcd)
