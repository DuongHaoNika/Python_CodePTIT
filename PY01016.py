t = int(input())

while t > 0:
    t-= 1
    s = input()
    n = len(s)
    for i in range(0, n - 1, 2):
        c = s[i]
        k = int(s[i + 1])
        for j in range(k):
            print(c, end='')
    print()