n=int(input())

o=0
z=0
for _ in range(n):
    a=int(input())
    if a==0: z+=1
    else: o+=1
if o>z: print("Junhee is cute!")
else: print("Junhee is not cute!")