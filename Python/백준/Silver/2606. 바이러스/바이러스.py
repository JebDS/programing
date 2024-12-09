def dfs(s, li, li2):
    g.append(s)
    li2[s]=True
    for i in range(n):
        if li[s][i]==1 and li2[i]==False:
            dfs(i, li, li2)

n=int(input())
num=int(input())
v=[i for i in range(n)]
li=[[0 for i in range(n)] for _ in range(n)]

for _ in range(num):
    a,b=map(int, input().split())
    li[a-1][b-1]=1
    li[b-1][a-1]=1
g=[]
dfs(0, li, [False]*n)
print(len(g)-1)