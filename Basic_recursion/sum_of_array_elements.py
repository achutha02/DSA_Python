def arraySum(nums):
    return sum(nums,0)

def sum(nums, left):
    if left >= len(nums):
        return 0
    
    return nums[left] + sum(nums, left+1)

arr = [1, 2, 3, 4, 5]
print(arraySum(arr))