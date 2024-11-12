n=int(input())

for i in range(n*5):
    if i<n or i>=n*4 or (i>=n*2 and i<n*3): print('@'*n+' '*n*3+'@'*n)
    else: print('@'*n*5)