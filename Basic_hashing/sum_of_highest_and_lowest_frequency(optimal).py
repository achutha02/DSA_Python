arr = [1, 2, 2, 3, 3, 3]

n = len(arr)

max_freq = 0
min_freq = n

mpp = {}

for ar in arr:
    if ar in mpp:
        mpp[ar] += 1
    
    else:
        mpp[ar] = 1

for freq in mpp.values():
    max_freq = max(max_freq, freq)
    min_freq = min(min_freq, freq)

print(max_freq + min_freq)