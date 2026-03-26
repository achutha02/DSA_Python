nums = [3, 3, 6, 1]

n = len(nums)

largest = nums[0]

for i in range(n):
    if nums[i] > largest:
        largest = nums[i]

print(largest)
