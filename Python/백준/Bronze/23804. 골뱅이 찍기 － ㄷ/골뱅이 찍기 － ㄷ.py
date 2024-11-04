n=int(input())
for i in range(n*5):
    if i<n or i>=(n*4): print('@'*n*5)
    else: print('@'*n)