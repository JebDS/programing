import sys
from collections import deque
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    T=False
    p=input().strip()
    n=int(input())
    li=input().strip()
    li=li[1:-1].split(',')
    de=deque(li)
    d=True
    s=0
    for i in p:
        if i=='R': d=not d; s+=1
        elif i=='D' and n!=0: 
            n-=1
            if d: de.popleft()
            else: de.pop()
        else: T=True; break
    if s%2==1: de.reverse()
    if T: sys.stdout.write(str("error")+'\n')
    else: sys.stdout.write('['+str(','.join(de))+']'+'\n')