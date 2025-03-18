e,f,c=map(int, input().split())
n=e+f
sum=0
while n//c>0:
    a=n//c
    sum+=a
    n-=a*c
    n+=a
print(sum)
