# https://www.acmicpc.net/problem/4673
# 실버 5 - 구현

numbers = list(range(1, 10001))
generate = []
for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 10000:
        generate.append(num)

for i in set(generate):
    numbers.remove(i)
for num in numbers:
    print(num)
