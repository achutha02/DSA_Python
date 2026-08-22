def lowerBound(nums, target):
    n = len(nums)
    low = 0
    high = n-1

    ans = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans

def upperBound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    ans = n

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans

nums = [5, 7, 7, 8, 8, 10]

target = 8

firstOcc = lowerBound(nums, target)

if firstOcc == len(nums) or nums[firstOcc] != target:
    print([-1, -1])

else:
    lastOcc = upperBound(nums, target)
    print([firstOcc, lastOcc])





"""
Time Complexity: 2*O(log N), where N is the size of the given array. Both the lowerBound and upperBound functions perform a binary search, which operates in logarithmic time. Thus, the overall time complexity is O(log N).

Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size. The space used by the variables low, high, mid, and ans does not depend on the size of the input array.
"""