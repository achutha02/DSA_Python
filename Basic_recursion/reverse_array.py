def reverseArray(nums):
    reverse(nums, 0, len(nums) - 1)
    return nums

def reverse(nums, left, right):
    if left >= right:
        return
    
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp

    return reverse(nums, left+1, right-1)

arr = [1, 2, 3, 4, 5]
print(reverseArray(arr))