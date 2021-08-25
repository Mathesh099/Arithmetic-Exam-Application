Inputs = input()
a, b, c = Inputs.split(" ")
if b == "+":
    print(int(a) + int(c))
elif b == "-":
    print(int(a) - int(c))
elif b == '*':
    print(int(a) * int(c))


