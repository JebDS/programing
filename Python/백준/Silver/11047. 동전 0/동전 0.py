n,k = map(int, input().split())
li=[]
for _ in range(n):
    li.append(int(input()))
sum=0

for i in sorted(li, reverse=True):
    sum+= k//i
    k=k%i
    
print(sum)
