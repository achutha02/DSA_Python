nums = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

n = len(nums)

temp = []

for i in range(n):
    if nums[i] != 0:
        temp.append(nums[i])
    
for i in range(len(temp)):
    nums[i] = temp[i]

for i in range(len(temp), n):
    nums[i] = 0

for num in nums:
    print(num, end=' ')