n = int(input())
arr=list(map(int,input().split()))
cnt = 0
for i in range (0, n):
      if(i > 0 and arr[i-1] < arr[i]):
        cnt += 1
print(cnt, end=" ")