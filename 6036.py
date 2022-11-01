# 단어와 반복 횟수를 입력받아 여러 번 출력해보자.

# 단어와 반복 횟수가 공백으로 구분되어 입력된다.
# 입력된 단어를 입력된 횟수만큼 반복해 출력한다. love 3

word, r = input().split(" ")
r = int(r)
for i in range(r):
    print(word, end="")