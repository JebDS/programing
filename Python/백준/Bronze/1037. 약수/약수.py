import sys

a=int(sys.stdin.readline().strip())
b=list(map(int, sys.stdin.readline().strip().split()))

if len(b)==1:
    sys.stdout.write(str(b[0]**2))
else:
    b.sort()
    sys.stdout.write(str(b[0]*b[-1]))