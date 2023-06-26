"""This program emulates a simple expense tracking program. It employs various functions
to add expenses to a list, save those expenses, and perform a certain number of 
operations on those expenses (total cost, matching of categories, etc.)

Task: Your task is to complete the implementation of the code and make sure that matches
the requirements set in the assignment's prompt.
First, you will have to make your code identifiable by setting the following information.

******************************************************
Name: Simon Pierre Ndizihiwe
Andrew ID: sndizihi@andrew.cmu.edu
Semester: Summer 2023
Course: Introduction to Python
Last modified: Sunday, 25 June 2023
******************************************************

"""

from typing import Tuple

## Declare a global variable to contain all the expenses processed in the program
expenses = []


class BadInputException(Exception):
   """Vanilla exception class used for testing"""
   pass


def add_expense(category: str, amount: float):

   global expenses

   # Verify that the category variable contains at least three characters
   if len(category) < 3:
      raise BadInputException("Invalid Input")

   # Verify that the amount variable is a floating value strictly greater than zero.
   if not isinstance(amount, float) or amount <= 0:
      raise BadInputException("Invalid Input")   

   # Append a tuple (category, amount) to the `expenses` list
   expenses.append((category, amount))


def dump_expenses(file_path='expenses.txt'):
   global expenses

   # Open the file in write mode, overriding its content
   with open(file_path, 'w') as f:
    #   for each tuple in the `expenses` list, write a line in the CSV format (e.g., Clothes,10.05)
    for category, amount in expenses:
       line = f"{category},{amount:.2f}\n" # Format the line with 2 decimal points precision for the amount
       f.write(line)


def read_expenses(file_path='expenses.txt'):
   global expenses
   
   # Attempt to open the file for reading
   try:
      with open(file_path, 'r') as f:
         # Read each line from the file
         for line in f:
            # Split the line by comma to separate category and amount
            category, amount = line.strip().split(',')
            # Convert the amount from string to float
            amount = float(amount)
            # Append the (category, amount) tuple to the expenses list
            expenses.append((category, amount))
   except FileNotFoundError:
       # If the file does not exist, safely return from the function
       return
   

def get_expenses_by_category(category):
   global expenses

   # Create an empty list to store the matching expenses
   matching_expenses = []

   # Iterate over each expense tuple in the expenses list
   for expense in expenses:
      # Check if the category matches the provided category argument
      if expense[0] == category:
         # If the category matches, add the expense tuple to the matching_expenses list
         matching_expenses.append(expense)
        
   # Return the matching expenses list
   return matching_expenses



def calculate_total_expenses():
   global expenses
   
   # Initialize a variable to store the total amount
   total_amount = 0.0

   # Iterate over each expense tuple in expenses list
   for expense in expenses:
      # Add the amount of current expense to the total_amount variable
      total_amount += expense[1]

   # Return the total amount of the expenses
   return total_amount


def get_menu_action() -> int:

   while True:
      print('Menu:')
      print('1. Add an expense')
      print('2. View expenses by category')
      print('3. Calculate total expenses')
      print('4. Exit')

      try:
         choice = int(input("Enter your selection: "))
         if choice in [1,2,3,4]:
            break # Valid input, break out of the loop
         else:
            print("Invalid selection. Please choose a number between 1 and 4.")
      except ValueError:
         print("Invalid input. Please enter a number.") 
   return choice



def print_expense(expense: Tuple[str, float]) -> str:
   category, amount = expense

   # Format category and amount strings with the desired width and precision
   formatted_category = category.ljust(10)[:10]
   formatted_amount = f"${amount:.2f}".ljust(10)[:10]

   # Construct the output string using the formatted category and amount
   output = f"|{formatted_category}|{formatted_amount}|"
   return output

if __name__ == "__main__":
   # Read the expenses, if file exists, into the 'expenses' list
   read_expenses()

   ## Retrieve the user's choice
   while True:
      command = get_menu_action()
      if command == 1:
         category = input('Expense Category: ')
         amount = float(input('Expense Amount: '))
         try:
            add_expense(category=category, amount=amount)
            print("Expense added successfully!")
         except BadInputException:
            print('Invalid value!')
      elif command == 2:
         category = input('Expense Category: ')
         expenses = get_expenses_by_category(category=category)
         print('|Category  |Amount    |')
         print('***********************')
         for expense in expenses:
            print(print_expense(expense))
      elif command == 3:
         total = calculate_total_expenses()
         print(f'Total expenses is: ${total:.2f}')
      elif command == 4:
         # Save the list of expenses into a file for future use
         dump_expenses()
         # changed the next statement to exit the program gracefully
         print('Expense tracker application exiting...')
         break
      else:
         raise ValueError('Invalid command entered')
