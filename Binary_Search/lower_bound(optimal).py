nums = [3, 5, 8, 15, 19]

x = 9

n = len(nums)

ans = n

low = 0
high = n-1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] >= x:
        ans = mid

        high = mid - 1
    else:
        low = mid + 1

print(ans)




"""
Time Complexity: O(log N), where N is the size of the given array. For using the Binary Search algorithm, the search space is divided in half each time, resulting in a logarithmic time complexity.

Space Complexity: O(1), not using any extra space to solve this problem.
"""

