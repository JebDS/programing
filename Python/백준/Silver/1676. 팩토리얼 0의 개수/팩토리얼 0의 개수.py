a=int(input())
b=1
for i in range(1, a+1):
    b*=i
h=0
for i in range(1,len(str(b))-1):
    if b%(10**i)!=0:
        break
    h+=1
print(h)