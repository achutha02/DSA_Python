nums = [7,8,1,2,3,3,3,4,5,6]

target = 9

n = len(nums)

low = 0
high = n - 1

isPresent = False

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        isPresent = True
        break

    if nums[low] == nums[mid] == nums[high]:
        low += 1
        high -= 1
        continue

    if nums[low] <= nums[mid]:
        if nums[low] <= target <= nums[mid]:
            high = mid - 1

        else:
            low = mid + 1

    else:
        if nums[mid] <= target <= nums[high]:
            low = mid + 1

        else:
            high = mid - 1

print(isPresent)






"""
Time Complexity:O(logN) for the best and average cases. As in the best and average scenarios, the binary search algorithm is primarily used and hence the time complexity is O(logN).
However, in the worst-case scenario, it'll be O(N/2) where all array elements are the same but not the target (e.g., given array = {3, 3, 3, 3, 3, 3, 3}), we continue to reduce the search space by adjusting the low and high pointers until they intersect, which will end up taking O(N/2) time complexity.


Space Complexity:O(1), as we are not using any extra space to solve this problem.
"""