h,m,s=map(int, input().split())
d=int(input())

sum=h*3600+m*60+s+d
print((sum//3600)%24, (sum//60)%60, sum%60)