a=int(input())

for i in range(a):
    print("*"*(i+1),end='')
    print(" "*(a*2-2*(i+1)),end='')
    print("*"*(i+1))
for i in range(a):
    print("*"*(a-i-1), end='')
    print(" "*((i+1)*2),end='')
    print("*"*(a-i-1))