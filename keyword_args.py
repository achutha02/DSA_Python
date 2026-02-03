import sys

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

def print_details(name, age, college):
    print(f"name is {name}, age is {age}, college is {college}")

print_details(age=17, name="raj", college="SVCE")