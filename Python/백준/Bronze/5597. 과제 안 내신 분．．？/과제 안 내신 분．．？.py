li=[]
L=[]
for i in range(28):
    li.append(int(input()))

for i in range(1, 31):
    if i not in li:
        L.append(i)
    if len(L)==2:
        break
L.sort()
print(L[0])
print(L[1])