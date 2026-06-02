nums = [1, 1, 1, 2, 2, 2]

n = len(nums)

result = []

for i in range(n):
    if len(result) == 0 or result[0] != nums[i]:
        cnt = 0

        for j in range(n):
            if nums[i] == nums[j]:
                cnt += 1

        if cnt > (n // 3):
            result.append(nums[i])
    
    if len(result) == 2:
        break


print(result)




"""
Time Complexity: O(N^2), where N is the size of the array. As for every element of the array the inner loop runs for N times.

Space Complexity: O(1) the space used is so small that it can be considered constant.
"""