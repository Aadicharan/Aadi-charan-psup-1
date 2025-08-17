a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case '+': print(f"Result: {a + b}")
    case '-': print(f"Result: {a - b}")
    case '*': print(f"Result: {a * b}")
    case '/':
        if b != 0:
            print(f"Result: {a / b}")
        else:
            print("Division by zero is not allowed.")
    case _: print("Invalid operator")
