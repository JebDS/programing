n = int(input())
di={'q1':0, 'q2':0, 'q3':0, 'q4':0, 'ax':0}

for _ in range(n):
    x, y = map(int, input().split())
    if (x==0 or y==0):
        di['ax']+=1
    elif (x>0 and y>0):
        di['q1']+=1
    elif (x<0 and y>0):
        di['q2']+=1
    elif (x<0 and y<0):
        di['q3']+=1
    elif (x>0 and y<0):
        di['q4']+=1

for i in range(1, 5):
    print("Q"+str(i)+":", di['q'+str(i)])
print("AXIS:", di['ax'])