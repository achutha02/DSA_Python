nums = [7,8,1,2,3,3,3,4,5,6]

target = 3

n = len(nums)

isPresent = False

for i in range(n):
    if nums[i] == target:
        isPresent = True

print(isPresent)




"""
Time Complexity: O(N), for iterating through N elements, where N is the size of the given array.

Space Complexity:O(1), not using any extra space to solve this problem.
"""