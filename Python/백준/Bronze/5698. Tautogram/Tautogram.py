a=input().upper().split()
while a[0]!='*':
    t=a[0][0]
    x=False
    for i in a:
        if t!=i[0]: x=True; break
    print('N') if x else print('Y')
    a=input().upper().split()