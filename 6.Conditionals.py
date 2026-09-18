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



# # Problem 9 — Student Scholarship System

# # Statement:
# # Write a program that takes a student's:

# # Name
# # Percentage
# # Family monthly income

# # Then determine whether the student qualifies for a scholarship.

# # Rules:

# # A student qualifies if:

# # Condition 1:

# # Percentage is 80 or higher
# # AND family income is 100,000 or less

# # OR

# # Condition 2:

# # Percentage is 90 or higher
# # AND family income is 150,000 or less

# # If qualified:

# # Congratulations Faizan!
# # You are eligible for the scholarship.

# # Otherwise:

# # Sorry Faizan.
# # You are not eligible for the scholarship.

# # 1. Inputs
# name = input("Enter student name: ")
# percentage = float(input("Enter percentage: "))
# income = float(input("Enter family monthly income: "))

# # 2. Check Conditions
# # Group each condition set in parentheses for clean logic evaluation
# condition_1 = (percentage >= 80) and (income <= 100000)
# condition_2 = (percentage >= 90) and (income <= 150000)

# # 3. Decision
# if condition_1 or condition_2:
#     print(f"\nCongratulations {name}!")
#     print("You are eligible for the scholarship.")
# else:
#     print(f"\nSorry {name}.")
#     print("You are not eligible for the scholarship.")


# # Problem 10  — Grade Calculator
# # Statement:

# # Write a program that takes a student's percentage and displays their grade.

# # Use these rules:

# # Percentage	Grade
# # 90–100	A+
# # 80–89	A
# # 70–79	B
# # 60–69	C
# # 50–59	D
# # Below 50	F


# # 1. Input
# percentage = float(input("Enter percentage: "))

# # 2. Decision Logic

# if percentage >= 90: # Covers 90 to 100
#     grade = "A+"
# elif percentage >= 80:
#     grade = "A"
# elif percentage >= 70:
#     grade = "B"
# elif percentage >= 60:
#     grade = "C"
# elif percentage >= 50:
#     grade = "D"
# else:
#     grade = "F"

# # 3. Output
# print(f"Your Grade is: {grade}")



# # Problem 11 — Electricity Bill
# # Statement:

# # Write a program that takes the number of electricity units consumed and determines the price category.

# # Use these rules:

# # Units	Category
# # 0–100	Low Usage
# # 101–300	Normal Usage
# # 301–500	High Usage
# # Above 500	Very High Usage

# # Print the category.



# # 1. Input
# units = float(input("Enter units consumed: "))

# # 2. Decision Logic

# if units <= 100:  # 0 to 100
#     category = "Low Usage"
# elif units <= 300:  # 101 to 300
#     category = "Normal Usage"
# elif units <= 500:  # 301 to 500
#     category = "High Usage"
# else:  # Above 500
#     category = "Very High Usage"

# # 3. Output
# print(f"Usage Category: {category}")




# # Problem 12 — ATM Transaction System
# # Statement:

# # Create an ATM program with:

# # balance = 50000

# # Ask the user to select:

# # 1. Check Balance
# # 2. Withdraw
# # 3. Deposit

# # Use if-elif-else to handle the selected option.

# # Requirements:

# # Option 1:

# # Display:

# # Your balance is: 50000

# # Option 2:

# # Ask for withdrawal amount.

# # If the amount is valid and there is sufficient balance, display the remaining balance.

# # Otherwise display:

# # Insufficient balance!

# # Option 3:

# # Ask for deposit amount and display the updated balance.

# # If the user enters anything other than 1, 2, or 3:

# # Invalid option!

# # Concept: if-elif-else + nested if

# # Initial state
# balance = 50000

# # Display menu options
# print("--- ATM MENU ---")
# print("1. Check Balance")
# print("2. Withdraw")
# print("3. Deposit")

# # Get user choice
# option = input("Select an option (1-3): ")

# # Main branching logic
# if option == "1":
#     print(f"Your balance is: {balance}")

# elif option == "2":
#     withdraw_amount = float(input("Enter withdrawal amount: "))
    
#     # NESTED IF: Checking if the withdrawal amount is valid against balance
#     if withdraw_amount <= balance:
#         balance = balance - withdraw_amount
#         print(f"Withdrawal successful!\nRemaining balance is: {balance}")
#     else:
#         print("Insufficient balance!")

# elif option == "3":
#     deposit_amount = float(input("Enter deposit amount: "))
#     balance = balance + deposit_amount
#     print(f"Deposit successful!\nUpdated balance is: {balance}")

# else:
#     print("Invalid option!")




# # Problem 13 — University Admission System
# # Statement:

# # Create a program that takes:

# # Student name
# # Percentage
# # Entry test score

# # Determine the student's admission status.

# # Rules:

# # First check the percentage:

# # 90 or above

# # Excellent Academic Record

# # 80–89

# # Very Good Academic Record

# # 70–79

# # Good Academic Record

