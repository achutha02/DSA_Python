s = ["h", "e", "l", "l", "o"]

n = len(s)

left = 0
right = n-1

while left < right:
    temp = s[left]
    s[left] = s[right]
    s[right] = temp
    left += 1
    right -= 1


print(s)



"""The swapping logic can also be implemented as

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

"""

