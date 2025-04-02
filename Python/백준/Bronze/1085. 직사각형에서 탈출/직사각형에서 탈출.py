x,y,w,h=map(int, input().split())
li=[x,y]
li.append(w-x)
li.append(h-y)
li.sort()
print(li[0])