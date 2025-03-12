import math

t = int(input())
while t > 0:
    t-=1
    s = input()
    n = int(s)
    m = int(s[::-1])
    p = math.gcd(n, m)
    if p == 1:
        print("YES")
    else:
        print("NO")

