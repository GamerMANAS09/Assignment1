while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    ch = input("Enter choice +, -, *, / to exit press 0: ")

    if ch == '+':
        print(a + b)
    elif ch == '-':
        print(a - b)
    elif ch == '*':
        print(a * b)
    elif ch == '/':
        if b != 0:
            print(a / b)
        else:
            print('Zero Error!!!!')
    elif ch == '0':
        print("Exiting the program")
        break
    else:
        print("Invalid operation")
