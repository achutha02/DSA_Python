import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')


# 1st Condition where else is executed
for i in range(0,10):
    print("Hello World!")

else:
    print("The entire loop was completed\n")


#2nd condition where else is not executed
for i in range(0,10):
    print("Hello World")
    if i == 3:
        break

else:
    print("The entire loop was completed")
