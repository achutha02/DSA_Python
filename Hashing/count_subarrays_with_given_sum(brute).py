nums = [1, 1, 1]

target = 2

n = len(nums)

cnt = 0

for i in range(n):
    for j in range(i, n):
        sum1 = 0
        for k in range(i, j+1):
            sum1 += nums[k]
        
        if sum1 == target:
            cnt += 1

print(cnt)