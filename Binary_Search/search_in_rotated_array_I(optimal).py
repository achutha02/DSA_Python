nums = [4, 5, 6, 7, 0, 1, 2]

target = 0

n = len(nums)

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        print(mid)
        break

    if nums[low] <= nums[mid]:
        if nums[low] <= target <= nums[mid]:
            high = mid - 1

        else:
            low = mid + 1

    else:
        if nums[mid] <= target <= nums[high]:
            low = mid + 1

        else:
            high = mid - 1

else:
    print(-1)




#                     [low ... mid ... high]
#                             |
#               is nums[low] <= nums[mid]?
#                     /                \
#                  YES                  NO
#                   |                    |
#         left half is sorted    right half is sorted
#                   |                    |
#       check: nums[low]<=target<=nums[mid]   check: nums[mid]<=target<=nums[high]
#         /              \                      /              \
#      YES               NO                  YES               NO
#       |                 |                    |                 |
#  search left      search right          search right      search left
#  (high=mid-1)     (low=mid+1)           (low=mid+1)        (high=mid-1)






"""
Time Complexity: O(logN), as the search space is reduced logarithmically, where N is the size of the given array.

Space Complexity: O(1), not using any extra data structure.
"""