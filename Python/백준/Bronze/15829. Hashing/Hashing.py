l=int(input())
a=input()
sum=0
for i in range(l):
    sum+=((ord(a[i])-96)*(31**i))%1234567891
print(sum)