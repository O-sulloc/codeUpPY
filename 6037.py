#반복 횟수와 문장이 줄을 바꿔 입력된다.

# 출력
# 입력된 횟수만큼 입력된 문장을 출력한다.
#
# 입력 예시
# 3
# I love CS

r = int(input())
sentence = input()

# for i in range(r):
#     print(sentence, end="")

print(sentence*r)

