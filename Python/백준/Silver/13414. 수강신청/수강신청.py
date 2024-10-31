import sys
input=sys.stdin.readline
l, n = map(int, input().split())
di={}
for i in range(n):
    a=input().strip()
    di[a]=i
li=list(di.items())
li.sort(key=lambda i:i[1])
for i in range(l):
    try: sys.stdout.write(str(li[i][0])+'\n')
    except: break