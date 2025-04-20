b,n=map(int, input().split())
while n!=0 and b!=0:
    i=1
    while i**n<=b:
        i+=1
    if i**n-b>b-(i-1)**n: print(i-1)
    else: print(i)
    b,n=map(int, input().split())