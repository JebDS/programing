import sys
input=sys.stdin.readline
n=int(input().strip())
di={}
a=input().strip().split()
for i in a:
    di[i]=0
for _ in range(n):
    a=input().strip().split()
    for i in a:
        di[i]+=1

di=list(di.items())
di.sort(key=lambda i: (-i[1], i[0]))

for i in di:
    sys.stdout.write(str(i[0])+' '+str(i[1])+'\n')