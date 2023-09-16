import random

answer = random.randint(1,21)
print("Guess the number between 1 and 20")

for guessTaken in range(1,6):
    print("Make a guess")
    guessedNum = int(input())

    if guessedNum < answer:
        print("Guessed value is lower than expected")
    elif guessedNum > answer:
        print("Guessed value is greater than the expected value")
    else:
        break

if guessedNum == answer:
    print("You got it right!")
else:
    print('Nope. The number I was thinking of was ' + str(answer))