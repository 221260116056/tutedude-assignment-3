# Task 2: Using the Math Module for Calculations

import math   # importing the math module

# Step 1: Ask the user for a number as input
num = float(input("Enter a number: "))

# Step 2: Perform calculations using math module
square_root = math.sqrt(num)       # square root
natural_log = math.log(num)        # natural logarithm (base e)
sine_value = math.sin(num)         # sine of the number (in radians)

# Step 3: Display the results
print("\n--- Results ---")
print("Square Root of", num, ":", square_root)
print("Natural Logarithm of", num, ":", natural_log)
print("Sine of", num, "(in radians):", sine_value)
