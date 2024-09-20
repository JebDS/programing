n, m = map(int, input().split())
di={}

for i in range(1, n+1):
    di[i]=i

for _ in range(m):
    a,b=map(int, input().split())
    t=di[a]
    di[a]=di[b]
    di[b]=t

for i in di.values():
    print(i,end=' ')