x,y=map(int, input().split())
li=[]
li.append(1000/y*x)
n=int(input())
for _ in range(n):
   x,y=map(int, input().split())
   li.append(1000/y*x)
li.sort()
print(li[0])