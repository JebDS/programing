import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    di={}
    _=input()
    a=list(map(int, input().strip().split()))
    for i in a:
        di[i]=1
    _=input()
    a=list(map(int, input().strip().split()))
    for i in a:
        if i in di: sys.stdout.write(str(1)+'\n')
        else: sys.stdout.write(str(0)+'\n')