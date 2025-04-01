from collections import deque
n,k=map(int, input().split())
li=deque([str(i) for i in range(1, n+1)])
s=[]
for i in range(n):
    li.rotate(-(k-1))
    s.append(li.popleft())
print('<'+', '.join(s)+'>')
