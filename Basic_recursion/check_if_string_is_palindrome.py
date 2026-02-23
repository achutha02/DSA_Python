def palindrome(s):
    return isPalindrome(s, 0, len(s) - 1)

def isPalindrome(s: str, left: int, right: int) -> bool:
    if left >= right:
        return True
    
    if s[left] != s[right]:
        return False
    
    return isPalindrome(s, left+1, right-1)

s = "hannah"
print(palindrome(s))