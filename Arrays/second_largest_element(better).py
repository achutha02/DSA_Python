arr = [1, 2, 4, 7, 7, 5]

n = len(arr)

largest = arr[0]

secondLargest = -1

for i in range(n):
    if arr[i] > largest:
        largest = arr[i]

for i in range(n):
    if arr[i] > secondLargest and arr[i] != largest:
        secondLargest = arr[i]

print(secondLargest)