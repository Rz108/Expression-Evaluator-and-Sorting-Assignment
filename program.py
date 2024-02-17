# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement program class
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 4-Jan-2024
# Filename: program.py
#
# ------------------------------------------------------------
from userMenu import UserMenu
from tools import Tools
from user import User
from classes.stack import Stack
from classes.hashTable import hashTable
from option1 import OptionOne
from option2 import OptionTwo
from option3 import OptionThree
from option4 import OptionFour
from option5 import OptionFive
from option6_ruizhuo import OptionSix
from option7_ruizhuo import OptionSeven
from option8_Bharathan import Feature1
from option9_Bharathan import Feature2
from option10_jonathan import Option10
from option11_jonathan import Option11
import os

class Program(UserMenu):
    '''
    Creating the inheritance here to username
    '''
    def __init__(self, config):
        # Create the inheritance here

        super().__init__()
        self.config = config

        # creating the hash table here 
        self.datas =  hashTable()
    
    '''
    Creating the set details function of the details
    '''
    def set_details(self):
        users = User()
        users.set_name(self.config['name'])
        users.set_adminNo(self.config['admin_number'])
        users.set_class(self.config['class'])
        users.set_moduleCode(self.config['module_code'])
        users.set_info(self.config['welcome_message'])
        return users
    
    '''
        Setting all the run methods here
    '''
    def run(self):
        userObj = self.set_details()

        # Setting the starting page

        print(userObj)
        while True:
            # Define the data structure
            # Setting the different options

            self.choices = ['Add/Modify assignment statement', 'Display current assignment statements',
                            'Evaluate a single variable', 'Read assignment statements from file', 
                            'Sort assignment statements','Assignment Game (Rui Zhuo)','Analyse on time complexity (Rui Zhuo)','Calculator (Bharathan)','Delete Assignment (Bharathan)','extra_option1 (Jonathan)','extra_option2 (Jonathan)','Exit']
            press_enter =   input("\nPress enter key, to continue...\n")
            
            # If the enter key is press here
            if press_enter == '' or press_enter:

                # Getting the user to input their choice
                user_choice = self.get_choice()

                # if the option choosen is one, run the run function here 
                if user_choice == 1:
                    self.datas = OptionOne(self.datas).run()

                # if the option choosen is two, run the run function here 
                elif user_choice == 2:
                    try:
                        print('\nCURRENT ASSIGNMENT:')
                        print('*'*20)
                        OptionTwo(self.datas).run()
                    except Exception as e:
                        print(e)

                # if the option choosen is three, run the run function here 
                elif user_choice == 3:
                    try:
                        OptionThree(self.datas).run()
                    except Exception as e:
                        print(e)

                # if the option choosen is four, run the run function here 
                elif user_choice == 4:
                    try:
                        self.datas = OptionFour(self.datas).get_data()
                        print('\nCURRENT ASSIGNMENT:')
                        print('*'*20)
                        OptionFour(self.datas).run()
                    except Exception as e:
                        print(e)

                # if the option choosen is five, run the run function here 
                elif user_choice == 5:
                    try:
                        OptionFive(self.datas).run()
                    except Exception as e:
                        print(e)

                # if the option choosen is six, run the run function here 
                elif user_choice == 6:
                    try:
                        OptionSix().run()
                    except Exception as e:
                        print(e)

                # if the option choosen is seven, run the run function here 
                elif user_choice == 7:
                    try:
                        OptionSeven(self.datas).full_run()
                    except Exception as e:
                        print(e)
                # if the option choosen is 8, run the run function here 
                elif user_choice == 8:
                    try:
                        Feature1(self.datas).run()
                    except Exception as e:
                        print(e)

                # if the option choosen is 9, run the run function here 
                elif user_choice == 9:
                    try:
                        Feature2(self.datas).run()
                    except Exception as e:
                        print(e)
                                         
                # if the option choosen is 10, run the run function here 
                elif user_choice == 10:
                    try:
                        # Instantiate Option11
                        option10_instance = Option10()
                        # Call the run method
                        option10_instance.run()
                    except Exception as e:
                        print(e)


                # if the option choosen is 11, run the run function here 
                elif user_choice == 11:
                    try:
                        option11 = Option11()  # Instantiate Option10 without passing arguments
                        option11.run(self.datas)
                    except Exception as e:
                        print(e)
                
                # if the option choosen is eight, run the run function here 
                elif user_choice == 12:
                    print(f'\nBye, thanks for using {userObj.get_moduleCode()} DSAA: Assignment Statement Evaluator & Sorter')
                    return
    



        

