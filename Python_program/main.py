# Importing libs
import ctypes
import sys


# Functions for the main to call upon
def main():
    menu()


def snake():
    import Snake


def ball():
    import Ball

def calculator():
    pass


def menu():
    print("Welcome to this program, what is it that you would like to do?")
    print()
    # this is where the menu starts
    choice = input("""
                     A: Calculator
                     B: Snake
                     C: Magic 8 ball
                     Q: exit
                     
                     Please enter your choice using the keyboard
                    """)
    choice = choice.upper()
    # Start of the if statement used for the menu, also scanning for input
    if choice == "A":
        calculator()
    elif choice == "B":
        snake()
    elif choice == "C":
        ball()
    elif choice == "Q":
        print("Exiting program!!")
        sys.exit()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Please select an option on the menu", "*****ERROR*****")
        menu()


# Execute the program
main()
