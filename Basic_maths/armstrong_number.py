import math

n = int(input("Enter your number: "))
duplicate = n

sum = 0
count = int(math.log10(n)) + 1

while n > 0:
    lastDigit = n % 10

    sum = sum + lastDigit ** count

    n = n // 10

if(sum == duplicate):
    print("Number is armstrong")

else:
    print("The number is not armstrong")

