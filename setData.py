# 집합 자료형

data = set([1, 1, 2, 3, 4, 4, 5, ])  # set에 넣어서 초기화
print(data)  # 중복된 자료는 제외하고 출력된.{1, 2, 3, 4, 5}

data = {1, 1, 2, 3, 4, 4, 5}  # 이렇게도 초기화 가능
print(data)  # 중복된 자료는 제외하고 출력된.{1, 2, 3, 4, 5}

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)  # {1, 2, 3, 4, 5, 6, 7}

# 교집합
print(a & b)  # {3, 4, 5}

# 차집합
print(a - b)  # {1, 2}

# 집합 관련 함수
num = set([1, 2, 3])

# 새 원소 추가 방법
num.add(4)
print(num)

# 새로운 원소 여러개 추가 방법
num.update([5, 6])
print(num)

# 특정 값 갖는 원소 삭제
num.remove(3)
print(num)
