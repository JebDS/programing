n=int(input())
a=input().split()
s=[]
sum=1
for i in range(n-1):
    if a[i]==a[i+1]: sum+=1
    else: s.append(sum); sum=1
s.append(sum)
if len(s)==0 or len(s)==1: print(n)
else:
    sum=0
    for i in range(len(s)-1):
        if s[i]+s[i+1]>sum: sum=s[i]+s[i+1]
    print(sum)