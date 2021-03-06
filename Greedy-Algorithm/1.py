'''
1. 거스름돈 문제

- 당신은 음식점의 계산을 도와주는 점원입니다
- 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정합니다.
- 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러주어야 할 동전의 최소 개수를 구하세요.
- 단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.
'''
N = int(input("거슬러줘야할 돈은?"))
a = N // 500

a = a % 500
b = a // 100

b = b % 100
c = b // 50

d = c % 50
d = d // 10


'''
# 문제 해결 아이디어

- 최적의 해를 빠르게 구하기 위해서는 **가장 큰 화폐 단위부터** 돈을 거슬러 주면 됩니다.
- N원을 거슬러줘야 될때, 500원으로 거슬러 줄 수 있을 만큼 우선 거슬러줌

# 정당성 분석
-- 이런식으로 그리디 알고리즘 문제에서는 이처럼 문제 풀이를 위한 최소한의 아이디어를 떠올리고, 그것이 정당한지 검토할 수 있어야됨
'''
n = 1260 # 거스름돈
count = 0

array = [500, 100, 50, 10]
for coin in array:
  count += n//coin
  n %= coin
  
print(count)

# 화폐의 종류가 K라고 할 때, 소스코드의 시간 복잡도는 O(K)임
