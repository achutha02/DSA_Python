arr = [5, 6, 5, 6, 9, 6]

hash_table = [0] * 10

for i in arr:
    hash_table[i] += 1

print(hash_table[6])
