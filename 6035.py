# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

#0.5 2.0 input

num = list(map(float, input().split(" ")))

print(num[0] * num[1])