n = int(input("Enter the number: "))
count = 0

if n == 0:
    print(1)

else:

    while(n > 0):
        n = n // 10
        count += 1

    print(count)