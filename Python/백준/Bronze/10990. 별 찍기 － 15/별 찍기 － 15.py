n=int(input())

for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end='')
    if i==1: print("*")
    else: print("*"+" "*((i-1)*2-1)+"*")