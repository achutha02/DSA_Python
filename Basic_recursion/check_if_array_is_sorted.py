def isSorted(nums):

    if len(nums) <= 1:
        return True
    
    return sort(nums, 0, 1)

def sort(nums, left, right):
    if right > len(nums) - 1:
        return True
    
    if nums[left] > nums[right]:
        return False
    
    return sort(nums, left+1, right+1)

nums=[1,2,3,4,6,5]
print(isSorted(nums))