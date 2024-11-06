import sys
input=sys.stdin.readline
_=input()
a=list(map(int, input().strip().split()))
b=list(set(a))
b.sort()
di={}
j=0
for i in b:
    di[i]=j
    j+=1
for i in a:
    sys.stdout.write(str(di[i])+' ')