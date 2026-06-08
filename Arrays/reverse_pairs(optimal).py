def merge(arr, low, mid, high):

    left = low
    right = mid + 1

    temp = []

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    for i in range(low, high+1):
        arr[i] = temp[i-low]


def countPairs(arr, low, mid, high):
    right = mid + 1
    cnt = 0

    for i in range(low, mid+1):
        while right <= high and arr[i] > 2 * arr[right]:
            right += 1

        cnt += right - (mid + 1)
    
    return cnt



def mergeSort(arr, low, high):
    if low >= high:
        return 0
    
    mid = (low + high) // 2

    cnt = 0

    cnt += mergeSort(arr, low, mid)

    cnt += mergeSort(arr, mid+1, high)

    cnt += countPairs(arr, low, mid, high)

    merge(arr, low, mid, high)

    return cnt

nums = [6, 4, 1, 2, 7]

n = len(nums)

print(mergeSort(nums, 0, n-1))




"""
Time Complexity: O(2N * logN), where N is size of the given array.
--> Inside the mergeSort() we call merge() and countPairs() except mergeSort() itself. Now, inside the function countPairs(), though we are running a nested loop, we are actually iterating the left half once and the right half once in total.
--> That is why, the time complexity is O(N). And the merge() function also takes O(N). The mergeSort() takes O(logN) time complexity. Therefore, the overall time complexity will be O(logN x (N+N)) = O(2NxlogN).


Space Complexity: O(N), as in the merge sort, a temporary array to store elements in sorted order is used.
"""
