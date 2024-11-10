n=int(input())
for i in range(n*5):
    if i<n or n*3>i>=n*2: print('@'*n*5)
    else: print('@'*n)