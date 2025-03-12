import re

s = input()

up = len(re.findall(r'[A-Z]', s))
down = len(re.findall(r'[a-z]', s))
if up > down:
    print(s.upper())
else:
    print(s.lower())