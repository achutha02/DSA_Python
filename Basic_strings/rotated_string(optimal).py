s = "abcde"
goal = "cdeab"

is_rotated = False

if len(s) != len(goal):
   is_rotated =  False

double_s = s + s

if goal in double_s:
   print("Yes, the given string can be rotated")

else:
   print("No, the string cannot be rotated")