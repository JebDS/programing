li=[[0 for _ in range(6)] for _ in range(6)]
E=False
for i in range(36):
    p=input()
    if p[0]=='A': s=5
    elif p[0]=='B': s=4
    elif p[0]=='C': s=3
    elif p[0]=='D': s=2
    elif p[0]=='E': s=1
    elif p[0]=='F': s=0

    if li[int(p[1])-1][s]==1: E=True
    else: li[int(p[1])-1][s]=1
    if i!=0:
        if abs(lp1-s)==2:
            if abs(lp2-int(p[1]))!=1:
                E=True
        elif abs(lp1-s)==1:
            if abs(lp2-int(p[1]))!=2:
                E=True
        else: E=True
    else:
        sp1=s
        sp2=int(p[1])
    lp1=s
    lp2=int(p[1])
    if E: break

if abs(lp2-sp2)==1:
    if abs(lp1-sp1)!=2: E=True
elif abs(lp2-sp2)==2:
    if abs(lp1-sp1)!=1: E=True
else: E=True

if E: print("Invalid")
else: print("Valid")