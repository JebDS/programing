a,b,c,d,e,f=map(int, input().split())
T=True
for x in range(-999, 1000):
    if T:
        for y in range(-999, 1000):
            if (a*x)+(b*y)==c and (d*x)+(e*y)==f:
                print(x, y)
                T=False
                break
    else: break
