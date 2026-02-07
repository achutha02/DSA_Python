n = int(input("Enter your number: "))

reverseNum = 0

while n > 0:
    lastDigit = n % 10
    reverseNum = (reverseNum*10) + lastDigit

    n = n // 10

print(reverseNum)