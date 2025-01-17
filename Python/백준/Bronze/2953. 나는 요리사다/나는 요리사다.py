B=0
for i in range(5):
    a=list(map(int,input().split()))
    A=sum(a)
    if A>B:
        B=A
        b=i+1
print(b,B)