import sys
import bisect

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

arr = [4, 5, 5, 6, 7, 7, 9, 10, 12, 12, 13]

print(bisect.bisect_left(arr, 5)) # Return the index where to insert item x in list a, assuming a is sorted.

print(bisect.bisect_right(arr, 5)) # Return the index where to insert item x in list a, assuming a is sorted (rightmost index).

print(bisect.bisect_right(arr, 5)) # Same as bisect_right

bisect.insort(arr, 5) # Inserts value to the rightmost assuming array is sorted

bisect.insort_right(arr, 5) # Same as insort

bisect.insort_left(arr, 6) # Inserts value to the leftmost assuming array is sorted