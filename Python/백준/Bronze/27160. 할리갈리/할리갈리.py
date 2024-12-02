di={}
n=int(input())
for _ in range(n):
    a, b = input().split()
    try:
        di[a]+=int(b)
    except: di[a]=int(b)

T=False
for i in list(di.values()):
    if i==5: T=True; break
if T: print("YES")
else: print("NO")