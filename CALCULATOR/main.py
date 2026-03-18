#----------CALCULATOR-----------

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



operations = {
    "*" : multiply,
    "/" : divide,
    "+" : add,
    "-" : subtract
    
}

def calculator():

    num1 = float(input("what's the 1st number?: "))

    for sign in operations:
        print(sign)
        
    should_continue = True
    while should_continue:
                
        op_sign = input("Pick an opration from the line above: ")
        num2 = float(input("what is the 2nd number?: "))

        calculation_function = operations[op_sign]
        answer = calculation_function(num1, num2)


        print(f"{num1} {op_sign} {num2} = {answer}")    

        if input(f"Type 'y' to continue calculating with {answer}: or type 'n' to start new calculation  ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()

