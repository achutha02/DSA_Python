s = "504"

ind = -1

n = len(s)

for i in range(n - 1, -1, -1):
    if (int(s[i]) % 2) == 1:
        ind = i
        break

i = 0
while i <= ind and s[i] == '0':
    i = i + 1

print(s[i: ind + 1])
