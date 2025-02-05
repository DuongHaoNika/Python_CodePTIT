s = input()

a = s.split()

m = int(a[0])
n = int(a[2])
p = int(a[4])

if m + n == p:
    print("YES")
else:
    print("NO")