# 1 3 5
# 1, 4, 7, 10, 13 (13 출력) 등차수열

a, d, n = map(int, input().split())

for i in range(n - 1):
    a += d

print(a)