# # Below 70

# # Academic Record Below Requirement

# # But there's an additional admission rule:

# # A student can be eligible for admission only if percentage ≥ 70.

# # If percentage is 70 or above, use a nested if to check the entry test:

# # Entry test ≥ 60 → Admission Eligible
# # Entry test < 60 → Entry Test Failed

# # If percentage is below 70:

# # Admission Not Eligible

# # 1. Take Inputs
# name = input("Enter student name: ")
# percentage = float(input("Enter percentage: "))
# entry_test = float(input("Enter entry test score: "))

# print(f"\n--- Admission Profile for {name} ---")

# # 2. Check Academic Record (First set of rules)
# if percentage >= 90:
#     print("Record: Excellent Academic Record")
# elif percentage >= 80:
#     print("Record: Very Good Academic Record")
# elif percentage >= 70:
#     print("Record: Good Academic Record")
# else:
#     print("Record: Academic Record Below Requirement")

# # 3. Check Admission Status (Using NESTED IF)
# if percentage >= 70:
#     # We are inside the first IF block now (Notice the indentation!)
#     if entry_test >= 60:
#         print("Status: Admission Eligible")
#     else:
#         print("Status: Entry Test Failed")
# else:
#     # This lines up with the main IF (percentage >= 70)
#     print("Status: Admission Not Eligible")


# # Problem 14 — Bank Loan Eligibility System

# # This is your hardest challenge.

# # Statement:

# # Create a loan eligibility program that asks the user for:

# # Name
# # Age
# # Monthly salary
# # Credit score
# # Existing loan (yes or no)

# # Use the following rules.

# # Step 1 — Age

# # If age is:

# # Below 18 → Not eligible
# # 18–25 → Young applicant
# # 26–50 → Standard applicant
# # Above 50 → Senior applicant
# # Step 2 — Salary

# # If the applicant is at least 18, check salary using a nested if:

# # Salary < 30,000 → Not eligible
# # Salary 30,000–59,999 → Basic category
# # Salary 60,000+ → Premium category
# # Step 3 — Credit Score

# # For applicants who passed the salary requirement:

# # 750+ → Excellent credit
# # 650–749 → Good credit
# # 550–649 → Average credit
# # Below 550 → Poor credit
# # Step 4 — Existing Loan

# # If the applicant already has a loan:

# # Existing loan detected.

# # Otherwise:

# # No existing loan.

# # Finally, determine eligibility:

# # A person is eligible only when:

# # Age is 18+
# # Salary is at least 30,000
# # Credit score is at least 650
# # No existing loan



# #       BANK LOAN ELIGIBILITY SYSTEM

# # 1. Collect Inputs
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# salary = float(input("Enter monthly salary: "))
# credit_score = int(input("Enter credit score: "))
# existing_loan = input("Existing loan (yes/no): ").strip().lower()


# # 2. Setup Variables
# applicant_category = ""
# salary_category = ""
# credit_rating = ""
# loan_status_text = ""
# is_eligible = False


# # 3. CHECK AGE


# if age < 18:
#     applicant_category = "Not eligible"

# elif 18 <= age <= 25:
#     applicant_category = "Young applicant"

# elif 26 <= age <= 50:
#     applicant_category = "Standard applicant"

# else:
#     applicant_category = "Senior applicant"


# # 4. CHECK SALARY


# if age >= 18:

#     if salary < 30000:
#         salary_category = "Not eligible"

#     elif salary < 60000:
#         salary_category = "Basic category"

#     else:
#         salary_category = "Premium category"


  
#     # 5. CHECK CREDIT SCORE


#     if salary >= 30000:

#         if credit_score >= 750:
#             credit_rating = "Excellent credit"

#         elif credit_score >= 650:
#             credit_rating = "Good credit"

#         elif credit_score >= 550:
#             credit_rating = "Average credit"

#         else:
#             credit_rating = "Poor credit"

        

#         # 6. CHECK EXISTING LOAN
       

#         if existing_loan == "yes":
#             loan_status_text = "Existing loan detected."

#         else:
#             loan_status_text = "No existing loan."


        
#         # 7. FINAL ELIGIBILITY
       

#         if credit_score >= 650 and existing_loan == "no":
#             is_eligible = True



# # 8. FINAL REPORT


# print("\n" + "=" * 45)
# print("        BANK LOAN ELIGIBILITY REPORT")
# print("=" * 45)

# print(f"Name: {name}")
# print(f"Age: {age}")

# print(f"\nApplicant Category: {applicant_category}")
# print(f"Salary Category: {salary_category}")

# if credit_rating:
#     print(f"Credit Rating: {credit_rating}")

# if loan_status_text:
#     print(f"Loan Information: {loan_status_text}")


# print("\n" + "-" * 45)

# if is_eligible:
#     print("Loan Status: ELIGIBLE")
# else:
#     print("Loan Status: NOT ELIGIBLE")

# print("=" * 45)
