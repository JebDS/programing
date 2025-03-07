a=input().lower()
while a!='#':
    sum=0
    sum+=a.count('a')
    sum+=a.count('e')
    sum+=a.count('i')
    sum+=a.count('o')
    sum+=a.count('u')
    print(sum)
    a=input().lower()