from collections import defaultdict
d=defaultdict(list);
l=[]
n,m=map(int,input().split(' '))
for x in range(n):
    d[input()].append(x+1)
for x in range(m):
    l.append(input())
for x in l:
    if x in d.keys():    
        for y in d[x]:
            print(y,end=" ")
        print()
    else:
        print(-1)
