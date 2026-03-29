nums = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

n = len(nums)

j = -1

for i in range(n):
    if nums[i] == 0:
        j = i
        break

for i in range(j+1, n):
    if nums[i] != 0:
        nums[j], nums[i] = nums[i], nums[j]
        j += 1

for num in nums:
    print(num, end=' ')