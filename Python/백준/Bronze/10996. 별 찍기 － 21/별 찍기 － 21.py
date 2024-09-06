a=int(input())

for j in range(a*2):
    if j%2==0:
        for i in range(1,a+1): #가로
            if i%2==1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    else:
        for i in range(1,a+1): #가로
            if i%2==0:
                print("*", end="")
            else:
                print(" ", end="")
        print()
