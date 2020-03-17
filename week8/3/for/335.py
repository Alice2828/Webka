import math

a = int(input())
b = int(input())

for i in range(a, b):
    if math.modf(math.sqrt(i))[0] == 0:
        print(i)