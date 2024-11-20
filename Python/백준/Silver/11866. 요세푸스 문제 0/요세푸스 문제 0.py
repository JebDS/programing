from collections import deque
n, k = map(int, input().split())
dq=deque()

for i in range(1, n+1):
    dq.append(i)
print("<", end='')
for _ in range(n-1):
    dq.rotate(-(k-1))
    print(dq.popleft(), end=', ')
print(str(dq.pop())+">")