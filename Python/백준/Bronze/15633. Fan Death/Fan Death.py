n=int(input())
sum=1
for i in range(2, n+1):
   if n%i==0: sum+=i
print(sum*5-24)