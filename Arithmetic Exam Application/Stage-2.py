import random
lists_1 = [2, 3, 4, 5, 6, 7, 8, 9]
lists_2 = ['+', '-', '*']
a = random.choice(lists_1)
b = random.choice(lists_2)
c = random.choice(lists_1)
print(a,b,c)
Input = int(input())
Addition = 0
Subtraction = 0
Multiplication = 0

if b == "+":
    Addition = int(a) + int(c)
elif b == "-":
    Subtraction = int(a) - int(c)
elif b == '*':
    Multiplication = int(a) * int(c)

if Input == Addition:
    print("Right!")
elif Input == Subtraction:
    print("Right!")
elif Input == Multiplication:
    print("Right!")
else:
    print("Wrong!")
