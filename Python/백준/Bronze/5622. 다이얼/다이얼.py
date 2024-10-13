x=input()
c=0
for i in x:
    if ord(i)<=67:
        c+=3
    elif ord(i)<=70:
        c+=4
    elif ord(i)<=73:
        c+=5
    elif ord(i)<=76:
        c+=6
    elif ord(i)<=79:
        c+=7
    elif ord(i)<=83:
        c+=8
    elif ord(i)<=86:
        c+=9
    elif ord(i)<=90:
        c+=10
print(c)