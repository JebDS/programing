import sys

n, m = map(int, sys.stdin.readline().strip().split())
adi={1:0}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a in adi:
        adi[a]+=1
    else:
        adi[a]=1

    if b in adi:
        adi[b]+=1
    else:
        adi[b]=1

for i in range(1, n+1):
    try:
        sys.stdout.write(str(adi[i])+'\n')
    except:
        sys.stdout.write(str(0)+'\n')
        