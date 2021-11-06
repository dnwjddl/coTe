# [x좌표][y좌표][벽 부순 횟수]
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs():
    queue = deque()
    queue.append([0, 0, 0])
    visit = [[[0] * (K+1) for _ in range(M)] for _ in range(N)] # 왜 K가 아니고 K+1?
    visit[0][0] = [1] * (K+1) # 처음 시작한 값은 1로 시작 [1,1,1]
    
    while queue:
        x, y, z = queue.popleft()
        
        if x == N-1 and y== M-1: #최종 목적지에 도달
            return visit[x][y][z]
        for i in range(4):
            nx, ny = x +dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny][z]: #부술 수 있는 벽이 남아져있으면
                if not array[nx][ny]: # 그냥 이동
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    queue.append((nx, ny, z))
                elif z < K: #벽 부수자
                    visit[nx][ny][z+1] = visit[x][y][z] + 1
                    queue.append((nx, ny, z+1))
    return -1 #목적지에 도달할 수 없을 때
N, M, K = map(int, input().split())
array = [list(map(int, list(input()))) for _ in range(N)]
print(dfs())
