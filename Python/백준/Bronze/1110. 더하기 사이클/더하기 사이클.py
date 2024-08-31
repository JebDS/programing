a=int(input())
c=0

q=a//10
w=a%10

e=(q+w)%10
sum=w*10+e
c+=1

while a!=sum:
    q=sum//10
    w=sum%10

    e=(q+w)%10
    sum=w*10+e
    c+=1
print(c)