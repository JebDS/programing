n=int(input())
for i in range(1,n+1):
   a=int(input())
   if a>4500: b="Round 1"
   elif a>1000: b="Round 2"
   elif a>25: b="Round 3"
   else: b="World Finals"
   print("Case #"+str(i)+':', b)