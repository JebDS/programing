n=int(input())
for _ in range(n):
    li=input().split()
    a=0
    for i in li:
        if i=='@': a*=3
        elif i=='#': a-=7
        elif i=='%':  a+=5
        else: a=float(i)
    print('{:.2f}'.format(a))