nums = [1, 2, 3, 6, 7, 5, 7]

n = len(nums)

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    
    else:
        freq[num] = 1

repeating = -1
missing = -1

for i in range(1, n+1):
    if i not in freq:
        missing = i
    
    elif freq[i] == 2:
        repeating = i

print([repeating,missing])



"""
Time Complexity: O(2*N), for using two loops each running for N times, where N is the size of the array.

Space Complexity: O(N) for using a hash array.
"""