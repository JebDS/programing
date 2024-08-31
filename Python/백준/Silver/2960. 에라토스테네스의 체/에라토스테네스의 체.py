n,k = map(int, input().split())
li=[i for i in range(2, n+1)]
c=1
g=True
while g:
    p=li[0]
    for i in li:
        if i%p==0:
            if c==k:
                g=False
                print(i)
                break
            li.remove(i)
            c+=1