# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement option 4
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: option4.py
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
from classes.equationCleanup import EquationCleanup
from option2 import OptionTwo
from error import Error

# Creating Option 4 with inheritance to option 2
class OptionFour(OptionTwo):
    '''
    Creating the init with data call in init and also create an initialising an error
    '''
    def __init__(self , datas):
        self.datas = datas
        self.errorVal = Error()

    '''
    Creating the get data function that retrieves all the file contents and evaluate it
    '''
    def get_data(self):
        while  True:
            # Get the file path here
            file_path = input('Please enter input file ("r" to return): ')

            # If user wants to return to main menu
            if file_path == 'r':
                return self.datas
            if not Tools.open_file(file_path):
                continue
            # Make sure that the file path exist and open file path
            while True:

                # Getting the file contents here
                text = Tools.open_file(file_path)

                # Splitting the file contents by new line
                text = text.split('\n')

                # For each new line in the file contents 
                for line in text:

                    # Strip the line of adding leading spaces
                    line = line.strip()

                    # If the line is empty then continue to the next line here
                    if not line:
                        continue


                    # Try except block to fully handle error
                    try:

                        # while loop to handle errors here
                        while True:

                            # Error message and is validate was check here for the key errors, 
                            # errors are return and continue to the next line
                            message, isVal =  self.errorVal.validateAssignment(line)
                            if not isVal:
                                print(message)
                                break
                            
                            # Proceed to split by the equal sign here
                            key, value = Tools.splitByEqual(line)
                            is_valid1_5 = self.errorVal.validateInputParams(value)

                            break_inner = False
                            # If it fails the validation here
                            if not is_valid1_5:
                                exp = EquationCleanup(value).get_cleanup()
                                if exp != value:
                                    while True: 
                                        input_msg = input(f'This is the equation after cleanup {message}={exp} compared to original equation {message}={exp}, do you want to continue? ')
                                        if input_msg.lower() in ['yes', 'y']:

                                            # If the user confirms to proceed
                                            print("Continuing with the cleanup equation.")
                                            break
                                        elif input_msg.lower() in ['no', 'n']:

                                            # If the user decides not to proceed
                                            break_inner=True
                                            break
                                        else:
                                            # If the input is not recognized
                                            print("Invalid input.")

                            if not break_inner:
                                # Getting the old value with the key
                                oldVal = self.datas.get(key, None) 

                                # Storing the data into the hash table
                                self.datas[key] = value
                                
                                # validation the circular statement
                                message2, is_valid2 = self.errorVal.validateCircular(self.datas)

                                # if the validation is not valid, provide the message of the error
                                 # If it's a circular dependency error here
                                if not is_valid2:

                                    # If the old value exist
                                    if oldVal is not None:

                                        # Store the old value
                                        self.datas[key] = oldVal  
                                    else:

                                        # Delete the key from the keys
                                        del self.datas[key] 
                                    
                                    # Print out the error message
                                    print(message2)

                                    # Here is to check whether the user want to redefine the variable
                                    while True:

                                        # Getting the input on whether to redefine
                                        inputQus = input(f'Do you want to redefine the variable {key} again? (Y/N): ')

                                        # if the users agree to redefine
                                        if inputQus.lower() in ['y', 'yes']:

                                            # Ask for the new assignment and user select their decision
                                            while True:  

                                                # Key in the assignment and no to cancel
                                                line = input('Key in the new assignment statement for the variable (N to cancel):\n')

                                                # If the user press no, go to the next line
                                                if line.lower() == 'N':
                                                    break

                                                # Checking whether the new line entered is valid or not
                                                message, isVal =  self.errorVal.validateAssignment(line)

                                                # If the new line is not valid continue to the while loop to ask the questions again
                                                if not isVal:

                                                    # Print out the error message if it is not valid
                                                    print(message)
                                                    continue

                                                # If it is valid, split the line by the equal sign here
                                                key2, value = Tools.splitByEqual(line)

                                                # If the key provided is not equal to the original key in the text, ask the user to key in again
                                                if key2 != key:

                                                    # Continue prompting and if the user want to stop they can and continue to the next line
                                                    var  = input('Wrong key. Please enter the correct key to redefine or N to cancel.')
                                                    if var == 'N':
                                                        break

                                                    # Continue prompting the keying in of quesion
                                                    continue

                                                # Break if the key is equal to continue to the evaluation and next line
                                                else:
                                                    break
                                            break  
                                    
                                        # If the user input is no then break too
                                        elif inputQus.lower() in ['n', 'no']:
                                            break  

                                        # If the user input is neither in the option, return invalid option here
                                        if inputQus.lower() not in ['y', 'n', 'yes', 'no']:
                                            print('Invalid option.')
                                            continue
                                    
                                    # If the user input is no then break here too
                                    if inputQus.lower() in ['n', 'no']:
                                        break       
                                
                                # Break if the sentence is valid and correct
                                else:
                                    break  

                          
                        
                    # Except block to handle other possible error
                    except Exception as e:
                        print(e)
                    
                # Break the loop if it get to this point
                break
            break

        # Return the stored data to the hashtable in the main program
        return self.datas
    

    '''
    Run the full option here with inheritance of function from option 2
    '''
    def run(self):
        results = super().run(self.datas)