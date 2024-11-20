t=int(input())
for _ in range(t):
    h,w,n = map(int, input().split())
    yy=n%h
    if yy==0: yy=h

    y=n//h
    if n%h==0: y-=1
    x=y+1

    print(str(yy)+str(x).zfill(2))