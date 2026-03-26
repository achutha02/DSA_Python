nums = [7, 7, 2, 2, 10, 10, 10]

n = len(nums)

nums.sort()

largest = nums[-1]

secondLargest = -1

for i in range(n-2, -1, -1):
    if nums[i] != largest:
        secondLargest = nums[i]
        break

print(secondLargest)