a, b, c = map(int, input().split(" "))

# a < b -> a < c

print((a if a<b else b) if (a if a<b else b) < c else c)