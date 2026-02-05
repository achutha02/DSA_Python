import sys
import heapq

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

val = []
heapq.heappush(val, 10)
heapq.heappush(val, 7)
heapq.heappush(val, 9)
heapq.heappush(val, 19)
heapq.heappush(val, 12)
heapq.heappush(val, 1)
print(val)
heapq.heappop(val) # Always the smallest element is removed which is at first and rearranges itself to keep the next smallest element at first
print(val)
heapq.heappushpop(val, 4) # First the element is pushed and smallest element is popped out
heapq.heapreplace(val, 29) # First the smallest element is popped and then the element is pushed in


print(heapq.nlargest(4, [7, 1, 5, 3, 10])) # Returns the largest numbers from given iterable in this case it is given 4 largest

print(heapq.nsmallest(3, [7,1,5,3,10])) # Same as nlargest but returns smallest numbers



arr = [7,8,2,1,-16,6]
val2 = []

for items in arr:
    heapq.heappush(val2, items)

print(val2)


# Instead of the above looping and inserting into new heap

heapq.heapify(arr)
print(arr)



## MAX HEAP
arr2 = [6, 7, 8, 9, 10]
pq =[]
for items in arr2:
    heapq.heappush(pq, -1 * items) # First negate the elements then smallest will come first

print(-1 * pq[0]) # Second negate and print the first element which gives largest