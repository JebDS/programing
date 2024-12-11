import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(s, li, li2):
    global c, v
    v[s]=c
    c+=1
    li2[s]=True
    for i in sorted(li[s], reverse=True):
        if li2[i]==False:
            dfs(i, li, li2)

n,m,r=map(int, input().strip().split())
li=[[] for _ in range(n)]
v=[0 for _ in range(n)]
for _ in range(m):
    a,b=map(int, input().strip().split())
    li[a-1].append(b-1)
    li[b-1].append(a-1)
c=1
dfs(r-1, li, [False]*n) 

for i in v:
    sys.stdout.write(str(i)+'\n')