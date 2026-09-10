"""
Functions in Python

Functions are one of the most important topics in Python.
They will later become extremely important for FastAPI, AI/ML, data science, and larger projects.
"""


# # Problem 1 — Simple Function

# def hello():
#     print("Hello World!")

# hello()



# # Problem 2 — Personal Greeting

# def greet():
#     print("Hello Ali")
#     print("Welcome to Python Programming.")
# greet()


# # Problem 3 — Print Numbers

# def num():
#     for i in range(10):
#         print(i)

# num()


# # Problem 4 — Even Numbers Function

# def even_num():
#     for i in range(10):
#         if i % 2 == 0:
#             print(i)

# even_num()


# # Problem 5 — Calculator Function

def calculator():
    # 1. Collect inputs and convert them to float for decimal support
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # 2. Perform basic calculations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    
    # 3. Defensive check: Prevent division by zero
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (Cannot divide by zero)"

    # 4. Display formatted results
    print(f"\nAddition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

# Execute the function
calculator()