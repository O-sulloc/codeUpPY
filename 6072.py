# 정수 1개 입력받아 카운트다운 출력하기1

# while n != 0: #3 != 0
#     for i in range(n): #0,1,2,3
#         print(n - i) #3-0, 3-1, 3-2 ...
#     if n - i == 1:
#         break

n = int(input())

while n != 0:
    print(n)
    n -= 1