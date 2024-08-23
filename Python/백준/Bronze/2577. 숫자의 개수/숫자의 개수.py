a=int(input())
b=int(input())
c=int(input())

p=str(a*b*c)

for i in range(10):
    print(p.count(str(i)))