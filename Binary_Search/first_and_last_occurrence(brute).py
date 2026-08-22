nums = [5, 7, 7, 8, 8, 10]
target = 8

n = len(nums)

first = -1
last = -1

for i in range(n):
    if nums[i] == target:
        if first == -1:
            first = i

        last = i

print(first, last)



"""
Time Complexity: O(N), where N is the size of the given array. This is because we are performing a linear search through the array to find the first and last occurrences of the target element.


Space Complexity: O(1), as we are not using any extra space that grows with the input size. We are only using a few additional variables to store indices and results.
"""