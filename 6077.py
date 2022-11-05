#1부터 그 수까지 짝수만 합해 출력한다.
#5 (2 + 4 = 6)

n = int(input())
sum = 0

for i in range(1,n+1):
    if i % 2 == 0:
        sum += i

print(sum)