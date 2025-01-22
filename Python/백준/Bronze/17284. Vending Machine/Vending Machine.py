a=list(map(int, input().split()))
c=0
for i in a:
    if i==1: c+=500
    elif i==2: c+=800
    else: c+=1000
print(5000-c)