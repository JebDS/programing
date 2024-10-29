n=int(input())
li=[]
for _ in range(100):
    li.append([0 for _ in range(100)])
sum=0
for _ in range(n):
    a,b=map(int, input().split())
    for i in range(10):
        for j in range(10):
            li[a+i][b+j]=1
for i in li:
    sum+=i.count(1)
print(sum)