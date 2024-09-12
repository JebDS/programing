import sys

a=int(sys.stdin.readline().strip())
d={}
for i in range(a):
    an=int(sys.stdin.readline().strip())
    if an in d:
        d[an]+=1
    else:
        d[an]=1

d=sorted(d.items(), key=lambda i:i[0])

for i in d:
    for j in range(i[1]):
        sys.stdout.write(str(i[0])+'\n')