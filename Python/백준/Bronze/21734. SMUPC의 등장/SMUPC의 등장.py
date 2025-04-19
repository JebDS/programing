s=input()
for i in s:
    n=int(ord(i))
    sum=n//100+(n%100)//10+n%10
    print(i*sum)