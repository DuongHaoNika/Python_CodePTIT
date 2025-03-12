t = int(input())

ans = []

def Try(i, n):
    if len(str(i)) % 2 == 0:
        if checkTN(i) and int(i) <= int(n):
            ans.append(int(i))
    if int(i) >= int(n):
        return
    Try(i + '0', n)
    Try(i + '2', n)
    Try(i + '4', n)
    Try(i + '6', n)
    Try(i + '8', n)

def checkTN(n):
    a = str(n)
    b = a[::-1]
    return a == b

while t>0:
    t-=1
    n = int(input())

    Try('2', str(n))
    Try('4', str(n))
    Try('6', str(n))
    Try('8', str(n))
    ans.sort()
    for a in ans:
        print(a, end=' ')
    ans.clear()
    print()