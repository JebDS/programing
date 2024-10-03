a=input()
if a[0]=='A':
    sum=4
elif a[0]=='B':
    sum=3
elif a[0]=='C':
    sum=2
elif a[0]=='D':
    sum=1
elif a[0]=='F':
    sum=0
if a[-1]=='+':
    sum+=0.3
elif a[-1]=='-':
    sum-=0.3

print(float(sum))