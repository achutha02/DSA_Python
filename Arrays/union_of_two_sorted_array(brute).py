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


"""
Time Complexity: O( (M+N)log(M+N) ), at max set can store M+N elements {when there are no common elements and elements in nums1 , nums2 are distntict}. So Inserting M+N th element takes log(M+N) time. Upon approximation across inserting all elements in worst, it would take O((M+N)log(M+N) time.

Space Complexity: O(M+N), considering space of Union Array.
"""