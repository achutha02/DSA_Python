def floor(nums, n, x):
    low = 0
    high = n-1

    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] <= x:
            ans = nums[mid]
            low = mid + 1

        else:
            high = mid - 1

    return ans

def ceil(nums, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= x:
            ans = nums[mid]
            high = mid - 1

        else:
            low = mid + 1

    return ans

nums = [3, 4, 4, 7, 8, 10]

x = 5

n = len(nums)

floor_ans = floor(nums, n, x)

ceil_ans = ceil(nums, n, x)

print(floor_ans, ceil_ans)