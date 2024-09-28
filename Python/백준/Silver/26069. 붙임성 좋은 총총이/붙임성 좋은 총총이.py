import sys

n=int(sys.stdin.readline().strip())
di={}
for _ in range(n):
    a, b = sys.stdin.readline().strip().split()
    if a not in di:
        di[a]=0
    if b not in di:
        di[b]=0
    if di[a]==1 or di[b]==1 or a=='ChongChong' or b=='ChongChong':
        di[a]=1
        di[b]=1
li=list(di.values())
sys.stdout.write(str(li.count(1)))