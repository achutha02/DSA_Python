arr = [1, 2, 3, 4, 5]

n = len(arr)

ans = [0] * n

for i in range(n):
    ans[n-i-1] = arr[i]

for i in range(n):
    arr[i] = ans[i]

print(arr)
