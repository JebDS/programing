li=["Never gonna give you up",
"Never gonna let you down",
"Never gonna run around and desert you",
"Never gonna make you cry",
"Never gonna say goodbye",
"Never gonna tell a lie and hurt you",
"Never gonna stop"]
t=True
n=int(input())
for _ in range(n):
    a=input()
    if a not in li:
        t=False
if t:
    print("No")
else: print("Yes")