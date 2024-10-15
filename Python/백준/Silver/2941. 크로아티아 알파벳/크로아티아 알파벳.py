a=input()
li=["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
sum=0

for i in li:
    sum+=a.count(i)
    a=a.replace(i, "0")
a=a.replace("0", "")
print(sum+len(a))