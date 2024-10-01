n=int(input())
li=list(map(int, input().split()))
li.sort()
m=li[-1]
sum=0
for i in li:
    sum+=(i/m)*100
print(sum/n)