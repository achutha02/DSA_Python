def reverseString(s):
    reverse(s, 0, len(s) - 1)
    return s

def reverse(s, left, right):
    if left >= right:
        return
    
    s[left], s[right] = s[right], s[left]
    return reverse(s, left+1, right-1)

s = ["h","e","l","l","o"]
print(reverseString(s))