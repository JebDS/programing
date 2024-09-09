import sys
import math
a,b,v=map(int, sys.stdin.readline().split())
if a>=v:
    sys.stdout.write(str(1))
else:
    c=a-b
    v=math.ceil(v/c-a/c)+1
    sys.stdout.write(str(v))