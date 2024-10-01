#!/usr/bin/python3
Square = __import__('6-square').Square

my_square = Square(3)
print(my_square)  # This will use the __str__ method

print("--")

my_square.size = 10
print(my_square)  # This will use the __str__ method

print("--")

my_square.size = 0
print(my_square)  # This will use the __str__ method

print("--")

