nums = [2, 3, 7, 1, 3, 5]

n = len(nums)

cnt = 0

for i in range(0, n-1):
    for j in range(i+1, n):
        if nums[i] > nums[j]:
            cnt += 1

print(cnt)