t = int(input())
while t > 0:
    t-=1
    p, q = map(int, input().split())
    a = input().strip()
    if a.count(' '):
        a, b = a.split()
    else:
        b = input()
    minA = min(p,q)
    maxA = max(p,q)
    print(int(a.replace(str(maxA), str(minA))) + int(b.replace(str(maxA), str(minA))), end=' ')
    print(int(a.replace(str(minA), str(maxA))) + int(b.replace(str(minA), str(maxA))))


