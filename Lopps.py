"""
for Loop — 5 Problems

"""

# # Problem 1 — Print Numbers

# # Statement:
# # Write a program using a for loop that prints numbers from 1 to 10.


# for i in range(10):
#     print(i)



# # Problem 2 — Multiplication Table

# # Statement:
# # Ask the user for a number and print its multiplication table from 1 to 10.


# # 1. Get user input and convert to an integer
# num = int(input("Enter a number: "))

# # 2. Loop from 1 to 10
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# # Problem 3 — Sum of Numbers

# # Statement:
# # Ask the user for a number n.

# # Use a for loop to calculate the sum of all numbers from 1 to n.

# num = int(input("Enter a number:"))
# sum = 0
# for i in range(0,num+1):
#     sum += i
# print(f"The sum of numbers from 1 to {num} is {sum}")


# # Problem 4 — Even and Odd Numbers

# # Statement:
# # Ask the user for a number n.

# # Use a for loop to go from 1 to n.


# # For every number, determine whether it is even or odd and print the result.


# num = int(input("Enter a number:"))

# for i in range(1,num+1):
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")



# Problem 5 — Student Marks Analyzer

# Statement:
# Write a program that asks the user to enter marks for 5 subjects, one at a time.

# Your program should:

# Use a for loop to collect the 5 marks.
# Calculate the total marks.
# Calculate the percentage.
# Display the total and percentage.