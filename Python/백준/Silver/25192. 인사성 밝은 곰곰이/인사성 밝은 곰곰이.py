import sys

n=int(sys.stdin.readline().strip())
di={}
c=0
for _ in range(n):
    a=sys.stdin.readline().strip()
    if a=="ENTER":
        di=dict(zip(di.keys(), '0'))
    elif a not in di:
        di[a]='1'
        c+=1
    else:
        if di[a]=='0':
            c+=1
sys.stdout.write(str(c))