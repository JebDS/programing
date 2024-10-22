num=int(input())
for _ in range(num):
    n=int(input())
    day=1
    sum=0
    li=list(map(int, input().split()))
    for i in range(6):
        sum+=li[i]
    while n>=sum:
        day+=1
        sum*=4
    print(day)