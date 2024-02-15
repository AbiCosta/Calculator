def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    while True:
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == '+':
                print("Result:", add(num1, num2))
            elif operation == '-':
                print("Result:", subtract(num1, num2))
            elif operation == '*':
                print("Result:", multiply(num1, num2))
            elif operation == '/':
                print("Result:", divide(num1, num2))
            else:
                print("Invalid operation!")
            
            choice = input("Do you want to perform another calculation? (yes/no): ")
            if choice.lower() != 'yes':
                print("Thank You for Using the Calculator!!!")
                break
        except ValueError as ve:
            print("Error:", ve)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    calculator()
