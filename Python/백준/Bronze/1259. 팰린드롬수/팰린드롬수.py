num=list(input())
while num[0]!='0': 
    origin=num[:]
    num.reverse()
    if num==origin:
        print("yes")
    else:
        print("no")
    num=list(input())
