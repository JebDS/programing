a=int(input())
c=0
for i in range(a):
    b=input()
    if int(b[2:])<=90:
        c+=1

print(c)