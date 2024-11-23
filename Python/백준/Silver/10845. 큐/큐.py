import queue
import sys
input=sys.stdin.readline

n=int(input())
q=queue.Queue()

for _ in range(n):
    a=input().strip().split()
    if a[0]=="push": q.put(int(a[1]))
    elif a[0]=="pop": 
        if q.qsize()>0: sys.stdout.write(str(q.get())+'\n')
        else: sys.stdout.write(str(-1)+'\n')
    elif a[0]=="size": sys.stdout.write(str(q.qsize())+'\n')
    elif a[0]=="empty": sys.stdout.write(str(q.empty()*1)+'\n')
    elif a[0]=="front": 
        if q.qsize()>0: sys.stdout.write(str(q.queue[0])+'\n')
        else: sys.stdout.write(str(-1)+'\n')
    elif a[0]=="back": 
        if q.qsize()>0: sys.stdout.write(str(q.queue[-1])+'\n')
        else: sys.stdout.write(str(-1)+'\n')