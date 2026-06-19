nums1 = [-5, -2, 4, 5]
nums2 = [-3, 1, 8]

n = len(nums1)
m = len(nums2)

left = 0
right = 0
index = 0

merged = [0] * (m+n)

while left < n and right < m:
    if nums1[left] < nums2[right]:
        merged[index] = nums1[left]
        left += 1
    else:
        merged[index] = nums2[right]
        right += 1
    index += 1

while left < n:
    merged[index] = nums1[left]
    left += 1
    index += 1

while right < m:
    merged[index] = nums2[right]
    right += 1
    index += 1


print(merged)