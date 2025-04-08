a=input()
li=[]
T=False
b=[]
for i in a:
    if T:
        b.append(i)
        if i=='>':
            T=False
            li.append(''.join(b))
            b.clear()
    else: 
        if i=='<':
            T=True
            if len(b)>0:
                b.reverse()
                li.append(''.join(b))
                b.clear()
            b.append(i)
        elif i==' ':
            b.reverse()
            b.append(i)
            li.append(''.join(b))
            b.clear()
        else: 
            b.append(i)
if len(b)>0:
    b.reverse()
    li.append(''.join(b))
print(''.join(li))