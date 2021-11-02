# DFS&BFS
그래프 탐색 알고리즘  
- [DFS & BFS](#DFS&BFS)  
  - [자료구조](#자료구조)
    - [스택 자료구조](#스택-자료구조)
    - [큐 자료구조](#큐-자료구조)  
  - [재귀함수](#재귀함수)
    - 유클리드호제법
  - [DFS](#DFS(Depth-First-Search))

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

## DFS(Depth-First Search)
