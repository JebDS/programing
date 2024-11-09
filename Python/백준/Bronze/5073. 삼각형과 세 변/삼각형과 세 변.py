li=list(map(int, input().split()))
while not (li[0]==li[1] and li[1]==li[2] and li[0]==0):
    li.sort()
    if li[2]>=li[1]+li[0]: print("Invalid")
    elif li[0]==li[1] and li[1]==li[2]: print("Equilateral")
    elif li[0]==li[1] or li[1]==li[2]: print("Isosceles")
    else: print("Scalene")
    li=list(map(int, input().split()))