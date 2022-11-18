# to save to github use these commands
# git add .
# git commit -m "added day 1 file"
# git push


# this code will print bye 
# print("bye")

# python3 day_1.py
# print("Hello World!")

# exercise 1 print three seperate lines the same like this
# print("Day 1 - Python Print Function")
# print("The function is declared like this:")
# print("print('what to print')")

# print("Hello world!\nHello world!")
# print('print("what to print")')

# This code will print HelloChelsea
# print("Hello" + "Chelsea")
# This code has a space after Hello which will print Hello Chelsea
# print("Hello " + "Chelsea")
# This has a space before Chelea which prints Hello Chelsea
# print("Hello" + " Chelsea")
# This code adds a seperate string for the space
# print("Hello" + " " + "Chelsea")


# exercise 2 debugging
# print("Day 1 - String Manipulation")
# When double quotes are in the function, single quotes relace where the double quotes usually go
# print('String Concatenation is done with the "+" sign.')
# print('e.g. print("Hello " + "world")')
# print("New lines can be created with a backslash and n.")


# exercise 3 - Input Function
# this code will print the prompt for the user to respond
# input("What is your name?")
# inserting the input function in to the print function will run the program to respond Hello Chelsea
# print("Hello " + input("What is your name?") )

# len() tells it to print the length of the name input to the prompt
# this code has 3 functions
# print( len( input("What is your name?")))

# notes 
# use thonny.org application to break down the code to understand

# the function is assigned to a variable
# name = input("What is your name?")
# the length function being variable name for short is assigned to this variable
# Length = len(name)
# this code will print whatever function is assigned to the variable in ()
# print(Length)


# excercise 4 - Variables
# variables are assigned inputs here
# a = input("a:")
# b = input("b:")

# used a 3rd variable to hold the first variables value (a) 
# c = a
# a = b
# b = c

# using print function to output the results using concatenation
# print("a = " + a)
# print("b = " + b)


# Day 1 Project - Band Name Generator

#1. Create a greeting for your program.
# print("Let's come up with a name for your band!")
#2. Ask the user for the city that they grew up in.
# gave a name to hold the value the user answers with \n at the end to allow the user to input on the next line
# city = input("Which city did you grow up in?\n")
#3. Ask the user for the name of a pet.
# pet = input("What is the name of your pet?\n" ) 
#4. Combine the name of their city and pet and show them their band name.
# print("Your band name is " + city + " " + pet)
#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end


# Data Types

# String

# subscripting
# subscripting in this code will print letter that the number represents
# print("Hello"[0])
# print("Hello"[4])

# Integer
# whole numbers in code

# this code will add the numbers
# print(123 + 345)

# Float
# floating point number
# numbers with decimals data type
# 3.14159

# Boolean

True
False
# this code gives an integer
# num_char = len(input("What is your name?"))
# this code breaks becasue the string does not have all the same data type
# print("Your name has " + num_char + " characters.")

# the type function will tell me the data type im using
# print(type(num_char))

# type conversion- to convert a data type
# new_num(_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

# this gives the int data type
# a = 123
# print(type(a))

# this gives the str data type
# a = str(123)
# print(type(a))

# this gives the float data type
# a = float(123)
# print(type(a))

# used the float function to convert
# print(70 + float("100.5"))

# used the str funtion to convert
# print(str(70)+str(100))




