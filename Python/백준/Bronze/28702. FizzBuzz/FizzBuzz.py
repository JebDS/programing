li=[]

for _ in range(3):
    li.append(input())

j=1
for i in range(3):
    if li[i]=="Fizz":
        while not (j%3==0 and j%5!=0):
            j+=1
    elif li[i]=="FizzBuzz":
        while not (j%3==0 and j%5==0):
            j+=1
    elif li[i]=="Buzz":
        while not (j%3!=0 and j%5==0):
            j+=1
    else: j=int(li[i])
    j+=1
if j%3==0 and j%5!=0: print("Fizz")
elif j%3==0 and j%5==0: print("FizzBuzz")
elif j%3!=0 and j%5==0: print("Buzz")
else: print(j)