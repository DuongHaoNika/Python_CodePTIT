t = int(input())

while t > 0:
    t-=1
    s = input()
    l = len(s)
    if s[l-2:l] == "86":
        print("YES")
    else:
        print("NO")