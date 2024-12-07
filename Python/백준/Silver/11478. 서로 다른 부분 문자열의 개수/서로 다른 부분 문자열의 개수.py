a=input()
li=[]
for i in range(1, len(a)+1):
    for j in range(len(a)-i+1):
        li.append(a[j:j+i])
li2=set(li)
print(len(li2))