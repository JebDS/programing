import sys

n=sys.stdin.readline().strip()
n=sorted(n, reverse=True)
for i in n:
    sys.stdout.write(i)

