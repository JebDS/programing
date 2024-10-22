a=input()

while a!='.':
    li=[]
    VPS=True
    for i in a:
        if (i=='(' or i=='['):
            li.append(i)
        if i==')':
            if len(li)==0:
                VPS=False
                break
            elif li[-1]=='(': li.pop()
            else: VPS=False; break
        elif i==']':
            if len(li)==0:
                VPS=False
                break
            elif li[-1]=='[': li.pop()
            else: VPS=False; break
    if VPS and len(li)==0: print("yes")
    else: print("no")
    a=input()