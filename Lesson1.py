## Basics 
# Expressions
# Evaluating an expression
# Variables
# Using variables
# Taking input from the user

#Expression --> Anything whose value can be evaluated

#Exp1 -
# print(1 + 2 + 3)

# 1 --> Operand --> On which operation is being performed
# + --> Operator ---> Addition operator

# Operators 
# 1. ** --> Exponent --> 2^5 = 32
# 2. %  --> Modulus / Remainder  --> 7/2 = 1
# 3. // --> Integer divison --> 7/2 = 3.5 --> 3
# 4. /  --> Divison --> 7/2 = 3.5
# 5. *  --> Multiplication --> 3*8 = 24
# 6. +  --> Addition --> 45+5 = 50
# 7. -  --> Subtraction --> 50-23 = 27

# BODMAS --> Bracket Open Division Multiplication Addition Subtraction

# Variables
# a place where you can keep your evaluated expression. The data get's stored inside the memory (RAM)

# Python is a dynamically typed language that means the type of a variable can be changed at runtime
# a = 532
# print(a, type(a))

# a = "124"
# print(a, type(a))

##############################

# var1 = 13
# var2 = 4
# addition = var1 + var2
# subtraction = var1 - var2
# mutliplication = var1 * var2
# division = var1 / var2
# integerDiv = var1 // var2
# remainder = var1 % var2

# print("Addition - ",addition)
# print("Subtraction - ",subtraction)
# print("Mutiplication - ", mutliplication)
# print("Division - ", division)
# print("IntegerDivision - ", integerDiv)
# print("Remainder - ", remainder)

# exp = 5*(5*2-10*-1)//2 # 5 *(10+10)/2 --> 5*(20)/2 --> 5(10) --> 50
# print(exp)

# name = "Joseph"
# print("Hi ", name*5)

# name = "Tom" + "Jerry"
# name += "Jerry"
# print(name)

################################
# Input from the command line or terminal is always in the form of a string. If you want to perfrom some integer operation on that you need to first convert that string into
# a integer.


print("Hi there!, What's your name?")
name = input()
print("My name is ",name)

print("What is your age?")
age = input()
print("You will be "+str(int(age) + 1) + ' in a year.')