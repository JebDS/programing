a=input()
a=a[:5]
n=input()
c=0
for _ in range(int(n)):
    b=input()
    if b[:5]==a: c+=1
print(c)