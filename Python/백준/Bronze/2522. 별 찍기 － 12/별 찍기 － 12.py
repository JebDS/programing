num=int(input())
for i in range(1, num+1):
    print((num-i)*' ', end='')
    print(i*'*')

for i in range(1, num):
    print(i*' ', end='')
    print((num-i)*'*')
