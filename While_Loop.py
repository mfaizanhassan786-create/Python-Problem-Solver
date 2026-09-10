# # Problem 1 — Print Numbers
# # Statement

# # Use a while loop to print numbers from 1 to 10.



# i = 1
# while i <= 10:
#     print(i)
#     i += 1



# # Problem 2 — Sum of Numbers
# # Statement

# # Ask the user for a number n.

# # Use a while loop to calculate the sum from 1 to n.



# num = float(input("Enter a number: "))

# sum = 0

# i = 1
# while i <= num:
#     sum += i
#     i += 1

# print(f"The sum of numbers from 1 to {num} is {sum}")

# # Problem 3 — Even Numbers
# # Statement

# # Ask the user for a number n.

# # Use a while loop to print all even numbers from 1 to n.


# # 1. Take input from the user
# n = int(input("Enter a number (n): "))

# # 2. Initialize the loop counter
# i = 1

# # 3. Loop until i goes past n
# while i <= n:
#     if i % 2 == 0:  # Checks if i is divisible by 2 with 0 remainder
#         print(i)
#     i += 1  # Increment counter (CRITICAL: prevents infinite loop)