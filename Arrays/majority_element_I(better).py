nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

n = len(nums)

mpp = {}

for num in nums:
    if num in mpp:
        mpp[num] += 1
    else:
        mpp[num] = 1

found = False

for num, count in mpp.items():
    if count > (n//2):
        print(num)
        found = True
        break

if not found:
    print(-1)



"""
Time Complexity: O(N), where N is the size of the array.
The code goes through the array once to count frequencies using a hash map (O(N)), then checks the map to find the majority element (O(N) in the worst case). Since these are separate linear operations, the overall time complexity is O(N).

Space Complexity: O(N), for using a map data structure.
"""