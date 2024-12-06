n=int(input())
if n==1: print(1)
else:
    n-=1
    a=n/6
    num=0
    while 1:
        a-=num
        if a<=0: print(num+1); break
        num+=1