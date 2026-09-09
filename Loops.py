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



# # Problem 5 — Student Marks Analyzer

# # Statement:
# # Write a program that asks the user to enter marks for 5 subjects, one at a time.

# # Your program should:

# # Use a for loop to collect the 5 marks.
# # Calculate the total marks.
# # Calculate the percentage.
# # Display the total and percentage.

# # 1. Initialize the accumulator variable before the loop starts
# total_marks = 0
# total_subjects = 5

# # 2. Loop 5 times (range(1, 6) gives us sequence: 1, 2, 3, 4, 5)
# for subject_num in range(1, total_subjects + 1):
#     mark = float(input(f"Enter marks for subject {subject_num}: "))
#     total_marks += mark  # Short for: total_marks = total_marks + mark

# # 3. Calculate percentage (assuming each subject is out of 100)
# max_marks = total_subjects * 100
# percentage = (total_marks / max_marks) * 100

# # 4. Display the results
# print("\n--- Summary ---")
# print(f"Total Marks: {total_marks} / {max_marks}")
# print(f"Percentage:  {percentage:.2f}%")



# # Problem 6 — Multiples of a Number

# # Statement:
# # Ask the user for a number n. Using a for loop, print the first 10 multiples of that number.

# # 1. Ask the user for a number and convert it to an integer
# n = int(input("Enter a number: "))

# print(f"\nThe first 10 multiples of {n} are:")

# # 2. Loop from 1 through 10
# for i in range(1, 11):
#     multiple = n * i
#     print(f"Multiple {i}: {multiple}")



# # Problem 7 — Count Even and Odd Numbers

# # Statement:
# # Ask the user for a number n.

# # Using a for loop from 1 to n:

# # Count how many numbers are even.
# # Count how many numbers are odd.
# # Display both counts.

# # 1. Ask user for input and convert to integer
# n = int(input("Enter a number (n): "))

# # 2. Initialize two counter variables outside the loop
# even_count = 0
# odd_count = 0

# # 3. Loop from 1 to n (inclusive)
# for num in range(1, n + 1):
#     if num % 2 == 0:
#         even_count += 1  # Increment even counter
#     else:
#         odd_count += 1   # Increment odd counter

# # 4. Display the results
# print(f"\nResults from 1 to {n}:")
# print(f"Even numbers count: {even_count}")
# print(f"Odd numbers count:  {odd_count}")

# Problem 8 — Find the Largest Number

# Statement:
# Ask the user to enter 5 numbers, one at a time.

# Use a for loop to determine the largest number without using Python's built-in max() function.

# 1. Initialize the record holder to negative infinity
# float('-inf') is smaller than any number the user could possibly enter
largest = float('-inf')

# 2. Loop 5 times to collect inputs
for i in range(1, 6):
    num = float(input(f"Enter number {i}: "))
    
    # 3. Check if the current number beats the record holder
    if num > largest:
        largest = num

# 4. Print the final winner
print(f"\nThe largest number is: {largest}")