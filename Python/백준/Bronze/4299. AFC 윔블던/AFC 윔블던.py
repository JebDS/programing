a, b=map(int, input().split())
c=(a+b)//2
d=a-c
if c+d==a and c-d==b and d>=0: print(c, d)
else: print(-1)