# n = ord(input())
# print(n)
# ord() 사용해서 영문자 -> 10진수 유니코드
# ord( ) 는 어떤 문자의 순서 위치(ordinal position) 값을 의미한다.

array = [3,5,1,2,4]

for i in array:
    for j in array:
        temp = i * j
        print(temp)