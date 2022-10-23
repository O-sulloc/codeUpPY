array = [i for i in range(10) if i % 2 ==0]

print(array)

b = []
for i in range(10):
    if i % 2 == 0:
        b.append(i)

print(b)

#1부터 9까지 수들의 제곱 값을 구하는
c = [i*i for i in range(10)]
print(c)

n = 4
m = 3
twoArr = [[0] * m for _ in range(n)]
twoArr[3][1] = 1
print(twoArr)