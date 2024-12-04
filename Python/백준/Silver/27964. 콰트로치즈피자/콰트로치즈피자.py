_=input()
di={}
li=input().split()

for i in li:
    if "Cheese" == i[-6:]:
        if i in di: di[i]+=1
        else: di[i]=1
if len(di) >=4: print("yummy")
else: print("sad")