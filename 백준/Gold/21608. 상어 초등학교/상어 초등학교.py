n = int(input())
lst = [[0]*n for _ in range(n)]
like = [[] for _ in range(n**2+1)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0

for _ in range(n**2):
    s, s1, s2, s3, s4 = map(int,input().split())

    like[s] = [s1, s2, s3, s4]
    temp = [[(0,0)]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            friend = 0
            blank = 0
            for k in range(4):
                if 0<=i+dx[k]<n and 0<=j+dy[k]<n:
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if lst[nx][ny] == 0:
                        blank += 1
                    elif lst[nx][ny] in like[s]:
                        friend += 1
            temp[i][j] = (friend, blank)

    friend, blank = 0,0

    sit = False
    
    for i in range(n):
        for j in range(n):
            if temp[i][j][0] > friend and lst[i][j]==0:
                x = i
                y = j
                friend = temp[i][j][0]
                blank = temp[i][j][1]
                sit = True
            elif temp[i][j][0] == friend and lst[i][j]==0:
                if temp[i][j][1] > blank:
                    x = i
                    y = j
                    blank = temp[i][j][1]
                    sit = True
            if not sit and lst[i][j]==0:
                x = i
                y = j
                sit = True         
    lst[x][y] = s

for i in range(n):
    for j in range(n):
        s = lst[i][j]
        friend = 0
        for k in range(4):
            if 0<=i+dx[k]<n and 0<=j+dy[k]<n:
                nx = i+dx[k]
                ny = j+dy[k]
                if lst[nx][ny] in like[s]:
                    friend += 1
        if friend==0:
            continue
        else:
            result += 10**(friend-1)

print(result)