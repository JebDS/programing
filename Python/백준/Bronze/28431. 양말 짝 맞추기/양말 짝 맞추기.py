li=[]
for _ in range(5):
    li.append(int(input()))
li.sort()
c=10
for i in li:
    if c==10:
        c=i
    elif c==i:
        c=10
print(c)
