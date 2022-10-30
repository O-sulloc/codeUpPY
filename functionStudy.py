def add(a, b):  # parameter 매개변수
    return a + b


print(add(3, 7))  # argument 인자


def add(a, b):
    print("add 함수의 결과", a + b)


add(4, 7)


def subtract(a, b):
    return a - b


print(subtract(8, 3))

# global
z = 0


def func():
    global z
    z += 1


for i in range(10):
    func()

print(z)

# lamda
print((lambda a, b: a + b)(3, 7))

#lamda 성적순으로 오름차순 정렬
array =[('kjh',97),('hgd',32),('wbp',55)]

def asc(k):
    return k[1] #매개변수로 들어오는 K의 1번째 인덱스를 리턴해

print(sorted(array,key=asc))

print(sorted(array,key=lambda k: k[1]))