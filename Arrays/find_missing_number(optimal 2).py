nums = [0, 2, 3, 1, 4]

xor1 = 0
xor2 = 0

for i in range(len(nums)):
    xor1 ^= (i+1)
    xor2 ^= nums[i]

print(xor1 ^ xor2)




"""
If nums = [1, 2, 4, 5] and n = 5

Full range:   1 ^ 2 ^ 3 ^ 4 ^ 5
Array:        1 ^ 2 ^   ^ 4 ^ 5
--------------------------------
Result:              3
"""