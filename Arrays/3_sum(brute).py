nums = [2, -2, 0, 3, -3, 5]

n = len(nums)

triplet_set = set()

for i in range(n - 2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if nums[i] + nums[j] + nums[k] == 0:
                temp = [nums[i], nums[j], nums[k]]

                temp.sort()
                triplet_set.add(tuple(temp))

ans = [list(triplet) for triplet in triplet_set]

print(ans)



"""
Time Complexity: O(N^3 x log(no. of unique triplets)), where N is size of the array. Using 3 nested loops & inserting triplets into the set takes O(log(no. of unique triplets)) time complexity. But we are not considering the time complexity of sorting as we are just sorting 3 elements every time.

Space Complexity: O(2 x no. of the unique triplets) for using a set data structure and a list to store the triplets.
"""