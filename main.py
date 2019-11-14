import re


print("The Magical Calculator\n")
print("Type 'quit' to Exit\n")
print("Type new for New Equation\n")

previous = 0
run = True

def PerformMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        print("Goodbye ,Human.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+ equation)


while run:
    PerformMath()