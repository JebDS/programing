import math as m

N=int(input())
size=list(map(int,input().split()))
T, P = map(int, input().split())
t=0
p=0

for i in size:
    if i != 0:
        t+=m.ceil(i/T)

p=N//P
pp=N%P

print(t)
print(p, pp)
        