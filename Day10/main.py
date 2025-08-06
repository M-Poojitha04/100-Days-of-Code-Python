import art
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

calc_dict = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
def calculator():
    print(art.logo)
    number1 = float(input("What's the first number: "))
    continue_calculation = True
    while continue_calculation:
        for key in calc_dict:
            print(key)
        operation = input("Pick an operation: ")
        number2 = float(input("What's the next number: "))
        output = calc_dict[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {output}")
        continue_calculation = input(f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
        if continue_calculation == 'y':
            number1 = output
            continue_calculation = True
        else:
            continue_calculation = False
            print("\n" * 20)
            calculator()
calculator()