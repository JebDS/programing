n=int(input())
m=8+7*(n-1)
y=2024+m//12
if m%12==0:
    m=12
    y-=1
else: m%=12
print(y, m)