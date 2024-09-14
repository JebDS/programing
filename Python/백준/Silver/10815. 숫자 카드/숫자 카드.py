import sys

n=int(sys.stdin.readline().strip())
nm=list(map(int, sys.stdin.readline().strip().split()))
m=int(sys.stdin.readline().strip())
mm=list(map(int, sys.stdin.readline().strip().split()))

md=dict.fromkeys(mm, 0)

for i in nm:
    try:
        md[i]+=1
    except:
        pass

for j in md:
    sys.stdout.write(str(md[j])+' ')