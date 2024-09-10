# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum is {add(num1, num2)}")
    print(f"The difference is {subtract(num1, num2)}")
