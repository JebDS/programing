from collections import deque as dq
import sys
input=sys.stdin.readline

n=int(input())
myQ=dq()
for _ in range(n):
    a=list(input().strip().split())
    if a[0]=="push": myQ.append(int(a[1]))
    elif a[0]=="pop":
        if len(myQ)!=0: sys.stdout.write(str(myQ.popleft())+'\n') 
        else: sys.stdout.write(str(-1)+'\n')
    elif a[0]=="size": sys.stdout.write(str(len(myQ))+'\n')
    elif a[0]=="empty":
        if len(myQ)==0: sys.stdout.write(str(1)+'\n')
        else: sys.stdout.write(str(0)+'\n')
    elif a[0]=="front": 
        if len(myQ)==0: sys.stdout.write(str(-1)+'\n')
        else: sys.stdout.write(str(myQ[0])+'\n')
    elif a[0]=="back":
        if len(myQ)==0: sys.stdout.write(str(-1)+'\n')
        else: sys.stdout.write(str(myQ[-1])+'\n')