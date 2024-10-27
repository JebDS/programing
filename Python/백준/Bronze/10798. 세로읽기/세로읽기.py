li=[]

for _ in range(5):
    li.append(list(input()))
li2=sorted(li, key=len, reverse=True)

for i in range(len(li2[0])):
    for j in range(5):
        if len(li[j])<=i:
            pass
        else: print(li[j][i], end='')