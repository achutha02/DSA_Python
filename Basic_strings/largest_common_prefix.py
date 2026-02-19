str = ["flowers" , "flow" , "fly", "flight" ]

if not str:
    print("Empty string")

ans = []

str.sort()

first = str[0]
last = str[-1]

for i in range(min(len(first), len(last))):
    if first[i] != last[i]:
        break
    ans.append(first[i])

print(''.join(ans))