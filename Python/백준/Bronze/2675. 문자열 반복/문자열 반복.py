a=int(input())

for i in range(a):
    r, s = map(str, input().split())
    for j in s:
        print(j*int(r), end='')
    print()