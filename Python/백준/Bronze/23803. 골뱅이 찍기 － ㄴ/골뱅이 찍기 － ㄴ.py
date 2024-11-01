n=int(input())
for i in range(1, (n*5)+1):
    if i > (n*4):
        print('@'*n*5)
    else: print('@'*n)