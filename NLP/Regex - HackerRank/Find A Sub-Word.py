import re

n = int(input())
text = "\n".join(input() for _ in range(n))
q = int(input())
for _ in range(q):
    print(len(re.findall(r'[a-zA-Z0-9_]%s[a-zA-Z0-9_]' % input().strip(), text)))
