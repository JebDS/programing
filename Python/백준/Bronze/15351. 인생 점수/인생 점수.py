n=int(input())
for _ in range(n):
    sum=0
    a=input()
    for i in a:
        if i!=' ':
            sum+=ord(i)-64
    print(sum) if sum!=100 else print("PERFECT LIFE")