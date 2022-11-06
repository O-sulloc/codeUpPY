w,h,b = map(int, input().split(" "))

result = w*h*b  # bit
result /= 8  # byte
result /= 1024  # kb
result /= 1024  # mb

print(format(result, ".2f"), 'MB')