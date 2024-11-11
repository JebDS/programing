n, m = map(int, input().split())
x=[]
for _ in range(n):
    x.append(input())
Lsum=m*n

for a in range(n-7):
    for b in range(m-7):
        for i in range(2):
            sum=0
            for j in range(8):
                for h in range(8):
                    if i==0:
                        if (j%2==1 and h%2==1) or (j%2==0 and h%2==0):
                            if x[j+a][h+b]=='B': sum+=1
                        else: 
                            if x[j+a][h+b]=='W': sum+=1
                    else:
                        if (j%2==1 and h%2==1) or (j%2==0 and h%2==0):
                            if x[j+a][h+b]!='B': sum+=1
                        else: 
                            if x[j+a][h+b]!='W': sum+=1
            if sum<Lsum: Lsum=sum
print(Lsum)