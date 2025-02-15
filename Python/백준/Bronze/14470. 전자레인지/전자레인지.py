A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
s=0
t=True
while A!=B:
    if A<0:
        if t: s+=D; t=False
        s+=C
        A+=1
    else:
        s+=E
        A+=1
print(s)
