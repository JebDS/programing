a=int(input())

for i in range(a):
    print(" "*i,end='')
    print("*"*(a*2-2*i-1))