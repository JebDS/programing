import math
n=input()
if len(n)>=3:
    if n[-2]=='0':
        print(int(n[:-1])+int(n[-1]))
    else:
        print(int(n[:-2])+int(n[-2:]))
else: print(int(n[0])+int(n[1]))