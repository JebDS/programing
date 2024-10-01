sum=0
A=0
for _ in range(20):
    _, a, b = input().split()
    if b!='P':
        if b[0]=='A':
            B=4
        elif b[0]=='B':
            B=3
        elif b[0]=='C':
            B=2    
        elif b[0]=='D':
            B=1
        else:
            B=0
        if b[-1]=='+':
            B+=0.5
        A+=float(a)
        sum+=float(a)*B
print(sum/A)