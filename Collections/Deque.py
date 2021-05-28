from collections import deque
d=deque()
n=int(input())
for x in range(n):
    t=input().split(" ")
    if(t[0]=='append'):
        d.append(int(t[1]))
    if(t[0]=='appendleft'):
        d.appendleft(int(t[1]))
    if(t[0]=='pop'):
        d.pop()
    if(t[0]=='popleft'):
        d.popleft()
for x in d:
    print(x,end=' ')
