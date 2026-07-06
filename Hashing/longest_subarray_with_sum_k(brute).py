nums = [1, 2, 3, 1, 1, 1, 1, 4, 2, 3]

n = len(nums)

target = 3

max_length = 0

for i in range(n):
    for j in range(i, n):
        curr_sum = 0
        for k in range(i,j+1):
            curr_sum += nums[k]
        if curr_sum == target:
            max_length = max(max_length, j-i+1)

print(max_length)

