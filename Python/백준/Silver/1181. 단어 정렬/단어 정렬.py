b=int(input())
li=[]
for _ in range(b):
    li.append(input())
li=list(set(li))
li.sort(key=lambda i: (len(i), i))
for j in li:
    print(j)