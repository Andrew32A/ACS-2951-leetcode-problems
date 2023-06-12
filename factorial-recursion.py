# Problem
# Create a function that returns the factorial of any positive input number
# Helpful tip: Try to solve the problem comfortably in code before trying it recursively!
# Factorial is:

# 4! ==> 4 x 3 x 2 x 1

# Step 1: Restate question
# Step 2: Ask Clarifying Questions
# Step 3: Write out action plan
# Step 4: Write out code


# action plan:
    # write code
    # code go brr

def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Please input a positive number"
    return n * factorial(n - 1)

num_input = int(input("Enter a number: "))
print(factorial(num_input))

# could add something like this for edge cases

# while True:
#     try:
#         num_input = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("Invalid input. Please enter an integer.")

