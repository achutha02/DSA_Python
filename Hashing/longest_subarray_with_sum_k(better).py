nums = [10, 5, 2, 7, 1, 9]

k = 15

n = len(nums)

maxLen = 0
sum = 0

preSumMap = {}

for i in range(n):
    sum += nums[i]

    if sum == k:
        maxLen = max(maxLen, i+1)

    rem = sum - k

    if rem in preSumMap:
        length = i - preSumMap[rem]
        maxLen = max(maxLen, length)
    
    if sum not in preSumMap:
        preSumMap[sum] = i

print(maxLen)


    
