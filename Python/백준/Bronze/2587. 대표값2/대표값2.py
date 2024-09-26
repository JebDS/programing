li=[]
sum=0
for _ in range(5):
    a=int(input())
    sum+=a
    li.append(a)
li.sort()

print(int(sum/5))
print(li[2])

