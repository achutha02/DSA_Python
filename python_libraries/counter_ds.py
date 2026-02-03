import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

from collections import Counter

arr = Counter([1, 2, 2, 3, 2, 3, 3, 4]) # 1 -> 1, 2 -> 3, 3 -> 3, 4 -> 1
print(arr[2])

print(arr.most_common(1))

print(arr.most_common(2))

print(list(arr.elements())) # Returns elements in insertion order and the elements of same type
arr.update([7, 3, 4])
print(list(arr.elements()))

arr.subtract([4])
print(list(arr.elements()))

c2 = Counter([3, 3, 1, 4, 5]) # 3 -> 2, 1 -> 1, 4 -> 1, 5 -> 1

c3 = arr - c2
print(list(c3.elements()))

c4 = c2 - arr
print(list(c4.elements()))

c5 = arr + c2
print(list(c5.elements()))

c6 = arr & c2 # Intersection of arr and c2
print(list(c6.elements()))

c7 = arr | c2
print(list(c7.elements()))