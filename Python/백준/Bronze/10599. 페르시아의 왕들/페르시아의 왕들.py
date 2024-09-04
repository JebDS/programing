while 1:
    b=[0,0]
    d=[0,0]
    b[0],b[1],d[0],d[1]=map(int, input().split())
    if b==d and b[0]==0:
        break
    b.sort()
    d.sort()

    print(abs(b[1]-d[0]), abs(b[0]-d[1]))