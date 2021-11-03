# https://www.acmicpc.net/problem/5430
## 골드 5 - 구현

N = int(input())
for _ in range(len(N)):
  # 수행할 함수
  p  = input()
  # 수의 갯수
  num = int(input())
  list = [int(input(x)) for x in range(len(num)))]
  
  for i in p:
    if len(list) == 0:
      print("error")
      break
    if i == 'R':
      list = list[::-1]
    if i == 'D':
      list = list[1:]
