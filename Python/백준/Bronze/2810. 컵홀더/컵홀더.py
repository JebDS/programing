n=int(input())
a=input()
sum=1
for i in a:
    if i=='L': sum+=0.5
    else: sum+=1
print(int(sum)) if sum<=n else print(int(sum-1))