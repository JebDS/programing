for _ in range(3):
   a1, a2, a3, b1, b2, b3=map(int, input().split())
   sum=b1*3600+b2*60+b3-a1*3600-a2*60-a3
   print(sum//3600, (sum%3600)//60, sum%60)