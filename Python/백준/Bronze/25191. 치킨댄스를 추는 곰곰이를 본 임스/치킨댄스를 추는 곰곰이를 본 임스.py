n=int(input())
a,b=map(int, input().split())
sum=a//2
sum+=b
if sum<=n: print(sum)
else: print(n)