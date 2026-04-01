nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = [2, 3, 4, 4, 5, 11, 12]

union = []

i = 0
j = 0

n = len(nums1)
m = len(nums2)

while i < n and j < m:
    if nums1[i] <= nums2[j]:
        if not union or union[-1] != nums1[i]:
            union.append(nums1[i])
        i += 1
    
    else:
        if not union or union[-1] != nums2[j]:
            union.append(nums2[j])
        j += 1

while i < n:
    if not union or union[-1] != nums1[i]:
        union.append(nums1[i])
    
    i += 1

while j < m:
    if not union or union[-1] != nums2[j]:
        union.append(nums2[j])
    j += 1

print(union)



"""
Time Complexity: O(M+N), because both the arrays must be traversed once.

Space Complexity: O(M+N), considering the space for returning the output, which in the worst case, can contain all the elements from both arrays
"""