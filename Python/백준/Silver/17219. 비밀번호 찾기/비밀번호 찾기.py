n, m = map(int, input().split())
di={}
for _ in range(n):
    a,b=input().split()
    di[a]=b
for _ in range(m):
    print(di[input()])