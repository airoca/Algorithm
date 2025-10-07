def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer

def bfs(place):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(5):
        for j in range(5):
            if (place[i][j] == "P"):
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if (nx < 0 or nx >= 5 or ny < 0 or ny >= 5):
                        continue
                    if place[nx][ny] == "P":
                        return 0
                    if place[nx][ny] == "O":
                         for dd in range(4):
                            nnx = nx + dx[dd]
                            nny = ny + dy[dd]
                            if (nnx < 0 or nnx >= 5 or nny < 0 or nny >= 5):
                                continue
                            if nnx == i and nny == j:
                                continue
                            if place[nnx][nny] == "P":
                                return 0
    return 1