n, m = map(int, input().split())
li=list(map(int, input().split()))
li.sort(reverse=True)

start=0
sum=0
for _ in range(n):
    if li[start]>(m-2):
        start+=1
    else: break
for i in range(start, n):
    for j in range(i+1, n):
        for h in range(j+1, n):
            if li[i]+li[j]+li[h]<=m and sum<li[i]+li[j]+li[h]:
                sum=li[i]+li[j]+li[h]
print(sum)