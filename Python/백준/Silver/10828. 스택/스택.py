n=int(input())
li=[]
for _ in range(n):
    a=input().split()
    if a[0]=='push': li.append(a[1])
    elif a[0]=='pop': print(-1) if len(li)==0 else print(li.pop())
    elif a[0]=='size': print(len(li))
    elif a[0]=='empty': print(1) if len(li)==0 else print(0)
    elif a[0]=='top': print(-1) if len(li)==0 else print(li[-1])