# coTe
coding Test practice

## 복잡도: 알고리즘의 성능을 나타내는 척도
- **시간복잡도**: 특정한 크기의 입력에 대하여 알고리즘의 수행시간 분석
- **공간복잡도**: 특정하 크기의 입력에 대하여 알고리즘의 수행시간 ㅜ석

### 빅오표기법(Big-O Notation)
- 가장 빠르게 증가하는 하만을 고려하는 표기법 (함수의 상항만을 나타나게 됨) 

O(1) > O(logN) > O(N) > O(NlogN) > O(N^2) > O(N^3) > O(2^n)

```python
for n in array:
  summary += n

# n하나씩 확인 > O(n)

for i in array:
  for j in array:
      temp = i+j
      
# 시간복잡도 O(n^2)
```
### 요구사항에 따라 적잘한 알고리즘 설계하기
**시간제한(수행시간 요구사항) 확인하기**  

시간제한이 1초인 문제를 만났을 경우, 일반적으로
- N의 범위가 500인 경우: 시간복잡도가 O(N^3)인 알고리즘
- N의 범위가 2,000인 경우: 시간복잡도가 O(N^2)인 알고리즘
- N의 범위가 100,000인 경우: 시간복잡도가 O(NlogN)인 알고리즘
- N의 범위가 10,000,000인 경우: 시간복잡도가 O(N)인 알고리즘

### 일반적 문제 해결 과정
- 1. 지문 읽기 및 컴퓨터적 사고
- 2. **요구사항(복잡도) 분석** 
- 3. 문제해결을 위한 아이디어 찾기
- 4. 소스코드 설계 및 코딩

