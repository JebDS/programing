while 1:
    a,b=map(int, input().split())
    if a==b and a==0:
        break
    else:
        if a>b:
            print("Yes")
        else:
            print("No")