h, b, c, s = map(int, input().split(" "))

result = h * b * c * s  # bit
result /= 8  # byte
result /= 1024  # kb
result /= 1024  # mb

print(format(result, ".1f"), 'MB')