import random
mark = 0
Input = 0
for _ in range(5):
    operations = [" + ", " - ", " * "]
    question = str(random.randint(2, 9)) + random.choice(operations) + str(random.randint(2, 9))
    print(question)
    while True:
        try:
            Input = int(input())
            if Input == eval(question):
                print("Right!")
                mark += 1
            else:
                print("Wrong!")
            break
        except ValueError:
            print("Incorrect format.")
            continue
print("Your mark is {}/5.".format(mark))
