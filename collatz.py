import sys

def collatz(number):
    print(number)
    if number == 1: 
        print("Reached Destination")
    elif number % 2 == 0:
        collatz(number // 2)
    else:
        collatz(3*number + 1)

while True:
    try:
        print("Enter any number!")
        userInput = int(input())
        collatz(userInput)
    except ValueError:
        print("Please enter a valid number!")
    except KeyboardInterrupt:
        print("Exiting Program")
        sys.exit()