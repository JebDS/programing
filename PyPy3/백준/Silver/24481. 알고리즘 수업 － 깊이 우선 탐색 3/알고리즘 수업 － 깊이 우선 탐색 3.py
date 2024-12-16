import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

def dfs(s, li, li2):
    global c, v
    li2[s]=True
    v[s]=c
    c+=1
    for i in sorted(li[s]):
        if li2[i]==False:
            dfs(i, li, li2)
            c-=1

n,m,r=map(int, input().strip().split())

li=[[] for _ in range(n)]
v=[-1 for _ in range(n)]
c=0
for _ in range(m):
    a,b=map(int, input().strip().split())
    li[a-1].append(b-1)
    li[b-1].append(a-1)

dfs(r-1, li, [False]*n)
for i in v:
    sys.stdout.write(str(i)+'\n')