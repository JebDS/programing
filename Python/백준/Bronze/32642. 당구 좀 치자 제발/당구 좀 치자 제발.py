_=input()
li=input().split()
a=0
sum=0
for i in li:
    if i=='1': 
        a+=1
        sum+=a
    else: 
        a-=1
        sum+=a
print(sum)