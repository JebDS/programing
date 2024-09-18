import sys

n=sys.stdin.readline().strip()
di={}
li=[]
for _ in range(int(n)):
    name, t = sys.stdin.readline().strip().split()
    if t=='enter':
        di[name]=1
    else:
        di[name]=0

for i in di:
    if di[i]==1:
        li.append(i)
for j in sorted(li, reverse=True):
    sys.stdout.write(j+'\n')

