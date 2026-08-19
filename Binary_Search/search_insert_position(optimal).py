nums = [1, 3, 5, 6]

n = len(nums)

target = 7

low = 0
high = n - 1

ans = n

while low <= high:
    mid = (low + high) // 2

    if nums[mid] >= target:
        ans = mid
        high = mid - 1

    else:
        low = mid + 1

print(ans)



"""
Time Complexity: O(logN), where N is the size of the given array. We are using the Binary Search algorithm, which divides the search space in half each time, resulting in a logarithmic time complexity.

Space Complexity: O(1), as we are not using any extra space to solve this problem.
"""