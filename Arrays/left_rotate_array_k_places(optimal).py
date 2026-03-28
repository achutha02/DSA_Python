def reverseArray(nums, start, end):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1

def rotateArray(nums, k):
    n = len(nums)
    k = k % n

    reverseArray(nums, 0, k-1)

    reverseArray(nums, k, n-1)

    reverseArray(nums, 0, n-1)

nums = [3, 4, 1, 5, 3, -5]

rotateArray(nums, 8)

for num in nums:
    print(num, end=' ')

