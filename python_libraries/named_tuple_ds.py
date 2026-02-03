import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

val1 = (1, 4, 5)
val2 = (4, 1, 5)
val3 = (3, (6, 7, 9))
a, (b, c, d) = val3
print(a, b, c, d)


from collections import namedtuple

Point = namedtuple('Point', ['first', 'second'])
Nested = namedtuple('Nested', ['first', 'second'])
val = Point(7,9)
val0 = Nested(2, val)
print(val)
print(val.first)
print(val0)
print(val0.second.second)