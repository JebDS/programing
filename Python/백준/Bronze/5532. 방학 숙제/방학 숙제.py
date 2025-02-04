L=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())

a=A//C
b=B//D

if A%C!=0:a+=1
if B%D!=0:b+=1

if a>b: print(L-a)
else: print(L-b)