b=[]

for i in range(10):
    a=int(input())
    b.append(a%42)

c=set(b)

print(len(c))
