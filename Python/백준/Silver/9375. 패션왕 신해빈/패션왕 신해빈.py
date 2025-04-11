import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    di={}
    for _ in range(n):
        a,b=input().strip().split()
        if b in di: di[b]+=1
        else: di[b]=1
    sum=1
    for i in di:
        sum*=di[i]+1
    sys.stdout.write(str(sum-1)+'\n')