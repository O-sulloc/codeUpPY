# 등비 수열 2 6 18 54 162 486 ...
# 2 3 5

a, r, n = map(int, input().split())

for i in range(n-1):
    a *= r

print(a)