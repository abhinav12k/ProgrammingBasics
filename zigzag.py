import time, sys

intent = 0
intentIncreasing = True

try:
    while True:

        print(' ' * intent, end='')
        print("********")
        time.sleep(.1)
        
        if intentIncreasing:
            intent += 1
            if intent == 20:
                intentIncreasing = False
        else:
            intent -= 1
            if intent == 0:
                intentIncreasing = True
except KeyboardInterrupt:
    sys.exit()