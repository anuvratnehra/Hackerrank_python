from collections import namedtuple
n=int(input())
marks=0
t=namedtuple('t',input().split())
for x in range(n):
    a,b,c,d=input().split()
    t1=t(a,b,c,d)
    marks+=int(t1.MARKS)
print(marks/n)
