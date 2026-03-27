nums = [8, 8, 7, 6, 5]

n = len(nums)

nums.sort()

largest = nums[-1]

secondLargest = -1

for i in range(n-2, -1, -1):
    if nums[i] != largest:
        secondLargest = nums[i]
        break

print(secondLargest)