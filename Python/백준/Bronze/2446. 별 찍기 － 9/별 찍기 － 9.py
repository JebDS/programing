a=int(input())

for i in range(a-1):
    print(" "*i,end='')
    print("*"*(a*2-2*i-1))
for i in range(a):
    print(" "*(a-i-1), end='')
    print("*"*(i*2+1))