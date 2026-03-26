s = "abcde"
goal = "cdeab"

n = len(s)
m = len(goal)

is_rotated = False

for i in range(n):
    if n != m:
        break

    rotated = s[i:] + s[:i]

    if rotated == goal:
        is_rotated = True

if is_rotated:
    print("Goal found")

else:
    print("Not found")





