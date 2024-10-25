n=int(input())
li=[]
for i in range(n):
    a, b = input().split()
    li.append([int(a), b, i])
li.sort(key=lambda a: (a[0], a[2]))
for i in li:
    print(i[0], i[1])
