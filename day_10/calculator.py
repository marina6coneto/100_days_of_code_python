from art import logo

# Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    print(logo)
    num1 = float(input('What is the first number? '))

    for symbol in operations:
        print(symbol)  
    
    should_continue = True

    while should_continue:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What is the next number? '))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')
        
        to_continue = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'q' to quit the calculator: ").strip().lower()
        if to_continue == 'y':
            num1 = answer
        elif to_continue == 'n':
            should_continue = False
        elif to_continue == 'q':
            should_continue = False
            global start_calculator
            start_calculator = False



start_calculator = True

while start_calculator:
    calculator()

print("Goodbye!")
