# 실수 2개(f1, f2)를 입력받아
# f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.
#
# 4.0 2.0

a,b = list(map(float, input().split(" ")))

print(a**b)