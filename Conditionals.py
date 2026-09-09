# # Problem 1 — Adult Check

# # Statement:
# # Write a program that stores a person's age and prints "You are an adult" only if the age is 18 or greater.

# a = int(input("Enter your age: "))

# if a >= 18:
#     print("You are an adult")
# else:
#     print("You are not an adult")


# # Problem 2 — Positive Number

# # Statement:
# # Take a number from the user and print "Positive number" only if the number is greater than 0.


# a= int(input("Enter the number: "))

# if a > 0:
#     print("Positive number")
# else:
#     print("Negative number")


# Problem 3 — Even Number

# Statement:
# Take an integer from the user.

# If the number is even, print:

# This is an even number.



# a = int(input("Enter your Number: "))

# if a % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")


# # Problem 4 — Discount Eligibility

# # Statement:
# # Take the user's shopping amount.

# # If the amount is 10,000 or greater, print:

# # You are eligible for a discount.


# a= int(input("Enter your shopping amount: "))

# if a >= 10000:
#     print("You are eligible for a discount.")
# else:
#     print("You are not eligible for a discount.")


# # Problem 5 — Login Verification

# # Statement:
# # Write a program that stores a correct username and password:


# # Stored credentials
# correct_username = "faizan"
# correct_password = "password123"

# # User inputs
# entered_username = input("Enter username: ")
# entered_password = input("Enter password: ")

# # Check credentials
# if entered_username == correct_username and entered_password == correct_password:
#     print("Login Successful! Welcome.")
# else:
#     print("Invalid username or password.")


# # Problem 6 — ATM Withdrawal

# # Statement:
# # Create a program with:

# # balance = 50000

# # Ask the user for a withdrawal amount.

# # If the withdrawal amount is less than or equal to the balance, calculate and display the remaining balance.
# # Otherwise, display:
# # Insufficient Balance!

# # Initial account balance

# balance = 50000

# # Get withdrawal amount from user (convert input to float or int for math)
# withdrawal_amount = float(input("Enter withdrawal amount: "))

# # Check if user has enough balance
# if withdrawal_amount <= balance:
#     balance = balance - withdrawal_amount
#     print(f" Withdrawal successful! Remaining balance: ${balance:.2f}")
# else:
#     print(" Insufficient Balance!")



# Problem 9 — Student Scholarship System

# Statement:
# Write a program that takes a student's:

# Name
# Percentage
# Family monthly income

# Then determine whether the student qualifies for a scholarship.

# Rules:

# A student qualifies if:

# Condition 1:

# Percentage is 80 or higher
# AND family income is 100,000 or less

# OR

# Condition 2:

# Percentage is 90 or higher
# AND family income is 150,000 or less

# If qualified:

# Congratulations Faizan!
# You are eligible for the scholarship.

# Otherwise:

# Sorry Faizan.
# You are not eligible for the scholarship.

# 1. Inputs
name = input("Enter student name: ")
percentage = float(input("Enter percentage: "))
income = float(input("Enter family monthly income: "))

# 2. Check Conditions
# Group each condition set in parentheses for clean logic evaluation
condition_1 = (percentage >= 80) and (income <= 100000)
condition_2 = (percentage >= 90) and (income <= 150000)

# 3. Decision
if condition_1 or condition_2:
    print(f"\nCongratulations {name}!")
    print("You are eligible for the scholarship.")
else:
    print(f"\nSorry {name}.")
    print("You are not eligible for the scholarship.")