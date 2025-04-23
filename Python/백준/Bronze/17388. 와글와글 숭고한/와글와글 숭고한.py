li=list(map(int, input().split()))
if sum(li)>=100: print("OK")
else:
    if li[0]<li[1] and li[0]<li[2]: print("Soongsil")
    elif li[1]<li[0] and li[1]<li[2]: print("Korea")
    else: print("Hanyang")