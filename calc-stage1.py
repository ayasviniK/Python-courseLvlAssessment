def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("float division by zero")
        return None

def power(a, b):
    return a ** b

def remainder(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        print("float division by zero")
        return None

#-------------------------------------


def select_op(choice):
    if choice == '#':
        return -1
    elif choice not in ['+', '-', '*', '/', '^', '%', '$']:
        print("Unrecognized operation")
        return 0
    elif choice == '$':
        return 0

    first = input("Enter first number: ")
    print(first)
    if '$' in first:
        return 0
    elif first == '#':
        print("Done. Terminating")
        exit()
    try:
        num1 = float(first)
    except ValueError:
        print("Not a valid number,please enter again")
        return 0

    second = input("Enter second number: ")
    print(second)
    if '$' in second:
        return 0
    elif second == '#':
        print("Done. Terminating")
        exit()
    try:
        num2 = float(second)
    except ValueError:
        print("Not a valid number,please enter again")
        return 0

    result = None
    if choice == '+':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '-':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '*':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '/':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    elif choice == '^':
        result = power(num1, num2)
        print(f"{num1} ^ {num2} = {result}")
    elif choice == '%':
        result = remainder(num1, num2)
        print(f"{num1} % {num2} = {result}")

    return 0




#End the select_op(choice) function here
#-------------------------------------

while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()