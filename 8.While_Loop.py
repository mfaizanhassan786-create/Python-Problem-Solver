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


# # Problem 4 — Countdown
# # Statement

# # Ask the user for a starting number.

# # Use a while loop to print a countdown until 1.



# # 1. Get input
# start_num = int(input("Enter a starting number: "))

# # 2. Initialize the counter with the user's number
# num = start_num

# # 3. Loop as long as the number is greater than or equal to 1
# while num >= 1:
#     print(num)        # Print current number
#     num = num - 1     # Decrement (count down)

# print("Blast off!")


# # Problem 5 — Password Attempts
# # Statement

# # Create a program with the correct password:


# # 1. Setup secret password and attempt limits
# secret_password = "python123"
# max_attempts = 3
# attempts = 0

# # 2. Loop as long as attempts are less than max_attempts
# while attempts < max_attempts:
#     user_input = input("Enter password: ")
#     attempts += 1  # Increment attempt counter
    
#     if user_input == secret_password:
#         print("✅ Access Granted!")
#         break  # Immediately exits the while loop
#     else:
#         remaining = max_attempts - attempts
#         if remaining > 0:
#             print(f"❌ Incorrect password! {remaining} attempt(s) remaining.\n")
#         else:
#             print("🔒 Account Locked! Too many failed attempts.")


