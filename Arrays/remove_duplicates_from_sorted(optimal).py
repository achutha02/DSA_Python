nums = [0, 0, 3, 3, 5, 6]

n = len(nums)

i = 0

for j in range(1, n):
    if nums[j] != nums[i]:
        nums[i+1] = nums[j]
        i += 1

for j in range(i+1):
    print(nums[j], end=" ")


"""
Time Complexity: O(N)

Space Complexity: O(1)
"""