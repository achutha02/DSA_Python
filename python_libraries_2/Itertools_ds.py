import sys
import itertools

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

arr = [1, 5, 6, 7]

print(list(itertools.combinations(arr, 2))) # Return successive r-length combinations of elements in the iterable.

print(list(itertools.combinations_with_replacement(arr, 2))) # Return successive r-length combinations of elements in the iterable allowing individual elements to have successive repeats.

print(list(itertools.permutations(arr, 2))) # Return successive r-length permutations of elements in the iterable.


arr1 = [1, 2]
arr2 = [3, 4]
arr3 = [5, 6]
print(list(itertools.product(arr1, arr2, arr3)))

arr4 = [1, 2, 4]
# print(list(itertools.cycle(arr4))) # Prints the same numbers infinitely in a list

arr5 = list(itertools.repeat(5, 6)) # Prints number 5 for 6 times in a list
print(arr5)

print(list(itertools.chain([1, 2], [5, 6], [3, 4]))) # Chains all elements into a single list

arr6 = [1, 3, 6, 10]
print(list(itertools.accumulate(arr6))) # Returns a cummulative sum till that index

print(list(itertools.accumulate(arr6, lambda x, y: x * y))) # Returns a cummulative product till that index