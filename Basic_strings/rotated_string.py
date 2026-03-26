s = "abcde"
goal = "cdeab"

n = len(s)
m = len(goal)

is_rotated = False

if n != m:
    print("No, string cannot be rotated")

else:
    for i in range(n):

        rotated = s[i:] + s[:i]
        if rotated == goal:
            is_rotated = True

    if is_rotated:
        print("Yes, the string can be rotated")

    else:
        print("No, string cannot be rotated")