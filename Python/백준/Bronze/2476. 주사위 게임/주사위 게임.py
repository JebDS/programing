n = int(input())
sum=0
li=[]
for _ in range(n):
    a,b,c=map(int, input().split())
    if a==b and b==c and a==c: sum+=10000+c*1000
    elif a==b or b==c: sum+=1000+b*100
    elif a==c: sum+=1000+100*c
    else: sum+=max(a,b,c)*100
    li.append(sum)
    sum=0
li.sort(reverse=True)
print(li[0])