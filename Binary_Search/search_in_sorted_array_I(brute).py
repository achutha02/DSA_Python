nums = [4,5,6,7,0,1,2]

target = 0

n = len(nums)

result = -1

for i in range(n):
    if nums[i] == target:
        result = i
        break

print(result)