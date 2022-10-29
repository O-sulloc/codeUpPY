a = [1,4,3]
print("기본출력",a)

a.append(2)
print("append",a)

a.sort()
print("sort",a)

a.sort(reverse=True)
print("내림",a)

a.reverse()
print(a)

a.insert(1,4) #1번 인덱스 사이에 100번 낑겨넣음
print(a)

print(a.count(4)) #4가 몇개 있는지 세기 2개

a.remove(4) # 숫자 3을 지워
print(a)

b = [1,2,3,3,5,6,5,5,2]
remove_set = {3,5} #집합 자료형. 3,5를 제거하고 싶음

result = [i for i in b if i not in remove_set]
# if b에서 하나씩 꺼낸 i가 remove_set의 수에 해당하지 않으면
# 않으면 i에 넣어. 그리고 그걸 Result에 넣어

print(result)