from collections import Counter
total=0
n=int(input())
l=list(map(int,input().split(" ")))
l=Counter(l)
m=int(input())
for x in range(m):
    l1=list(map(int,input().split(" ")))
    if (l1[0] in l):
        if(l[l1[0]]>0):
            total+=l1[1]
            l[l1[0]]-=1;
print(total)
