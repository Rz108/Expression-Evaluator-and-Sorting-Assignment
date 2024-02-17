# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement option 5
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: option5.py
#
#
# ------------------------------------------------------------

from tools import Tools
from classes.hashTable import hashTable
from classes.expressionEvaluator import ExpressionEvaluator
from classes.expressionManager import ExpressionManager
from classes.dependency import DependencyGraph
from classes.parseTree import ParseTreeBuilder
from classes.mergeSort import MergeSort
from option2 import OptionTwo
import os

# Creating option 5 inheriting option 2
class OptionFive(OptionTwo):
    '''
    Creating the init with data call in init 
    '''
    def __init__(self,datas):
        self.datas = datas

    '''
    Creating the run function to run the full code
    '''
    def run(self):

        # Inherit from option two the run option and getting the evaluated results
        results = super().run( boolean=False)
        
        # Retriving the value from the result and storing it as a list here
        vals = list(results.values())

        # If the storage is empty, return the program to the user
        if len(vals) == 0:
            print('\nThe storage is empty. Please add statements before saving it.')
            return
        
        # Creating a filtered list to store the item here and removing repeated values
        filtered_list = [item for item in vals if item is not None]
        filtered_listUnique = list(set(filtered_list))

        # Using custom sort function, i sort the values here 
        vals = MergeSort().sort(filtered_listUnique)[::-1] + [None] * (1 if len(vals) - len(filtered_list) > 0 else 0)

        # Initialising the string statement to store in the file
        statement = ''
        for i in (vals):

            # Creating the line for each statement here
            statement += f'*** Statements with value=> {i}\n'

            # getting the keys that matches with the value
            keys = [key for key, val in results.items() if (i is val or i== val)]

            # Sorting the keys if the length of keys is more than or equal to 2
            keys = MergeSort().sort(keys)

            # Storing it into the list
            statement_list = [f'{var}={self.datas[var]}' for var in keys]

            # Adding to the original statement for storing later on
            statement += '\n'.join(statement_list) + '\n'*2
        
        # Statement remove the last two characters in the list
        statement = statement[:-2]

        # Creating the while loop 
        while True:

            # Enter the output file for storage of contents
            file = input(f'\nPlease enter output file ("r" to return, "b" to menu): ')

            # If the r button is press, return to previous question
            if file.lower() == 'r':
                break

            # If the b button is pressed, return straight to main menu here
            if file.lower() == 'b':
                return

            # Try except block to check for all possible errors
            try:

                # Check if file path exist
                if os.path.exists(file):

                    # Ask if user wants to continue
                    while True:

                        # IF the file type provided is not acceptable, prompt the user to input the filetype again
                        if file[-4:] !=  '.txt'  and file[-3:] != '.md':
                            print('File type not supported ')
                            break
                            
                        # If the file already exist, ask the user to overwite it
                        question = input(f'Filename {file} already exists. Do you want to overwrite it? (y/n, "r" to return, "b" to menu): ')

                        # If the r button is press, return to previous question
                        if question.lower() == 'r':
                            break 

                        # If the b button is pressed, return straight to main menu here
                        if question.lower() == 'b':
                            return
                        
                        # IF the user wants to cancle the operation
                        elif question.lower() == 'n':
                            print("Operation cancelled.")
                            break   

                        # Overwrite file if the user input yes 
                        elif question.lower() == 'y':

                            # Proceeed to write file to the file here
                            Tools.write_file(file , statement)
                            print("File overwritten successfully.")
                            return  
                        
                        # Return invalid option if invalid buttons was pressed 
                        else:
                            print('Invalid Option')
                            continue
                
                # Write file if no error found
                else:

                    # Create a inner while loop 
                    while True:

                        # IF the file type provided is not acceptable, prompt the user to input the filetype again
                        if file[-4:] !=  '.txt'  and file[-3:] != '.md':
                            print('File type not supported ')
                            break
                            
                        # Write file to the file path with the statement
                        else:
                            Tools.write_file(file , statement)
                            return
            
            # Exception to handle other errors
            except Exception as e:
                print(f"An error occurred while writing to the file: {e}")
                return   