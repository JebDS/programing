import sys
_=input()
a=list(input().split())
b=dict(zip(input().split(), [0 for _ in range(len(a))]))
for i in a:
    try:
        b[i]+=1
    except:
        print(i)
        break