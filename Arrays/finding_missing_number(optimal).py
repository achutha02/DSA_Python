nums = [0, 2, 3, 1, 4]

n = len(nums)

sum1 = n * (n+1) // 2

sum2 = 0

for num in nums:
    sum2 += num

missing_num = sum1 - sum2

print(missing_num)



"""
Time Complexity: O(N), where N is size of array, to compute the sum of the array elements.

Space Complexity: O(1)
"""