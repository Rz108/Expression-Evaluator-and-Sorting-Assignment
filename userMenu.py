# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement User Menu Class
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 4-Jan-2024
# Filename: userMenu.py
#
# ------------------------------------------------------------

from user import User
from error import Error
class UserMenu:
    def __int__(self, choices):
        self.choices = choices

    '''
     Set the choices 
    '''
    # Set the choices 
    def display_choices(self):
        # Looping through to display the different options
        statements = ''
        for index, choice in enumerate(self.choices, start = 1):
            statements += (f'\t{index}. {choice}\n')
        return statements[:-1]

    '''
     Get the choice from the user
    '''
    def get_choice(self):
        minimum, maximum = 1, len(self.choices)  
        
        # Getting the user input
        while True:
            user_input = input(f"Please select your choice: {str(tuple(f'{i}' for i in range(1,len(self.choices)+1))).replace(' ', '') }:\n" + self.display_choices() + '\nEnter choice: ' ).strip()

            # Validate selected option
            choice = Error.validate_integer(user_input, minimum, maximum)

            # If the choice is not none here, return the full model
            if choice is not None:
                return choice
    
