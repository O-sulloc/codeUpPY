# i = 1
# sum = 0
#
# while i <= 9:
#     sum += i
#     i += 1
#
# print(sum)

#홀수
# i = 1
# sum = 0
#
# while i <= 9:
#     if i % 2 == 1:
#         sum += i
#     i += 1
#
# print(sum)

#for문으로 구현
#1부터 9까지 더하기

sum = 0

for i in range(1,10):
    sum += i

print(sum)

# 합격 여부 출력
# continue
scores = [90, 85, 77, 65, 97] #학생들의 점수
cheating_list=[2,4] #블랙리스트 학생

for i in range(5): #0부터 4까지
    if scores[i] in cheating_list:
        continue #
    if scores[i] >= 80:
        print(i+1,"번 학생은 80점 이상으로 합격입니다.")

#break
x = 1
while True:
    print(x)
    if x ==5:
        break;
    x += 1