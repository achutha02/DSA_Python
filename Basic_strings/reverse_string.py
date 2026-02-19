s = ["h", "e", "l", "l", "o"]

n = len(s)

stack = []

for c in s:
    stack.append(c)

for i in range(n):
    s[i] = stack.pop()

print(s)
