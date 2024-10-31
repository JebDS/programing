n=int(input())
di={}
for _ in range(n):
    a=input()
    if a in di:
        di[a]+=1
    else: di[a]=1
li=list(di.items())
li.sort(key=lambda i:(-i[1], i[0]))
print(li[0][0])