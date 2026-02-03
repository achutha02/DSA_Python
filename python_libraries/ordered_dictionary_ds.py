import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')


from collections import OrderedDict

od = OrderedDict([(1, "raj"), (3, "striver"), (2, "tuf"), (7, "msd")])
print(od)
print(od[1])

# print(od[10]) # Throws error like normal dictionary

if 10 in od:
    print(od[10])
else:
    print("not in dictionary")

od[10] = "messi"
od.move_to_end(1)
print(od)

od.move_to_end(10, last=False) # last will come to first by default last is True
print(od)

print(od.popitem())
print(od)

print(od.pop(7)) # The particular key value pair is popped out
print(od)