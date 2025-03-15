ax, ay=map(int, input().split())
bx, by=map(int, input().split())
cx, cy=map(int, input().split())

if ax==bx: x=cx
elif ax==cx: x=bx
else: x=ax

if ay==by: y=cy
elif ay==cy: y=by
else: y=ay

print(x,y)