"""
for Loop — 5 Problems

"""

# # Problem 1 — Print Numbers

# # Statement:
# # Write a program using a for loop that prints numbers from 1 to 10.


# for i in range(10):
#     print(i)



# Problem 2 — Multiplication Table

# Statement:
# Ask the user for a number and print its multiplication table from 1 to 10.


# 1. Get user input and convert to an integer
num = int(input("Enter a number: "))

# 2. Loop from 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")