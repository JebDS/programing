r,c,n=map(int, input().split())

if r%n!=0:R=r//n+1
else: R=r//n
if c%n!=0: C=c//n+1
else: C=c//n
print(R*C)