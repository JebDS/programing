A={}
B={}
a, b = map(int, input().split())

c=list(map(int, input().split()))
for i in c:
    A[i]=1
d=list(map(int, input().split()))
for i in d:
    B[i]=1

sum=0
for i in c:
    if i in B: sum+=1
sum2=0
for i in d:
    if i in A: sum2+=1
print(a-sum+b-sum2)
