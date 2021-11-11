from collections import deque

def bfs(array, x, y):
    queue = deque()
    queue.append((x, y))
    array[x][y]=0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and array[nx][ny] == 1: #한번도 방문하지않은 집이 있는 표시
                array[nx][ny] = 0 #집에 방문했었음을 표시
                count += 1
                queue.append((nx, ny))
    return count

N = int(input())
array = [list(map(int, input())) for _ in range(N)]
answer = []
dx, dy = [-1,1, 0,0], [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            answer.append(bfs(array, i, j))
print(len(answer))
for ans in sorted(answer):
    print(ans)
    
# while queue:
# x, y = queue.popleft()
# array[x][y] = 0 ([nx][ny] 만 바꾸지말고)
# count = 1 (count= 0이 아님)
## 확인해주기
