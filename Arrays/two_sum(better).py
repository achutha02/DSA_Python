nums = [2, 6, 5, 8, 11]

target = 14

n = len(nums)

found = False

mpp = {}

for i in range(n):
    num = nums[i]

    more_needed = target - num

    if more_needed in mpp:
        print(mpp[more_needed],i)
        found = True
        break

    mpp[num] = i

if not found:
    print(-1, -1)




"""
Time Complexity: O(N), where N is the size of the array. The loop runs N times in the worst case and searching in a hashmap takes O(1) generally. So the time complexity is O(N).

Note:In the worst case(which rarely happens), the unordered_map takes O(N) to find an element. In that case, the time complexity will be O(N^2). If we use map instead of unordered_map, the time complexity will be O(N* logN) as the map data structure takes logN time to find an element.


Space Complexity:  O(N) for using the map data structure.
"""