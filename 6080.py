# 주사위 경우의 수
# 2 3

# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3

n, m = map(int, input().split(" "))

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)