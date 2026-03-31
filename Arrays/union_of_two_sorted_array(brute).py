nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]

s = set()

Union = []

for num in nums1:
    s.add(num)

for num in nums2:
    s.add(num)

s1 = sorted(s)

for num in s1:
    Union.append(num)

print(Union)