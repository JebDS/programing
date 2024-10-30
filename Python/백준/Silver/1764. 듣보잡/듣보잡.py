import sys
input=sys.stdin.readline
n, m = map(int, input().split())
di={}
for _ in range(n):
    a=input().strip()
    di[a]=0
li=[]
for _ in range(m):
    a=input().strip()
    if a in di:
        li.append(a)
print(len(li))
li.sort()
for i in li:
    sys.stdout.write(str(i)+'\n')