n=int(input())

for i in range(n):
    for j in range(n*2):
        if i%2==0: 
            if j%2==0: print("*", end=" ")
        else: 
            if j%2==0: print(" ", end="*")
    print()