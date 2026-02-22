s = "anagram"
t = "nagaram"

if len(s) == len(t) and sorted(s) == sorted(t):
    print("Yes, they are anagram")

else:
    print("No, they are not anagram")