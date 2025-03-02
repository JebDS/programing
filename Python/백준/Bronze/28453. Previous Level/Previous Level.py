_=input()
a=list(map(int, input().split()))
b=[]
for i in a:
    if i==300: b.append(1)
    elif i>=275: b.append(2)
    elif i>=250: b.append(3)
    else: b.append(4)
print(*b)