a=input()
li=[]
for i in range(len(a)):
    if a[i].isupper():
        li.append(a[i].lower())
    else:
        li.append(a[i].upper())
for i in li:
    print(i,end='')
