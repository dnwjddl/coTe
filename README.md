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
```

