import sys
input=sys.stdin.readline
print=sys.stdout.write
n=int(input().strip())
li=[]
for _ in range(n):
    a=input().strip()
    if len(a)>1:
        li.append(a[2:])
    elif a=='2':
        if len(li)>=1:
            print(str(li.pop())+'\n')
        else:
            print(str(-1)+'\n')
    elif a=='3': print(str(len(li))+'\n')
    elif a=='4': print(str(1)+'\n') if len(li)==0 else print(str(0)+'\n')
    elif a=='5': print(str(li[-1])+'\n') if len(li)>=1 else print(str(-1)+'\n')