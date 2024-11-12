n=int(input())
m=int(input())
p='IO'*n+'I'
plen=len(p)
s=input()

sum=0
for i in range(m-(n*2+1)+1):
    if s[i:i+plen]==p: sum+=1
print(sum)