a,b = map(int, input().split(" "))

#if not bool(a) and not bool(b):
if not (bool(a) or bool(b)):
    print(True)
else:
    print(False)