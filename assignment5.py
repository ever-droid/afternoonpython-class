# 1. Write a program that prompts
# a user to enter number checks
# whether a number is prime or not

# 2. A program that allows you to enter an alphabet
# and returns the alphabet as
# either a vowel or a constant

# 3. Write your own program to demonstrate the concept of inheritance in python

number= int(input("Enter a number:"))
if number == 3 or number == 5 or number == 7 or number == 11 or number == 13:
    print("This is a prime number")
else:
    print("This is not a prime number")

letter = input("This is a letter:")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" :
    print("This is a vowel")
else:
    print("This is a constant")

class Animal:
    def __init__(self,name,hasscales):
        self.name = name
        self.hasscales = hasscales

    def movement(self):
        print(self.name, "Moves by galloping")
        

animal1 = Animal("Horse", False)
animal2 = Animal ("Bird", True)

animal1.movement()
