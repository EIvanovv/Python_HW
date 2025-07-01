# ---------------------------------- Task 1 ---------------------------------- #
### Description:
#  Ask the user for their name, age, and favorite color. Store this information
#  into variables and print a greeting in the console, for example:
#  "Hello, my name is Alice, I am 30 years old, and my favorite color is black."
#  Use f-strings and the variables to construct the message.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here

# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# color = input("Enter your favourite color:")

# print(f"Hello, my name is {name}, I am {age} years old, and my favorite color is {color}.")

### Expected output (example):
# Enter your name: Alice
# Enter your age: 30
# Enter your favorite color: black
# Hello, my name is Alice, I am 30 years old, and my favorite color is black.

# ---------------------------------- Task 2 ---------------------------------- #
### Description:
#  Ask the user for their birth year and the current year.
#  Calculate their age using these inputs, then print the result.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here

# birth_year = int(input("Enter your birth year: "))
# current_year = int(input("Enter the current year: "))
# user_years_old_calculated = current_year - birth_year

# print(f"You are {user_years_old_calculated} years old.")

### Expected output (example):
# Enter your birth year: 1995
# Enter the current year: 2025
# You are 30 years old.

# ---------------------------------- Task 3 ---------------------------------- #
### Description:
#  Ask the user to enter a large numeric amount (e.g., 1234567.89).
#  Format this number to be displayed as a USD currency with two decimal places and
#  commas for thousands separators. Example: "$1,234,567.89".
#  Use an f-string to format and print the result.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here

# amount = float(input("Enter an amount: "))

# print(f"${amount:,}")

### Expected output (example):
# Enter an amount: 1234567.89
# $1,234,567.89

# ---------------------------------- Task 4 ---------------------------------- #
### Description:
#  Ask the user for the names and prices of three different shopping items.
#  Create a simple receipt format. Use f-strings to format each item name
#  aligned to the left and its price aligned to the right.
#  Each line for an item should be 30 characters wide.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here

# item_1 = input("Enter name for item 1: ")
# price_item_1 = float(input("Enter price for item 1: "))
# item_2 = input("Enter name for item 2: ")
# price_item_2 = float(input("Enter price for item 2: "))
# item_3 = input("Enter name for item 3: ")
# price_item_3 = float(input("Enter price for item 3: "))
# header = "Shopping Items:"

# print("")
# print(f"{header:^40}")
# print(f"{item_1:<20}{price_item_1:>20}")
# print(f"{item_2:<20}{price_item_2:>20}")
# print(f"{item_3:<20}{price_item_3:>20}")

### Expected output (example):
# Enter name of item 1: Milk
# Enter price of item 1: 1.99
# Enter name of item 2: Bread
# Enter price of item 2: 2.49
# Enter name of item 3: Eggs
# Enter price of item 3: 3.59
#
#           Shopping Items:
# Milk                          1.99
# Bread                         2.49
# Eggs                          3.59

# ---------------------------------- Task 5 ---------------------------------- #
### Description:
#  Ask the user for the current temperature in Celsius.
#  Convert this temperature to Fahrenheit using the formula: $F = (C \times 9/5) + 32$.
#  Print both the Celsius and Fahrenheit temperatures, formatted to one decimal place,
#  using an f-string.

### Given:
# No initial variables are given. You need to get input from the user.

### Your code here

# current_temperature_in_celsius = float(input("Please enter the current temperature in Celsius: "))
# temperature_converted_to_fahrenheit = current_temperature_in_celsius * (9/5) + 32

# print(f"{current_temperature_in_celsius:.1f}°C is qual to {temperature_converted_to_fahrenheit:.1f}°F")

### Expected output (example):
# Enter temperature in Celsius: 25
# 25.0°C is equal to 77.0°F