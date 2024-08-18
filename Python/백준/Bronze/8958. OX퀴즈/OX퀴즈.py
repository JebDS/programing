a=int(input())

for i in range(a):
    b=list(input())
    combo=0
    sum=0
    for j in b:
        if j=='O':
            combo+=1
            sum+=combo
        else:
            combo=0
    print(sum)