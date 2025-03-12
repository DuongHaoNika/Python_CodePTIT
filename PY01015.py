t = int(input())
while t > 0:
    t-=1
    s = input()
    check = True
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")