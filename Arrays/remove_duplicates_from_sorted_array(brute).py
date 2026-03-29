nums = [0, 0, 3, 3, 5, 6]

nums = sorted(list(set(nums)))

print(nums)


# Can also be written like this
"""
unique = set(nums)
unique_list = list(unique)
nums = sorted(unique_list)
"""