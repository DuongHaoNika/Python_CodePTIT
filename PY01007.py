t = int(input())

while t > 0:
    t-=1
    n,x,m = map(float, input().split())
    res = 0
    while True:
        if n*pow((1 + x*0.01), res) >= m:
            break
        res+=1
    print(res)