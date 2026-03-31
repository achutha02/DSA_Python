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
