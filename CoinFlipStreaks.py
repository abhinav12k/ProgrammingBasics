import random

numberOfStreak = 0

for experimentNumber in range(10000):

    print("Please wait while we toss the coin 100 times")
    coinOutcomes = []
    for i in range(100):
        outcome = ''
        if random.randint(0,1) == 0:
            outcome = 'T'
        else:
            outcome = 'H'
        coinOutcomes.append(outcome)

    print(coinOutcomes)

    consecutiveCt = 1
    for idx in range(1,len(coinOutcomes)):
        if consecutiveCt == 6:
            numberOfStreak+=1
            consecutiveCt = 0
        if coinOutcomes[idx-1] == coinOutcomes[idx]:
            consecutiveCt+=1
        else:
            consecutiveCt = 0

print("Chance of streak: %s%%" % (numberOfStreak/100))
