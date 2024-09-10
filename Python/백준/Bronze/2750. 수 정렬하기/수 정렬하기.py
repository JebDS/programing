import sys
li=[]
n=int(sys.stdin.readline())
for i in range(n):
    li.append(int(sys.stdin.readline().strip()))
li.sort()
for i in li:
    sys.stdout.write(str(i)+'\n')