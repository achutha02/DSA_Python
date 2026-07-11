nums = [4, 2, 2, 6, 4]

target = 6

xr = 0

n = len(nums)

count = 0

mpp = {}

mpp[xr] = mpp.get(xr, 0) + 1

for i in range(n):
    xr = xr ^ nums[i]

    x = xr ^ target

    count += mpp.get(x, 0)

    mpp[xr] = mpp.get(xr, 0) + 1

print(count)



"""
Time Complexity: O(N) or O(NxlogN), where N is the size of the array. If we use an unordered_map in C++, the time complexity is O(N). However, with a map data structure, the time complexity is O(NxlogN). In the worst case for an unordered_map, the searching time can increase to O(N), making the overall time complexity O(N2).


Space Complexity: O(N), as we are using a map data structure.
"""

