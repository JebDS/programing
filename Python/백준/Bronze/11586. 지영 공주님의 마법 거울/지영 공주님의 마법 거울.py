a=int(input())
li=[]
for _ in range(a):
    li.append(input())
n=int(input())
if n==1:
    for i in li:
        print(i)
elif n==2:
    for i in li:
        for j in i[-1::-1]:
            print(j, end='')
        print()
else:
    for i in reversed(li):
        print(i)
