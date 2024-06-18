def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return a ** 0.5

def factorial(a):
    if a < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if a == 0:
        return 1
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

def main():
    print("Scientific Calculator")
    print("Operations: +, -, *, /, **, sqrt, fact")

    while True:
        operation = input("Enter operation (or 'quit' to exit): ").strip().lower()
        if operation == 'quit':
            break

        if operation in {'+', '-', '*', '/', '**'}:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if operation == '+':
                    result = add(a, b)
                elif operation == '-':
                    result = subtract(a, b)
                elif operation == '*':
                    result = multiply(a, b)
                elif operation == '/':
                    result = divide(a, b)
                elif operation == '**':
                    result = power(a, b)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif operation == 'sqrt':
            try:
                a = float(input("Enter number: "))
                result = sqrt(a)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

        elif operation == 'fact':
            try:
                a = int(input("Enter number: "))
                result = factorial(a)
                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

        else:
            print("Invalid operation")

if __name__ == "__main__":
    main()
