n, m = map(int, input().split())
li=[]
li2=[]
for _ in range(n):
    li.append(list(map(int, input().split())))
for _ in range(n):
    li2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(li[i][j]+li2[i][j], end=' ')
    print()