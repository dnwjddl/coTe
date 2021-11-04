## https://www.acmicpc.net/problem/14499

## 골드 4 - 구현

N, M, x, y, K = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(N)]

dice = [0] * 6

order = list(map(int, input().split()))
# 동 서 남 북
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(K):
    dir = order[i]
    nx = x+ dx[dir -1]
    ny = y+ dy[dir -1]
    if 0<=nx<N and 0<=ny<M:
        if dir == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif dir == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif dir == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        else:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[5]
        else:
            dice[5] = graph[nx][ny]
            graph[nx][ny] = 0
        x = nx
        y = ny
        print(dice[0])
        
    else:
        continue
