n=int(input())

for i in range(1, n+1):
    for _ in range(n-i):
        print(" ", end='')
    for j in range(1, i*2+1):
        if j%2==1: print("*", end='')
        else: print(" ", end='')
    print()