import sys

a=sys.stdin.readline().strip().upper()
di={}
li=[]
c=0

for i in a:
    if i in di:
        di[i]+=1
    else:
        di[i]=1
di=sorted(di.items(), key=lambda i:i[1], reverse=True) #정렬시 리스트화
try:
    if di[0][1]==di[1][1]:
        sys.stdout.write('?')
    else:
        sys.stdout.write(str(di[0][0]))
except:
    sys.stdout.write(str(di[0][0]))