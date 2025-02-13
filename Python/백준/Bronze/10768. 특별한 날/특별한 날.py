m=int(input())
n=int(input())
if m>2: print("After")
elif m==2:
    if n<18: print("Before")
    elif n==18: print("Special")
    else: print("After")
else: print("Before")