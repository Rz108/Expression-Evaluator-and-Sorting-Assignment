# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement option 1
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo, Bharathan Bhaskaran
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: option1.py
#
#
# ------------------------------------------------------------
from tools import Tools
from error import Error
from classes.equationCleanup import EquationCleanup

# Create the option 1 
class OptionOne:

    '''
    Creating the init with data call in init and also create an initialising an error
    '''
    def __init__(self,datas):
        self.datas = datas
        self.errorVal = Error()

    '''
    Creating the run funcion to run the code for option 1 with the checking of input statement 
    '''
    def run(self):

        # Create the try except block
        try:

            # Creating the while true block
            while True: 

                # Getting the input of the assignment from the user
                user_input = input('Enter the assignment statement you want to add/modify ("r" to return):\nFor example, a=(1+2)\n')

                # Provide option to return to main menu
                if user_input.lower() == 'r':
                    return self.datas
                
                # Removing the space from the user input
                user_input = user_input.replace(" ", "")

                # Validating the assignment input by the user
                message, isVal =  self.errorVal.validateAssignment(user_input)

                # if the validation is not valid, provide the message of the error
                if not isVal:
                    print(message)
                    continue
                
                # If all else pass, split by the equal sign
                key, value = Tools.splitByEqual(user_input)
                # Check for correctly fully paramthesis here

                is_valid1_5 = self.errorVal.validateInputParams(value)

                break_inner = False
                # If it fails the validation here
                if not is_valid1_5:
                    exp = EquationCleanup(value).get_cleanup()
                    if exp != value:
                        while True: 
                            input_msg = input(f'This is the equation after cleanup {message}={exp} compared to original equation {message}={exp}, do you want to continue (y/n)? ')
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
                    if not is_valid2:

                        # If old val exist then put back into the hashtable
                        if oldVal is not None:
                            self.datas[key] = oldVal  
                        else:
                            del self.datas[key] 
                        
                        # print the error message here
                        print(message2)
                        continue

                
                # while block to add more assignment 
                while True: 
                    user_input2 = input('Do you want continue adding more assignments? (Y/N) ')

                    # Validating the input here
                    if user_input2.lower() in ['y','yes']:
                        break
                    elif user_input2.lower() in ['n','no']:
                        return self.datas
                    if user_input2.lower() not in ['y','n','yes','no']:
                        print('Invalid option.')
                        continue
        
        # Try except block here to print the error
        except Exception as e:
            print(e)




        