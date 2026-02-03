import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

arr = [1,5,6,7,4]
print(sorted(arr)) # returns a new sorted list

print(sorted(arr, reverse=True))

print(arr)

arr.sort() # Original list is sorted
print(arr)

arr2 = [-1,5,-6,7,4]
print(sorted(arr2, key=lambda x: abs(x))) # sorting based on absolute values

fruits_list = ["apple", "pineapple", "kiwi"]
print(sorted(fruits_list, key = len)) # sorted based on length
print(sorted(fruits_list, reverse=True, key=len))



arr3 = [-15,6,8,7]
print(min(arr3))
print(max(arr3))
print(max(arr3, key=lambda x: abs(x)))

fruits_list1 = ["apple", "pineapple", "kiwi"]
print(max(fruits_list1))

print(sum(arr3))
print(sum(arr3, start=10))


arr4 = [True, False, True]
print(any(arr4)) # Any of the value in list should be True which returns True
print(all(arr4)) # All values in list should be True returns True else returns False

arr5 = [1,2,1,6,7]
print(arr5.count(1)) # Returns number of occurrences of an element in the list

arr6 = [5,6,1,3]
print(list(enumerate(arr6))) # (index, value)
print(list(reversed(arr6)))

arr7 = list(range(2,15,3))
print(arr7)