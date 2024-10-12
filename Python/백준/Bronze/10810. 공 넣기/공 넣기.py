n, m = map(int, input().split())
x=[0 for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    for i in range(a-1, b):
        x[i]=c
for j in x:
    print(j, end=' ')