n = int(input())

check = list(map(int,input().split()))
check.reverse()

for i in range(n):
    print(check[i], end=" ")