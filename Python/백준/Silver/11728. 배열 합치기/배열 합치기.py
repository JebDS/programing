import sys

_=sys.stdin.readline()
num=[]
num+=list(map(int, sys.stdin.readline().strip().split()))
num+=list(map(int, sys.stdin.readline().strip().split()))
num.sort()
for i in num:
    sys.stdout.write(str(i)+' ')
