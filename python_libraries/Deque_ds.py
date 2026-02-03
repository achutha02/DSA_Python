import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

from collections import deque

dq = deque([2, 3, 1])
dq.append(5)
print(dq)


dq.appendleft(7)
print(dq)


print(dq.pop())
print(dq)

print(dq.popleft())
print(dq)

dq.extend([10,19])
print(dq)


dq.extendleft([89,70])
print(dq)

dq.rotate(2)
print(dq)

dq.rotate(7) # If Deque is rotated exactly equal to length of Deque it returns same Deque
print(dq)

