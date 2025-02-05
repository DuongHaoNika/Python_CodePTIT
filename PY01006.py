t = int(input())
while t > 0:
    t -= 1
    s = input()
    check = True
    for c in s:
        if c != '4' and c != '7':
            check = False
            break
    if check:
        print("YES")
    else:
        print("NO")
