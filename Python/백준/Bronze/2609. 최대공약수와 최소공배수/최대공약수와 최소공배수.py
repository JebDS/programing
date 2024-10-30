a, b = map(int, input().split())
if a>b:
    a, b = b, a
li=[]
for i in range(1, a+1):
    if a%i==0:
        li.append(i)
for i in li:
    if b%i==0:
        c=i
print(c)
print(a//c*b)