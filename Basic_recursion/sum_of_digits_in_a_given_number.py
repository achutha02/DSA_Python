"""Given an integer num, repeatedly add all its digits until the result has only one digit, and return it."""

def addDigits(num):
    if num < 10:
        return num
    
    sum_digit = sumDigit(num)

    return addDigits(sum_digit)

def sumDigit(num):
    if num == 0:
        return 0
    
    return sumDigit(num // 10) + (num % 10)

num = 529
print(addDigits(num))