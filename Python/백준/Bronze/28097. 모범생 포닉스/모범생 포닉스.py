n=int(input())
li=list(map(int, input().split()))
sum=sum(li)+8*(n-1)
print(sum//24, sum%24)