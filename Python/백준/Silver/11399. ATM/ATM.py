n = int(input())
li=list(map(int, input().split()))
li.sort()
sum=0
for i in li:
    sum+=i*n
    n-=1
print(sum)