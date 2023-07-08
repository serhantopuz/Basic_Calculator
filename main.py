from functions import *

while_true = True
with_same_number = False
result = 0

print("""
Functions of the Calculator:

1) Addition
2) Subtraction
3) Multiplication
4) Division""")

while while_true:
    choice = int(input("\nPick the function you want to use by the number: "))
    if with_same_number:
        number1 = result
        number2 = int(input("Enter the new Number to keep calculate: "))
    else:
        number1, number2 = input("Enter two Numbers you want to use: ").split()

    if choice == 1:
        result = add(number1, number2)
        print(f"The Result is: {result}\n")
    elif choice == 2:
        result = sub(number1, number2)
        print(f"The Result is: {result}\n")
    elif choice == 3:
        result = multi(number1, number2)
        print(f"The Result is: {result}\n")
    else:
        result = div(number1, number2)
        print(f"The Result is: {result}\n")

    keep_use = input("Do you want to keep using the calculator(Y/N): ").lower()

    if keep_use == "n":
        while_true = False
        break

    with_same_result = input("Do you want to keep using the same number(Y/N): ").lower()

    if with_same_result == "y":
        with_same_number = True
    else:
        with_same_number = False

