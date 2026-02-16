arr = [1, 2, 3, 4, 5]

n = len(arr)

is_sorted = True

for i in range(n-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("The array is sorted")

else:
    print("The array is not sorted")