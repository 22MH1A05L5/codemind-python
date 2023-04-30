from math import gcd
def lcm(a, b):
    return a * b // gcd(a, b)

t = int(input())

for _ in range(t):
    n, a, b, k = map(int, input().split())
    x = (n // a) - (n // lcm(a, b))
    y = (n // b) - (n // lcm(a, b))
    z = (n // lcm(a, b)) - (x + y)
    if x + y >= k:
        print("Win")
    else:
     print("Lose")