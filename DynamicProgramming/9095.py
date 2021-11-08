# n = 1 -> 1
# n = 2 -> 2
# n = 3 -> 4
# n = 4 -> 7
# n = 5 -> 13

def train(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return train(num-1) + train(num-2) + train(num-3)
T = int(input())
for _ in range(T):
    l = int(input())
    print(train(l))
    
    #############################
N = int(input())
ott = [1, 2, 4]
for i in range(3, 10):
    ott.append(ott[i - 3] + ott[i - 2] + ott[i - 1])
for _ in range(N):
    n = int(input())
    print(ott[n - 1])
