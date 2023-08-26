# Flow control

print("Is it raining? ")
isRaining = input()
takeOutUmbrella = False
msg = ""
if isRaining == "yes":
    takeOutUmbrella = True
    msg = "It's raining let's take out the umbrella"
else:
    msg = "It's a sunny day. Let's go out!"
print(msg)

# Comparison Operators -- result in Boolean values

# == --> equality operator
# != --> not equal to operator
# >  --> greater than
# <  --> less than
# >= --> greater than or equal to 
# <= --> less than or equal to

# print(True != False)    # True
# print(True == True)     # True
# print(3 < 5)            # True
# print(5 > 2)            # True
# print(5 >= 5)           # True
# print(6 <= 1)           # False

# Binary Boolean

# and operator
#   True and True --> True
#   True and False --> False
#   False and True --> False
#   False and False --> False

# or operator
#   True or True --> True
#   True or False --> True
#   False or True --> True
#   False or False --> False

# not operator
#   not True --> False
#   not False --> True

# v1 = 5 > 1
# v2 = 10 % 5 == 0

# print(v1 and v2)
# print(not v1 and v2)

# print((5 > 2) or (10 < 4)) # print(True or False) --> True

## Elements of Flow Control

# 1. Conditions
# 2. Block of Code

print("Please enter your age...")
age = int(input())

if age < 18:
    print("You are not allowed to drive!")
elif age < 22:
    print("Do you have a driving license?")
    answer = input()
    if answer == "yes":
        print("Have a safe journey :)")
    else:
        print("Please apply for driving license!")
else:
    print("Have a safe journey :)")

# Loops

# while loop

# a = 1
# while a <= 10:
#     print(a)
#     a+=1

num = 0
while True:
    num+=1
    if num == 20:
        break
    
    if num % 2 == 1:
        print(num)
    else:
        continue


# for loop

# for i in range(21):
#     if i % 2 == 0:
#         print(i)

# for i in range(5, 21):
#     if i % 2 == 0:
#         print(i)

for i in range(0, 21, 5):
    # print("Index",i)
    if i % 2 == 0:
        print(i)

