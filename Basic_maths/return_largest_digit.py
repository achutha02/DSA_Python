n = int(input("Enter your number: "))

largest = 0

while n > 0:
    lastDigit = n % 10
    if lastDigit > largest:
        largest = lastDigit
    
    n = n // 10

print(largest)