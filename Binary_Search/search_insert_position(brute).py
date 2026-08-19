nums = [1, 3, 5, 6]

target = 7

n = len(nums)

ans = n

for i in range(n):
    if nums[i] >= target:
        ans = i
        break

print(ans)



"""
Time Complexity: O(N), where N is the size of the given array. We are using the Linear Search algorithm, which iterates linearly resulting in N time complexity.

Space Complexity: O(1), as we are not using any extra space to solve this problem.
"""
    