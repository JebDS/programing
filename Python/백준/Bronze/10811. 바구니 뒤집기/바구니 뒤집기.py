n, m=map(int, input().split())
li=[int(i) for i in range(1, n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    li2=li[a-1:b]
    li2.reverse()
    li[a-1:b]=li2

for i in li:
    print(i, end=' ')
