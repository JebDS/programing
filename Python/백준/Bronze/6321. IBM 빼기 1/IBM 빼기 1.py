n=int(input())
for i in range(n):
    a=input()
    print(f"String #{i+1}")
    for j in a:
        b=ord(j)+1
        if b>90:
            print(chr(b-26), end='')
        else:
            print(chr((ord(j)+1)), end='')
    print()
    print()