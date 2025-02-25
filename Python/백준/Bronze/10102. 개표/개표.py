_=input()
a=input()
A=0; B=0
for i in a:
    if i=='A': A+=1
    else: B+=1
if A==B: print("Tie")
elif A>B: print("A")
else: print("B")