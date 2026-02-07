n = int(input("Enter your number: "))

duplicate = n
reverseNum = 0

while n > 0:
    lastDigit = n % 10
    reverseNum = (reverseNum * 10) + lastDigit

    n = n // 10

if(reverseNum == duplicate):
    print("The number is palindrome")

else:
    print("The number is not palindrome")
