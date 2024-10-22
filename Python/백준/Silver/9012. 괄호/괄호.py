n=int(input())

for _ in range(n):
    li=[]
    VPS=True
    a=input()
    for i in a:
        if i=='(':
            li.append(i)
        elif i==')':
            try:
                li.pop()
            except:
                VPS=False
                break
    if len(li)!=0 or not VPS:
        print("NO")
    else: print("YES")