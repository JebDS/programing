n=int(input())
sum=0
for _ in range(n):
    a,b,c=map(int, input().split())
    for i in range(1, a+1):
        for j in range(1, b+1):
            for h in range(1, c+1):
                if i%j==j%h and j%h==h%i:
                    sum+=1
    print(sum)
    sum=0
