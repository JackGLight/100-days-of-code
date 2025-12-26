'''
Calculator app for addition, subtraction, multiplication, division
'''

continue_calc = "n"
answer = 0
num_1 = 0
num_2 = 1


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operator():
    valid_operators = ("+", "-", "*", "/")
    
    while True:
        operator = input(
            """Which operation?
+
-
*
/
"""
        ).strip()
        
        if operator in valid_operators:
            return operator
        print("Please choose a valid operator (+, -, *, /).")



def addition(num_1, num_2):
    result = num_1 + num_2
    return result

def subtraction(num_1, num_2):
    result = num_1 - num_2
    return result

def multiplication(num_1, num_2):
    result = num_1 * num_2
    return result

def division(num_1, num_2):
    result = num_1 / num_2
    return result



print("Welcome to the calculator app!")

while True:

    if continue_calc == "y":
        num_1 = answer
    else:
        num_1 = get_number("What is your first number?\n")

    operator = get_operator()


    while True:
        num_2 = get_number("What is your second number?\n")
        if operator == "/" and num_2 == 0:
            print("You cannot divide by zero. Please enter a different number.")
        else:
            break

    if operator == "+":
        answer = addition(num_1, num_2)
    elif operator == "-":
        answer = subtraction(num_1, num_2)
    elif operator == "*":
        answer = multiplication(num_1, num_2)
    elif operator == "/":
        answer = division(num_1, num_2)

    print(f"The answer is: {answer}\n")
    continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:\n")