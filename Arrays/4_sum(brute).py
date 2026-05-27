nums = [1, -2, 3, 5, 7, 9]

target = 7

n = len(nums)

ans = set()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                sum = nums[i] + nums[j] + nums[k] + nums[l]

                if sum == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]

                    temp.sort()

                    ans.add(tuple(temp))

print(list(ans))


"""
Time Complexity: O(N4) for using 4 nested loops, where N is size of the array.

Space Complexity: O(2 x no. of the quadruplets), for using a set data structure and a list to store the quads.
"""