import math

n, k = map(int, input().split())
start = pow(10, k - 1)
end = pow(10, k)
cnt = 1
for i in range(start, end):
    if math.gcd(i, n) == 1:
        print(i, end=' ')
        if cnt % 10 == 0:
            print()
        cnt+=1