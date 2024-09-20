def Rev(x):
    x=list(x)
    x.reverse()
    return int(''.join(x))

x,y=input().split()
print(Rev(str(Rev(x)+Rev(y))))