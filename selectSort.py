from random import randint
import time

# 배열에 10,000개의 정수 삽입
arr = []
for _ in range(10000):
    arr.append(randint(1,100)) #1부터 100 사이의 랜덤한 정수를 넣어. 10000번

# 선택 정렬 프로그램 성능 측정 해보기
start_time = time.time()

arr.sort()

end_time = time.time()
print(end_time - start_time)