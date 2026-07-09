nums = [1, 1, 1]

target = 2

n = len(nums)

cnt = 0

for i in range(n):
    currentSum = 0
    for j in range(i, n):
        currentSum += nums[j]

        if currentSum == target:
            cnt += 1

print(cnt)