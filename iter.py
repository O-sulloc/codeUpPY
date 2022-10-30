# 조건문

x = 15

if x >= 10:
    print("x>=10")
if x >= 0:
    print("x>=0")
if x >= 30:
    print("x>=30")

# if elif else
score = 0
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# block
data = 95
if data >= 80:
    print("80점 이상입니다.")
    if data >= 90:
        print("매우 우수한 성적입니다.")

else:
    print("80점 미만입니다.")

print("출력 끝")