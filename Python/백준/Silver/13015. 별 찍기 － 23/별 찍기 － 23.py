n=int(input())

for i in range(n):
    print(' '*i, end='')
    if i==0:
        print('*'*n+' '*(1+2*(n-2))+'*'*n)
    elif i==(n-1):
        print('*'+' '*(n-2)+'*'+' '*(n-2)+'*')
    else:
        print('*'+' '*(n-2)+'*'+' '*(1+2*(n-2-i))+'*'+' '*(n-2)+'*')
for j in range(0, n-1):
    print(' '*(n-j-2), end='')
    if j==(n-2):
        print('*'*n+' '*(1+2*(n-2))+'*'*n)
    else:
        print('*'+' '*(n-2)+'*'+' '*(1+(2*j))+'*'+' '*(n-2)+'*')