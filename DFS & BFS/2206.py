from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs():
    queue = deque()
    queue.append([0, 0, 1])
    visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visit[0][0][1] = 1
    while queue:
        x, y, z = queue.popleft()
        if x == N-1 and y== M-1: #최종 목적지에 도달
            return visit[x][y][z]
        for i in range(4):
            nx, ny = x +dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if array[nx][ny] == 1 and z == 1: # 벽 부시기
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    queue.append([nx, ny, 0]) #z는 벽이 부셔졌으니까 1->0
                elif array[nx][ny] == 0 and visit[nx][ny][z] == 0: #빈 방이라면
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    queue.append([nx, ny, z])
    return -1 #목적지에 도달할 수 없을 때
N, M = map(int, input().split())
array = [list(map(int, list(input()))) for _ in range(N)]
print(dfs())
