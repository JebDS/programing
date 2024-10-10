li=[]
for _ in range(9):
    li+=list(map(int, input().split()))
li_sort=sorted(li, reverse=True)
key=li.index(li_sort[0])+1
print(li_sort[0])
print(key//9 if key%9==0 else key//9+1, 9 if key%9==0 else key%9)
