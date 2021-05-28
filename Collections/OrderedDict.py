from collections import OrderedDict
n=int(input())
d=OrderedDict()
for x in range(n):
    t=list(map(str,input().split()))
    e=t[-1]
    st=t[0]
    for x in range(1,len(t)-1):
        st+=" "+t[x]
    if (st in d.keys()):
        d[st]+=int(e)
    else:
        d[st]=int(e)
for x in d.keys():
    print(x,end=" ")
    print(d[x])
