nums = [3, 4, 1, 5, 3, -5]

n = len(nums)
k = 8

k = k % n

temp = []
for i in range(k):
    temp.append(nums[i])

for i in range(k,n):
    nums[i-k] = nums[i]

for i in range(k):
    nums[n-k+i] = temp[i]

for num in nums:
    print(num, end=' ')