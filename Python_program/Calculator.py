# Importing libraries
import sys
import ctypes

# defining the methods
def addition(numa, numb):
    result = numa + numb
    print(result)

def subtraction(numa, numb):
    result = numa + numb
    print(result)


def multiplication(numa, numb):
    result = numa * numb
    print(result)


def division(numa, numb):
    result = numa / numb
    print(result)


def main():
    print("Welcome to the calculator!")
    numa = input("What is your first Number?")
    numb = input("what is your second Number?")

    choice = input("""What operation would you like to complete?
                   Press + for Addition
                   Press - for Subtraction
                   Press * for Multiplication
                   Press / for Division
                   Press Q to quit""")
    # Creating the if statement
    if choice == "+":
        addition()
    elif choice =="-":
        subtraction()
    elif choice =="*":
        multiplication()
    elif choice =="/":
        division()
    elif choice =="Q" or "q":
        sys.exit()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Please select an option on the menu", "*****ERROR*****")


