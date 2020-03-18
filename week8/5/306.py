def min(a: int, b: int, c: int, d: int):
    min1 = a if a < b else b
    min2 = c if c < d else d
    return min1 if min1 < min2 else min2

arr=list(map(int,input().split()))
a = arr[0]
b = arr[1]
c = arr[2]
d = arr[3]

print(min(a, b, c, d))

