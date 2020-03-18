import math

a = int(input())
b = int(input())

# for i in range(a, b):
#     if math.modf(math.sqrt(i))[0] == 0:
#         print(i)


for i in range (a, b+1):
    if math.sqrt(i) == math.ceil(math.sqrt(i)):
        print(i, end=' ')