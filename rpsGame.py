import random, sys

print("Rock, Papers, Scissors")

#Variables used to track the win, lose and tie of the game
win = 0
lose = 0
tie = 0

#Game loop
while True:

    #player move
    while True:
        print("Choose between (r)Rock, (p)Paper, (s)Scissors or (q)Quit")
        playerMove = input()

        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            #valid move
            break
        print("Please enter a valid input i.e either r, p, s")

    # Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what the computer chose:
    botMoveIdx = random.randint(1, 3)
    if botMoveIdx == 1:
        botMove = 'r'
        print('ROCK')
    elif botMoveIdx == 2:
        botMove = 'p'
        print('PAPER')
    elif botMoveIdx == 3:
        botMove = 's'
        print('SCISSORS')
    
    #Predice the outcome of the game

    if playerMove == botMove:
        tie+=1
    elif playerMove == 'r' and botMove == 's':
        win+=1
    elif playerMove == 'p' and botMove == 's':
        lose+=1
    elif playerMove == 'r' and botMove == 'p':
        lose+=1
    elif playerMove == 'p' and botMove == 'r':
        win+=1

    print("Win = ",win," Lose = ",lose," Tie = ",tie)
