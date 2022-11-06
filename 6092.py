n = int(input())  # 출석번호 부른 횟수

check = list(map(int, input().split()))  # 출석 번호 몇 번(number) 불렀는지

for i in range(1,24):
    print(check.count(i), end=" ")