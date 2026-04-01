nums1 = [1, 2, 2, 3, 3, 3]
nums2 = [2, 3, 3, 4, 5, 7]

i = 0
j = 0

ans_list = []

while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
        i += 1
    elif nums2[j] < nums1[i]:
        j += 1
    
    else:
        ans_list.append(nums1[i])
        i += 1
        j += 1

print(ans_list)




"""
Time Complexity: O(M+N), where M and N are the lengths of the given arrays.
This is because both the arrays are traversed once.

Space Complexity: O(min(m, n)), extra space to store answer is not considered. worst case it can be O(N)
"""
