a=input()
while a!='0':
    li=[a]
    while  1:
        s=1
        if len(a)==1:
            break
        for i in a:
            s*=int(i)
        li.append(s)
        if len(str(s))==1:
            break
        a=str(s)
    print(*li)
    a=input()