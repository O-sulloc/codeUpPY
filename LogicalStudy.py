if True or False: #둘 중 하나만 true여도 true
    print("yes")

a = 15
if a>=0 and a<20: #and는 두 조건이 모두 true여야 true
    print("a는 0이상 20미만이다.")

#pass
num = 10

if num >= 50:
    pass
else:
    print("50점 미만입니다.")

# short expression
# num2 = 8
# if num2 >= 80: result = "pass"
# else: result = "try again"
#
# print(result)

# conditional expression
num2 = 87
result = "pass" if num2 >= 80 else "try again"

print(result)

# list
b = [1,2,3,4,5,5,5]
remove_set = {3,5}

# result =[]
# for i in b:
#     if i not in remove_set:
#         result.append(i)
#
# print(result)

result = [i for i in b if i not in remove_set]
print(result)

# 0<x<20
x = 15
if 0 < x < 20:
    print("0 이상 20미만이다.")