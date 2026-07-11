nums = [4, 2, 2, 6, 4]

target = 6

count = 0

n = len(nums)

for i in range(n):
    for j in range(i, n):
        xor = 0
        for k in range(i, j+1):
            xor ^= nums[k]
        
        if xor == target:
            count += 1

print(count)



"""
Time Complexity: O(N3), where N is the size of the array. This is because we are using three nested loops, each running approximately N times.

Space Complexity: O(1) since we are not using any additional space.
"""