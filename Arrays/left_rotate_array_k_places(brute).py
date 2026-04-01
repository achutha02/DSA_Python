nums = [3, 4, 1, 5, 3, -5]

n = len(nums)
k = 8

k = k % n

temp = []
for i in range(k):
    temp.append(nums[i])

for i in range(k,n):
    nums[i-k] = nums[i]

for i in range(k):
    nums[n-k+i] = temp[i]

for num in nums:
    print(num, end=' ')



"""
Time Complexity: O(n), where N is the length of the array.
Three loops are used taking K, N-K, and K iterations respectively contributing to O(N+K). However, K can be N-1 in the worst case boiling down the time complexity as O(N).

Space Complexity: O(k) where k is the number of elements to be rotated
"""