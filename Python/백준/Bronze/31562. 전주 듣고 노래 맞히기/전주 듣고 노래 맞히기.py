n,m=map(int, input().split())
b={}
for _ in range(n):
    a=input().split()
    s=''.join(a[-7:-4])
    if s in b:
        li=[]
        li.append(b.get(s))
        li.append(a[1])
        b[s]=li
    else: b[s]=a[1]
    
for _ in range(m):
    s=''.join(input().split())
    if s not in b: print('!')
    elif type(b[s])==list: print('?')
    else: print(b[s])
