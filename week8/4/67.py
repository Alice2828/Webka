def sign(x: int):
    if(x < 0):
        return -1
    if(x > 0):
        return 1
    return 0

n = int(input())
a=list(map(int,input().split()))
ans = 0
for f in range(0, n-1):
    if (a[f] > 0 and a[f+1] > 0) or (a[f] < 0 and a[f+1] < 0):
        ans = 1
        break
if ans == 1:
    print('YES')
elif ans == 0:
    print('NO')