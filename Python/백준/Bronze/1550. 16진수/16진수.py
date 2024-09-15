a=input()
j=len(a)-1
sum=0
for i in a:
    try:
        sum+=int(i)*(16**j)
    except:
        sum+=((10+int(chr(ord(i)-17))))*(16**j)
    j-=1
print(sum)