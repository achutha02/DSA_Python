nums = [3, 5, 8, 15, 19]

x = 9

n = len(nums)

ans = n

for i in range(n):
    if nums[i] >= x:
        ans = i
        break

print(ans)


"""
Time Complexity: O(N), where N is the size of the given array. In the worst case, we have to traverse the entire array. This is the time complexity of the linear search algorithm.

Space Complexity: O(1), no extra space is used to solve this problem.
"""