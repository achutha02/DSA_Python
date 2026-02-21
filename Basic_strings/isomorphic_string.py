s = "apple"
t = "bbnbm"

n = min(len(s), len(t))

m1 = [0] * 256
m2 = [0] * 256

is_isomorphic = True

for i in range(n):
    if m1[ord(s[i])] != m2[ord(t[i])]:
        is_isomorphic = False
        break
    m1[ord(s[i])] = i+1
    m2[ord(t[i])] = i+1

if is_isomorphic:
    print("The strings are isomorphic")

else:
    print("The Strings are not isomorphic")