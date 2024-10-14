s=input()
n=len(s)
s=s.replace("pi","--")
s=s.replace("ka","--")
s=s.replace("chu","---")
if s==("-"*n):
    print("YES")
else:
    print("NO")