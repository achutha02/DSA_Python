nums = [0, 0, 3, 3, 5, 6]

nums = sorted(list(set(nums)))

print(nums)


# Can also be written like this
"""
unique = set(nums)
unique_list = list(unique)
nums = sorted(unique_list)
"""


"""
Time Complexity: O(N*Log N)

Space Complexity: O(N), because in the worst case, all the elements of the array can be unique and it will take O(N) space. Here N represents the size of the array.
"""