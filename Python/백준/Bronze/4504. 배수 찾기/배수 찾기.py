n=int(input())

a=int(input())
while a!=0:
    if a%n==0: print(a,"is a multiple of",str(n)+'.')
    else: print(a,"is NOT a multiple of",str(n)+'.')
    a=int(input())