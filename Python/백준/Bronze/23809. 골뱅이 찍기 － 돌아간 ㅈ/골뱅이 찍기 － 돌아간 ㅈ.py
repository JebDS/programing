n=int(input())

for i in range(1, n*5+1):
    if i<=n or i>n*4: 
        print('@'*n+' '*n*3+'@'*n)
    elif i>n*2 and i<=n*3:
        print('@'*n*3)
    else: print('@'*n+' '*n*2+'@'*n)
    
    