nums = [4, 2, 2, 6, 4]

target = 6

n = len(nums)

count = 0

for i in range(n):
    xor = 0
    for j in range(i, n):
        xor ^= nums[j]

        if xor == target:
            count += 1

print(count)


"""
Time Complexity: O(N2), where N is the size of the array. Since we are using two nested loops, each running for N times, the time complexity will be approximately O(N2).

Space Complexity: O(1) as we are not using any additional space.
"""