b=list(map(int, input().split()))
dx, dy=map(int, input().split())
jx, jy=map(int, input().split())

dsum=abs(jx-dx)+abs(jy-dy)
b[0], b[1] = abs(b[0]-jx), abs(b[1]-jy)
bsum=max(b)

if dsum<bsum: print("daisy")
elif bsum<dsum: print("bessie")
else: print("tie")