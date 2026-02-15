arr = [1, 2, 3, 4, 5, 7]

count = 0

for i in arr:
    if i % 2 != 0:
        count = count + 1

print(f"The number of odd numbers are:{count}")