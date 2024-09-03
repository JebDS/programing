import sys

s=[]
m=int(input())

for i in range(m):
    r = sys.stdin.readline().strip().split()
    if r[0]=="add":
        if int(r[1]) not in s:
            s.append(int(r[1]))
    elif r[0]=="remove":
        if int(r[1]) in s :
            s.remove(int(r[1]))
    elif r[0]=="check":
        if int(r[1]) in s:
            sys.stdout.write(str(1)+"\n")
        else:
            sys.stdout.write(str(0)+"\n")
    elif r[0]=="toggle":
        if int(r[1]) in s :
            s.remove(int(r[1]))
        else:
            s.append(int(r[1]))
    elif r[0]=="all":
        s.clear()
        s=list(range(1,21))
    elif r[0]=="empty":
        s.clear()