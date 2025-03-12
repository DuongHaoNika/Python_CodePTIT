t = int(input())
while t > 0:
    t-=1
    n = input()
    check = True
    sum = 0
    for c in n:
        sum += int(c)
    if sum % 10 != 0:
        check = False
    for i in range(0, len(n) - 2):
        if abs(int(n[i]) - int(n[i+1])) != 2:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")