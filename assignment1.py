#!/usr/bin/env python3

'''
OPS445 Assignment 1 
Program: assignment1.py 
This script is the original work of Prabhnoor Singh. No code in this file 
has been copied from any external source except for materials provided 
by the course instructor. I understand and will abide by the Academic 
Honesty Policy, and I have not shared this script with anyone other 
than for grading purposes.

Author: Prabhnoor Singh
Student ID: psingh647
Semester: Fall 2024
Description:
This script calculates past and future dates based on a given start date 
and a divisor of a year. It validates the input, handles leap years, and 
accurately transitions between days, months, and years.

Citations and References:
1. Seneca College. https://seneca-ictoer.github.io/OPS445/A-Labs/Labs1-5  
   - Used for understanding concepts like leap years, date validation, and Python basics.
2. Codecademy. Retrieved February 27, 2024, from https://www.codecademy.com/resources/docs/python  
   - Referenced for splitting strings and general Python syntax.
3. Lemonaki, D. (2022). Splitting a string in Python.  
   Retrieved from https://www.freecodecamp.org/news/how-to-split-a-string-in-python/  
   - Provided insights into string manipulation techniques used in the `valid_date()` function.
4. GfG. (2023). Logical operators in Python with examples.  
   Retrieved from https://www.geeksforgeeks.org/python-logical-operators/  
   - Assisted with constructing logical conditions in `leap_year()` and `valid_date()`.
5. Real Python. (2023). Defining your own Python function.  
   Retrieved from https://realpython.com/defining-your-own-python-function/  
   - Inspired the use of clear function definitions and docstring formatting.
6. Loops. LearnPython.org. Retrieved from https://www.learnpython.org/en/Loops  
   - Helped in structuring loops in the `dbda()` function for calculating future and past dates.
'''


import sys

def leap_year(year: int) -> bool:
    """
    Checks if a given year is a leap year.
    
    Leap years are divisible by 4, but not by 100 unless also divisible by 400.
    If it's a leap year, February will have 29 days instead of 28.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """
    Gets the maximum number of days in a given month for a specific year.
    
    This function takes into account leap years for February.

    Args:
        month (int): The month (1 for January, 2 for February, etc.).
        year (int): The year (used to check for leap years).

    Returns:
        int: The maximum number of days in the given month.
    """
    # Standard days in each month
    mon_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # Adjust February's days if it's a leap year
    if month == 2 and leap_year(year):
        return 29
    return mon_dict.get(month, 0)

def after(date: str) -> str:
    """
    Calculates the next day's date based on the given date.
    
    Refactored as required to use the `leap_year()` and `mon_max()` functions to handle
    transitions between days, months, and years.

    Args:
        date (str): The current date in YYYY-MM-DD format.

    Returns:
        str: The next day's date in YYYY-MM-DD format.
    """
    # Split the date into year, month, and day
    year, mon, day = (int(x) for x in date.split('-'))
    day += 1  # Move to the next day

    # Check if the day exceeds the max for the current month
    if day > mon_max(mon, year):  # Uses mon_max() for max days
        day = 1  # Reset to the first day of the next month
        mon += 1
        if mon > 12:  # If month exceeds December, reset to January and increment year
            mon = 1
            year += 1

    # Return the formatted next day's date
    return f"{year}-{mon:02}-{day:02}"

def before(date: str) -> str:
    """
    Calculates the previous day's date based on the given date.
    
    Handles transitions between months and years, and accounts for leap years.

    Args:
        date (str): The current date in YYYY-MM-DD format.

    Returns:
        str: The previous day's date in YYYY-MM-DD format.
    """
    # Split the date into year, month, and day
    year, mon, day = (int(x) for x in date.split('-'))
    day -= 1  # Move to the previous day

    # Check if the day is less than 1 (previous month's last day)
    if day < 1:
        mon -= 1  # Move to the previous month
        if mon < 1:  # If month is less than January, move to December of the previous year
            mon = 12
            year -= 1
        day = mon_max(mon, year)  # Set the day to the max of the previous month

    # Return the formatted previous day's date
    return f"{year}-{mon:02}-{day:02}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " YYYY-MM-DD NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    ...

def dbda(start_date: str, step: int) -> str:
    "given a start date and a number of days into the past/future, give date"
    # create a loop
    # call before() or after() as appropriate
    # return the date as a string YYYY-MM-DD
    ...

if __name__ == "__main__":
    # process command line arguments
    # call dbda()
    # output the result
    ...
