# https://www.acmicpc.net/problem/2941
## 실버 5 - 구현

alpha = ['c=','c-','dz=','d-','lj', 'nj', 's=', 'z=']

str = input()

for a in alpha:
    str = str.replace(a, '*')
    
print(len(str))
