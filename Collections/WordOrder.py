from collections import Counter
c=Counter([input() for x in range(int(input()))])
print(len(c))
print(*c.values())
