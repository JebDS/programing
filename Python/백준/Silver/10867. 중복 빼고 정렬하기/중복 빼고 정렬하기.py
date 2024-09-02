b=input()
a=list(map(int, input().split()))
a=list(set(a))
for i in sorted(a):
    print(i, end=' ')
