# Binary Search
- 순차탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 **앞에서부터 데이터를 하나씩 확인**하는 방법
- 이진탐색: 정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며 데이터를 탐색**하는 방법
  - 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정함

### 이진탐색의 시간 복잡도
- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산횟수는 log2N에 비례함
- 초기데이터 개수가 32개일때, 1단계를 거치면 16개의 데이터만 남음
  - 2단계를 거치면 8개가량의 데이터만 남음
  - 3단계를 거치면 4개가량의 데이터만 남음
- 이진탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)을 보장

```python
# 재귀함수
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) //2
  if arrary[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  else:
    return binary_search(array, target, mid+1, end)

# 반복문
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) //2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid -1
    else:
      start = mid + 1
  return None

#######################################################
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result+1)
```

### 파이썬 이진 탐색 라이브러리
```python
from bisect import bisect_left, bisect_right
# bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
# bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

a = [1,2,4,4,8]
x = 4
print(bisect_left(a, x)) # 2
print(bisect_right(a, x)) # 4
```

#### 값이 특정 범위에 속하는 데이터 개수 구하기
```python
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a, 4, 4)) #값이 4인 데이터 개수 출력 -> 2
```

### 파라메트릭 서치(Parametric Search)
- **파라메트릭 서치**란 최적화 문제를 결정문제(예, 아니오)로 바꾸어 해결하는 기법
  - ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코딩 테스트에서는 파라메트릭 서치 문제는 **이진탐색을 이용**하여 해결 가능

## 문제풀기
- 0~max(array)까지 값 사이 중에서 조건에 만족하는 값 중 가장 큰 값을 고르는 문제
- ```이진탐색```생각
```python
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))
start = 0
end = max(array)

result = 0
while(start <= end):
  total = 0
  mid = (start + end) //2
  for x in array:
    # 잘랐을 때의 떡의 양 계산
    if x > mid:
      total += x-mid
  if total<m:
    end = mid -1
  else:
    result = mid
    start = mid+1
print(result)
```
- 
