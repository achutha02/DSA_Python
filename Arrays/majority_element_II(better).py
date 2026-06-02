nums = [1, 2, 1, 1, 3, 2]

n = len(nums)

result = []

mini = (n // 3) + 1

mpp = {}

for num in nums:
    if num in mpp:
        mpp[num] += 1
    else:
        mpp[num] = 1

    if mpp[num] == mini:
        result.append(num)

print(result)



"""
Time Complexity: O(N), where N is size of the given array. For using an unordered map data structure, where insertion in the map takes O(1) time and we are doing it for N elements. On using map instead, the first term will be O(N*logN) for the best and average case and for the worst case, it will be O(N^2).

Space Complexity: O(N) for uing a map data structure. A list that stores a maximum of 2 elements is also used, but that space used is so small that it can be considered constant.
"""