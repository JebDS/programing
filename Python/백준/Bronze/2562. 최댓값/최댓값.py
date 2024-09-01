li=[]
for _ in range(9):
    li.append(int(input()))
li2=sorted(li)
print(li2[-1])
print(li.index(li2[-1])+1)
