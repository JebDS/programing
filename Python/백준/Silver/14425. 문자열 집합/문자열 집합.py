import sys
input=sys.stdin.readline
n, m = map(int, input().strip().split())
di={}
for _ in range(n):
    di[input().strip()]=0

sum=0
for _ in range(m):
    if input().strip() in di: sum+=1

print(sum)