t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    a.sort()
    for j in range(n - 1):
        idx1 = j + 1
        idx2 = n - 1
        x = a[j]
        while idx1 < idx2:
            if x + a[idx1] + a[idx2] == 0:
                res += 1
                idx1 += 1
                idx2 -= 1
            elif x + a[idx1] + a[idx2] < 0:
                idx1 += 1
            else:
                idx2 -= 1
    print(res)