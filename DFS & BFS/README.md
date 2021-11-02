# DFS&BFS
그래프 탐색 알고리즘  
- [DFS & BFS](#DFS&BFS)  
  - [자료구조](#자료구조)
    - [스택 자료구조](#스택-자료구조)
    - [큐 자료구조](#큐-자료구조)  
  - [재귀함수](#재귀함수)
    - 유클리드호제법
  - [DFS](#DFS)
  - [BFS](#BFS)
  - [문제풀이](#문제풀이)

- **탐색(Search)** 란, 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
- 대표적 DFS, BFS

## 자료구조
### 스택 자료구조
- 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)
- 입구와 출구가 동일한 형태로 스택을 시각화

```python
stack=[]
stack.append(5)
stack.append(2)
stack.pop()

stack[::-1]
```

### 큐 자료구조
- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)
- 입구와 출구가 모두 뚫려있는 터널과 같은 형태

```python
from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.append(3)
queue.popleft()

queue.reverse()
```
## 재귀함수
- 자기자신을 다시 호출하는 함수
- DFS를 실제로 구현하고자 할 때 구현하는 함수  
- 모든 재귀함수 <-> 모든 반복문
- 컴퓨터가 함수를 연속적으로 호출을 하게 되면 컴퓨터 메모리 내부의 스택프레임이 쌓임
  - 스택을 사용해야될때 구현상 스택 라이브러리 대신 재귀함수를 사용하는 경우가 많음


**유클리드 호제법**
- 두개의 자연수에 대한 최대공약수를 구하는 대표적인 알고리즘
- 두 자연수 A, B에 대하여 (A>B) A를 B로 나누는 나머지를 R
- 이때 A와 B의 최대 공약수는 B와 R의 최대공약수와 동일


```python
def gcd(a,b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a%b)
   

print(gcd(192, 162))
```
|알고리즘|사용|방법|
|:----:|-----|-----|
|DFS|경로의 특징을 저장해야되는 가중치 있는 문제 && 그래프가 크면|스택&재귀|
|BFS|미로찾기등 가장 짧은, 가장 빠른/간선의 비용들이 모두 같을 때|큐|

## DFS
### Depth-First Search
- 깊이 우선 탐색
- **스택 자료구조(혹은 재귀함수)** 를 이용
  - 탐색 시작 노드를 스택에 삽입하고 방문처리 함
  - 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리함
    - 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼냄
  - 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
```python
def dfs(graph, v, visited):
  #현재 노드를 방문 처리
  visited[v] = True
  print(v, end = ' ')
  #현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
## 그래프 문제의 경우 노드의 숫자가 1번부터 시작되는 경우의 수가 많아서 처음 list는 빈칸
graph = [[],
        [2,3,8],
        [1,7],  
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]]
#각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph, 1, visited)
```
## BFS
### Breadth-First Search (최단경로)
- 너비우선 탐색
- 그래프가 가까운 노드부터 우선적으로 탐색하는 알고리즘
- 큐 자료구조를 사용
  - 탐색 시작 노드를 큐에 삽입하고 방문처리
  - 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
  - 더이상 2번의 과정을 수행할 수 없을 때까지 반복

```python
from collections import deque

def bfs(graph, start, visited):
  # 큐를 구현을 위하여 deque 라이브러리 사용
  queue = dequq([start])
  # 현재 노드를 방문처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    #큐에서 하나의 원소를 뽑아서 출력
    v = queue.popleft( 
    print(v, end = ' ')
    # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
graph = [[],
        [2,3,8],
        [1,7],
        [1,4,5],
        [3,5],
        [3,4],
        [7],
        [2,6,8],
        [1,7]]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
```

### 문제풀이
1. 1,0으로만 채워진 2차원 행렬이 주어지고 0으로 묶을 수 있는 그룹의 수를 구하여라

```python
## graph 2차원 배열 내에 1,0

# 모든 노드(위치)에 대하여 음료수 채우기
for i in range(n):
  for j in range(m):
    #현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1
print(result)

## Visit하면 False로 바꿈
## True로 하나 추출하면 옆에 Graph되는 것들은 모두 False로
def dfs(x, y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x<= -1 or x>=n or y <= -1 or y>= m:
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    #해당 노드 방문 처리
    graph[x][y] = 1
    #상,하,좌,우의 위치들도 모두 재귀적으로 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
 return False

```
2. 미로 찾기
동빈이가 N x M 크기의 직사각형 형태의 미로에 갇혔는데 미로에는 여러 마리의 괴물이 있음  
동빈이의 위치는 (1,1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있음  
이때 괴물이 있는 부분이 0, 없는 부분이 1로 표시  
동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수  
- 하나씩 더해서 마지막 노드까지 가기
- 계속 수행해서 결과적으로 최단 경로의 값들이 1씩 증가하는 형태를 만듦

```python
from collections import deque

def bfs(x, y):
  queue = deque()
  # 첫 (x,y) 방문
  queue.append((x,y))
  # 큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 4가지 방향으로의 위치 확인
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      # 미로 찾기 공간을 벗어난 경우 무시
      if nx <0 or nx>= n or ny <0 or ny >= m:
        continue
      # 벽인 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
       
  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n-1][m-1]

# 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 수행한 결과 출력
print(dfs(0, 0))
```
