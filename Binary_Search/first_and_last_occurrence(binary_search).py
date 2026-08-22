def firstOcc(nums, x):
    n = len(nums)

    low = 0
    high = n - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == x:
            first = mid
            high = mid - 1

        elif nums[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return first

def lastOcc(nums, x):
    n = len(nums)

    low = 0
    high = n - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == x:
            last = mid
            low = mid + 1

        elif nums[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return last

nums = [5,7,7,8,8,10]

target = 8

firstOccurrence = firstOcc(nums, target)

if firstOccurrence == -1:
    print([-1, -1])

else:
    lastOccurrence = lastOcc(nums, target)
    print([firstOccurrence, lastOccurrence])




"""
Time Complexity: O(log N), where N is the size of the given array. Both the firstOccurrence and lastOccurrence functions perform a binary search, which operates in logarithmic time. Thus, the overall time complexity is O(log N).

Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size. The space used by the variables low, high, mid, first, and last does not depend on the size of the input array.
"""