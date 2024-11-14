n=int(input())
m=0
for i in range(n):
    sum=0
    I=str(i)
    for j in range(len(I)):
        sum+=int(I[j])
    if i+sum==n: m=i; break
print(m)