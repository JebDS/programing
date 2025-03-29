n=int(input())
for i in range(n):
    li=list(map(int, input().split()))
    li.sort()
    print("Case #"+str(i+1)+":", end=' ')
    if li[0]+li[1]<=li[2]: print("invalid!")
    elif (li[0]==li[1] and li[2]!=li[1])or(li[0]!=li[1] and li[2]==li[1]): print("isosceles")
    elif li[0]==li[1] and li[2]==li[1]: print("equilateral")
    else: print("scalene")