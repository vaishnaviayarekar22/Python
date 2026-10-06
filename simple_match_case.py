# Simple match-case example in Python

choice = int(input("Enter a number (1-3): "))

match choice:
    case 1:
        print("You selected Apple")
    case 2:
        print("You selected Banana")
    case 3:
        print("You selected Mango")
    case _:
        print("Invalid choice")
