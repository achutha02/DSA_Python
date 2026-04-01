nums = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

n = len(nums)

temp = []

for i in range(n):
    if nums[i] != 0:
        temp.append(nums[i])
    
for i in range(len(temp)):
    nums[i] = temp[i]

for i in range(len(temp), n):
    nums[i] = 0

for num in nums:
    print(num, end=' ')



"""
Time Complexity: O(2*N), O(N) for copying non-zero elements from the original to the temporary array. O(X) for again copying it back from the temporary to the original array. O(N-X) for filling zeros in the original array. Here N is the size of the array and X is the number of non-zero elements.

Space Complexity: O(N), for using a temporary array to solve this problem and the maximum size of the array can be N in the worst case.
"""