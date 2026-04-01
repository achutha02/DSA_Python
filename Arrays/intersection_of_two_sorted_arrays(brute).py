nums1 = [1, 2, 2, 3, 3, 3]
nums2 = [2, 3, 3, 4, 5, 7]

ans_list = []

visited = [0] * len(nums2)

i = 0
j = 0

while i < len(nums1):
    while j < len(nums2):
        if nums1[i] == nums2[j] and visited[j] == 0:
            ans_list.append(nums2[j])
            visited[j] = 1
            break

        elif nums2[j] > nums1[i]:
            break
        j += 1
    
    i += 1

print(ans_list)



"""
Time Complexity: O(MxN), where M is the length of nums1 and N is the length of nums2.

Space Complexity: O(N), where N is size of nums2, extra space to store answer is not considered.
"""