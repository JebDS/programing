a=int(input())
b=[]
for i in range(a):
    b.append(list(map(int, input().split())))

b.sort(key=lambda i: (i[0], i[1]))

for i in b:
    print(i[0], i[1])