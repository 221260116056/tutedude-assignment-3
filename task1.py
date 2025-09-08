# Task 1: Calculate Factorial Using a Function

# Step 1: Define a function to calculate factorial
def factorial(n):
    result = 1
    # Using a loop to calculate factorial
    for i in range(1, n + 1):
        result *= i
    return result

# Step 2: Call the function with a sample number
num = int(input("Enter a number to find its factorial: "))

# Step 3: Print the result
print("The factorial of", num, "is:", factorial(num))
