import sys, pyperclip, time

TEXT_STACK = []

copiedText = pyperclip.paste()
TEXT_STACK.append(copiedText)
print(f'Added {copiedText} \nin internal stack!')

if len(sys.argv) > 1:
    print('Usage: py mclip.py')
    sys.exit()

pyperclip.copy(TEXT_STACK.pop())