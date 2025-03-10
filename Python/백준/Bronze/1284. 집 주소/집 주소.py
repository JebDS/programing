n=input()
while n!='0':
    sum=1
    for i in n:
        if i=='1': sum+=3
        elif i=='0': sum+=5
        else: sum+=4
    print(sum)
    n=input()