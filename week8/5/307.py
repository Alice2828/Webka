def power(a, n):
    if n == 0:
        return 1
    if n>0:
        return a*power(a, n-1)
    return (1/a)*(1/power(1/a,n+1))


arr = [int(i) for i in input().split()]
print(power(arr[0], arr[1]))