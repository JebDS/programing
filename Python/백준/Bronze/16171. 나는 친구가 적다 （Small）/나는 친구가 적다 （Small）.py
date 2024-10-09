a=input()
n=input()
N=''
li=[str(i) for i in range(10)]
for i in a:
    if i not in li:
        N+=i
if n in N:
    print(1)
else:
    print(0)