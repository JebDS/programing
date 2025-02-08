li=list(input().split())
while li[0]!='#':
    if int(li[1])>17 or int(li[2])>=80: c="Senior"
    else: c="Junior"
    print(li[0], c)
    li=list(input().split())