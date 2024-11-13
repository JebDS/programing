sum=0
for i in range(8):
    a=input()
    if i%2==0:
        for j in range(0, 8, 2):
            if a[j]=='F': sum+=1
    else:
        for j in range(1,8,2):
            if a[j]=='F': sum+=1
print(sum)