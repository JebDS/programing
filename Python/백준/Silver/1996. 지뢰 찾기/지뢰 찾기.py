a=int(input())
map=[]
li=[]
l=0
for i in range(a):
    map.append(list(input()))

#변환
for i in range(a):
    for j in range(a):
        if map[i][j]=='.':
            map[i][j]= 0
        else:
            li.append(int(map[i][j]))
            map[i][j]='*'

#본격지뢰쇼 #대각선 없음!!
for i in range(a):
    for j in range(a):
        if map[i][j]=='*': 
            if i != 0: #상
                if map[i-1][j] != '*':
                    map[i-1][j]+=li[l]
            if i != a-1: #하
                if map[i+1][j] != '*':
                    map[i+1][j]+=li[l]
            if j != 0: #좌
                if map[i][j-1] != '*':
                    map[i][j-1]+=li[l]    
                if i != 0: #좌상
                    if map[i-1][j-1] != '*':
                        map[i-1][j-1]+=li[l]
                if i != a-1: #좌하
                    if map[i+1][j-1] != '*':
                        map[i+1][j-1]+=li[l]
                    
            if j != a-1: #우
                if map[i][j+1] != '*':
                    map[i][j+1]+=li[l]
                if i != 0: #우상
                    if map[i-1][j+1] != '*':
                        map[i-1][j+1]+=li[l]
                if i != a-1: #우하
                    if map[i+1][j+1] != '*':
                        map[i+1][j+1]+=li[l]
            l+=1

#변환
for i in range(a):
    for j in range(a):
        try:
            if map[i][j]>=10:
                map[i][j]= 'M'
        except:
            pass

for i in map:
    for j in i:
        print(j,end='')
    print()

