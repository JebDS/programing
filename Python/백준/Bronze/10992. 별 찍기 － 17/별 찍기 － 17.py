n=int(input())

for i in range(n):
    print(' '*(n-i-1), end='')
    if i==0: print('*')
    elif i==n-1: print('*'*(n*2-1))
    else: print('*'+' '*(i*2-1)+'*')