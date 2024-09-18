import sys

n=int(sys.stdin.readline().strip())

for _ in range(n):
    num=int(sys.stdin.readline().strip())
    di=[]
    for _ in range(num):
        name, l = sys.stdin.readline().strip().split()
        di.append([name, int(l)])
    di.sort(key=lambda i: -i[1])
    print(di[0][0])
