import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

from collections import defaultdict

dd = defaultdict(int)
dd[1] = "raj"
dd["striver"] = "striver"
dd['u'] = 99
dd["list"] = [1, 2, 4]

print(dd["zyc"])


dd2 = defaultdict(list)
dd2["raj"] = [7, 8, 9]
dd2["raj"].append(10)

print(dd2["raj"])
