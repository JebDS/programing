_=int(input())
dic={}

a=input().split()
for i in a:
    dic[i]=1

_=int(input())
b=input().split()
for i in b:
    try: print(dic[i])
    except: print(0)