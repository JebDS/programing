import queue

def dfs(li, li2, s):
    print(N[s], end=' ')
    li2[s]=True
    for i in range(n):
        if li[s][i]==1:
            if li2[i]==False:
                dfs(li, li2, i)

def bfs(li, li2, s):
    q=queue.Queue()
    q.put(s)
    li2[s]=True
    while not q.empty():
        a=q.get()
        print(N[a], end=' ')
        for i in range(n):
            if li[a][i]==1:
                if li2[i]==False:
                    q.put(i)
                    li2[i]=True
        
    

n, m, v = map(int, input().split())
N=[i for i in range(1,n+1)]
li=[[0 for i in range(n)] for j in range(n)]

for _ in range(m):
    a,b = map(int, input().split())
    li[a-1][b-1] = 1
    li[b-1][a-1] = 1

dfs(li, [False]*n, v-1)
print()
bfs(li, [False]*n, v-1)
