c=0
n=int(input())
for _ in range(n):
    IN=True
    li=['0']
    a=input()
    for i in a:
        if i not in li[-1] and i in li:
            IN=False
            break
        else:
            li.append(i)
    if IN: c+=1
print(c)