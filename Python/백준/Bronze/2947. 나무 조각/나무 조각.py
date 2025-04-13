li=list(map(int, input().split()))
an=[1,2,3,4,5]
while an!=li:
    for c in range(4):
        if li[c]>li[c+1]:
            li[c], li[c+1] = li[c+1], li[c]
            print(*li)