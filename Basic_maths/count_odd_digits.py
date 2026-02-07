n = int(input("Enter your number: "))

countOdd = 0

while n > 0:
    lastDigit = n % 10
    if lastDigit % 2 == 1:
        countOdd += 1
    
    n = n // 10

print(countOdd)