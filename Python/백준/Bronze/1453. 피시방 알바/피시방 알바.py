n=int(input())
li=list(map(int, input().split()))
dic={}
c=0
for i in range(1, 101):
    dic[i]=0

for j in li:
    if dic[j]==0:
        dic[j]=1
    else: c+=1
print(c)