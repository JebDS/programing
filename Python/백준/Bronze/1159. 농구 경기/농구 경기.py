n=int(input())
di={}
for _ in range(n):
    a=input()
    if a[0] in di:
        di[a[0]]+=1
    else: di[a[0]]=1
li=list(di.items())
li.sort(key=lambda i:-i[1])
li2=[]
for i in li:
    if i[1]>=5:
        li2.append(i[0])
    else: break
li2.sort()
if len(li2)==0: print("PREDAJA")
else:
    for i in li2:
        print(i, end='')