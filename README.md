# coTe  
## 목차   

- [복잡도: 알고리즘 성능을 나타내는 척도](#복잡도)  
  - [빅오표기법](#빅오표기법)
  - [요구사항에 따라 적잘한 알고리즘 설계하기](#요구사항에-따라-적잘한-알고리즘-설계하기)
- [파이썬의 자료형](#파이썬의-자료형)  
  - [정수형, 실수형](#정수형,-실수형)
  - [리스트 자료형](#리스트-자료형)
  - [문자열 자료형](#문자열-자료형)
  - [튜플 자료형](#튜플-자료형)
  - [사전 자료형](#사전-자료형)
  - [집합 자료형](#집합-자료형)
- [입출력 방법](#입출력-방법)  
  - [표준 입력 방법](#1.-표준-입력-방법)
  - [표준 출력 방법](#2.-표준-출력-방법)
- [조건문과 반복문](#조건문과-반복문)
  - [조건문](#조건문)
  - [반복문](#반복문)
- [함수](#함수)
- [표준 라이브러리](#표준-라이브러리)

---

## 복잡도
알고리즘의 성능을 나타내는 척도
- **시간복잡도**: 특정한 크기의 입력에 대하여 알고리즘의 수행시간 분석
- **공간복잡도**: 특정하 크기의 입력에 대하여 알고리즘의 수행시간 ㅜ석

### 빅오표기법
Big-O Notation
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


### 수행시간 측정 소스코드
```python
import time
start_time = time.time()
'''문제풀이'''
end_time = time.time()
print("time:" ,end_time - start_time)
```

## 파이썬의 자료형

정수형, 실수형, 복소수형, 문자열, 리스트, 튜플, 딕셔너리

### 정수형, 실수형
- (정수형)양의 정수, 음의 정수 0
- (실수형)소수점 아래의 데이터를 포함하는 자료형(-.7, 5.)
- (실수형) e나 E는 다음에 나오는 수의 10의 지수부를 의미(1e9 -> 10억)
- (실수형) round() (```round(123.456, 2)``` -> ```123.46``` (소수 셋째자리에서 반올림))
- (정수형) / 실수형, // 몫, % 나머지

### 리스트 자료형
Array 기능
- 초기화시, list() 혹은 간단히 [] 사용 가능
- 리스트의 원소에 접근할 때 인덱스 값을 괄호에 넣어줌(0부터 시작)
- ```a = [0] * 10```로 초기화도 가능

#### 인덱싱과 슬라이싱
```print(a[1:3])```

#### 리스트 컴프리헨션
- 대괄호 안에 조건문과 반복문을 적용하여 리스트 초기
```array = [i for i in range(10)]```  
```array = [i for i in range(10) if i % 2 == 0]```  
- 2차원 리스트를 초기화할때 효과적
- N과 M크기의 2차원 리스트 ```array = [[0] * m for _ in range(n)]```

#### 기타 메서드
- append() > O(1)
- sort() // sort(reverse = True) > O(NlogN)
- reverse()  > O(N)
- insert() > O(N)
- count() > O(N)
- remove() > O(N)
```python
a.reverse()
a.insert(2,3)
a.count('b')
a.remove('c')

a = [1,2,3,4,5,5]
remove_set = {3,5} # 집합 자료형(특정 원소가 있는지만 확인할때)
 
result = [i for i in a if i not in remove_set] 
```

### 문자열 자료형
- 문자열 변수 초기화: 큰 따옴표(")나 작은 따옴표(')을 이용하여 초기화
- 백슬래시를 사용하면 문자열 내 따옴표들 사용가능 ```data = "Don't you know \"Python\"?"```
- 덧셈 기호를 사용하면 문자열이 더해짐 (연결됨)
- 특정 양의 정수와 곱하면 반복됨

### 튜플 자료형
- 튜플은 한번 선언된 값은 수정 불가
- []는 리스트 () 튜플
- 공간효율적

사용하기 좋은 경우  
- 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
  - 최단경로 알고리즘에서는 (비용, 노드번호)의 형태
- 데이터의 나열을 Hashing의 키 값으로 사용해야 될 때
  - 튜플은 변경이 불가능하여 리스트와 다르게 키 값으로 사용가능
- 리스트보다 메모리 효율적으로 사용가능
-  

### 사전 자료형
- 사전 자료형은 **키(key)**와 **값(value)**의 쌍을 데이터로 가지는 자료형
- ```Immutable(변경 불가능한) 자료형```
- 파이썬의 사전 자료형은 Hash Table을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리가능

```python
a = dict()
a['홍길동'] = 98
a['이순신'] = 96

print(a['이순신'])
key_list = list(a.keys())
```

### 집합 자료형
- 중복을 허용하지 않음
- 순서가 없음
- 리스트 혹은 문자열을 이용하여 초기화 가능
  - set() 함수를 사용
- 데이터 조회 및 수정에 있어서 O(1)의 시간에 처리가능

```python
# 초기화 방법1
data = set([1,2,3,4,5])

# 초기화 방법2
data = {1,2,3,4,5}
```

#### 집합 자료형의 연산
- 합집합 ```print(a|b)```
- 교집합 ```print(a&b)```
- 차집합 ```print(a-b)```

```python
data = set([1,2,3])
data.add(4)
data.update([5,6])
data.remove(3)
```
- 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻음
- 사전자료형이나 집합자료형은 **순서가 없기 때문에** 인덱싱으로 인하여 값을 얻음
  - 사전의 키(key) 혹은 집합의 원소(element)를 이용해 O(1)의 시간 복잡도로 조회함

## 입출력 방법
### 1. 표준 입력 방법
- ```input()``` : 한 줄의 문자열을 입력 받는 함수
- ```map()```: 리스트의 모든 원소에 각각 특정한 함수를 적용할때 사용
```python
a,b,c = map(int, input().split())
```
- 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우 : **입력의 갯수가 많을 경우**
  - **이진탐색**, **정렬**, **그래프** 문제에서 많이 사용됨
  - ```sys.stdin, readline()```메서드 이용
  - 단, 입력 후 Enter가 줄바꿈 기호로 입력되므로 rstrip()메서드를 함께 사용

```python
import sys
data = sys.stdin.readline().rstrip()
```

### 2. 표준 출력 방법
- ```print()``` : 사용
- 각 변수를 콤마를 이용하여 띄어쓰기로 구분하여 출력할 수 있음
- print()는 기본적으로 출력 이후에 줄바꿈을 수행
  - 줄바꿈을 원치 않을 경우 'end' 속성을 이용할 수 있음
 ```python
 print(7, end = " ")
 ```
 - ```f-string```문법

```python
answer= 7
print(f'정답은 {answer}입니다.')
```

## 조건문과 반복문
### 조건문
- 프로그램의 흐름을 제어하는 문법
- ```if~elif~else```
#### 비교연산자
|비교 연산자|설명|
|:---------|:---|
|X==Y|X와 Y가 서로 같을때 참이다|
|X!=Y|X와 Y가 서로 다를때 참이다|
|X>Y|X가 Y보다 클 때 참이다|
|X<Y|X가 Y보다 작을 때 참이다|
|X>=Y|X가 Y보다 크거나 같을 때 참이다|
|X<=Y|X가 Y보다 작거나 같을 때 참이다|

#### 논리연산자
|논리 연산자|설명|
|:---------|:---|
|X and Y|X와 Y가 모두 참일때 참이다|
|X or Y|X와 Y중에 하나만 참이어도 참이다|
|not X|X가 거짓일 때 참이다|

#### 기타 연산자
- 리스트, 튜플, 문자열, 딕셔너리 모두에 사용가능

|in, not in 연산자|설명|
|:---------|:---|
|x in 리스트|리스트 안에 x가 들어가 있을 때 참이다|
|x not in 문자열|문자열 안에 x가 들어가 있지 않을 때 참이다|

#### pass

### 반복문
- 특정한 소스코드를 반복적으로 실행하고자 할 때 사용하는 문법
- ```while```혹은 ```for```문

## 함수
- 내장함수: 파이썬이 기본적으로 제공하는 함수
- 사용자 정의 함수: 개발자가 직접 정의하여 사용할 수 있는 함수

### global 키워드
global 키워드로 변수를 지정하면 해당 함수에서는 지역변수를 만들지 않고, **함수 바깥에 선언된 변수를 바로 참조**하게 됨
```python
a = 0
def func():
  global a
  a += 1

for i in range(10):
  func()
print(a) # 10
# 지역변수라면 1임
```

### 람다 표현식
```python
def add(a, b):
  return a+b
print(add(3, 7))
print((lambda a,b: a+b)(3, 7))
```

```python
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
def my_key(x):
  return x[1]
print(sorted(array, key = my_key))
print(sorted(array, key = lambda x: x[1]))
```

```python
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b: a+b, list1, list2)
# a = list(map(int, a))
# a = list(map(str, range(10)))
# map(적용시킬 함수, 적용할 값들)
# list(map(lambda x: x*2, [5,4,3,2,1]))
print(list(result)) #[7,9,11,13,15]
```

## 표준 라이브러리
- 내장 함수: 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들
  - sum(), min(), max(), eval(), sorted()
  - ```result = eval("(3+5)*7")```
- itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들 제공
  - 순열과 조합 라이브러리
- headpq: Heap(힙) 자료구조를 제공
  - 우선순위 큐 기능을 구현하기 위함
  - 최단경로
- bisect: 이진 탐색(Binary Search) 기능을 제공
- collections: 덱(deque), 카운터(Counter)등의 유용한 자료구조 포함
- math: 필수적인 수학적 기능
 - 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 파이(pi)


### 순열과 조합
- 순열
  - 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
  - nPr = n * (n-1) * (n-2) * ... * (n-r+1)
- 조합
  - 서로 다른 n개에서 **순서에 상관 없이** 서로 다른 r개를 선택하는 것
  - nCr = n * (n-1) * (n-2) * ... * (n-r+1) / r!

- 주의
  - ```combinations```, ```permutations```, ```product``` 세 메소드 모두 generator이기 때문에 list() 로 캐스팅하여 다른 곳에 저장해두지 않으면 사라짐

```python
# 순열
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)  #[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C')..]

# 조합
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2)) #2개를 뽑는 모든 조합 구하기
print(result) #[('A', 'B'), ('B','C'), ('A', 'C')]
```

```python
# 중복 순열
from itertools import product
data = ['A','B','C']
result = list(product(data, repeat = 2)) # 2개를 뽑는 모든 순열 구하기 (중복허용)
# AA, AB, AC, BB, BA, ..

# 중복 조합
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
```

### Counter
```python
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) #3
print(dict(counter))
```

### 최대 공약수와 최소 공배수
```python
import math
#최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
  return a*b//math.gcd(a,b)
print(math.gcd(a,b)) #최대공약수(GCD)
print(lcm(a,b)) #최소공배수(LCM)
```
