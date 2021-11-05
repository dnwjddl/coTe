# Recursive Error 나오지않기 위해서
import sys
sys.setrecursionlimit(100000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, k):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < N) and (0 <= ny < N) and not visit[nx][ny] and zone[nx][ny] > k:
            visit[nx][ny] = True
            bfs(nx, ny, k)

N = int(input())
zone = [list(map(int, input().split())) for _ in range(N)]
answer = 1
for k in range(max(map(max, zone))):
    visit = [[False]*N for _ in range(N)]
    safe = 0
    for i in range(N):
        for j in range(N):
            # 해당 zone이 K 이상이거나 한번도 방문한 적 없다 판단했을때 visit 을 1로 바꿈
            if zone[i][j] > k and not visit[i][j]:
                safe += 1
                visit[i][j] = True
                # Recursive을 해서 bfs을 통해 확인함
                bfs(i, j, k)
    answer = max(answer, safe)

print(answer)
