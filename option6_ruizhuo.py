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
from ruizhuo_class.login import Login
from ruizhuo_class.games import Game
from ruizhuo_class.staff import Staff
from ruizhuo_class.staffMenu import StaffMenu
from config import Configuration
from error import Error

# Setting the options siz here
class OptionSix:
    def __init__(self):
        pass
        
    def run(self):
        try: 

            # Login system
            login_system = Login()

            # Create the game and staff menu
            game = Game(login_system)
            staff_menu = StaffMenu(login_system)

            # Inner menu
            while True:
                print(f"\n{'*' * 33}\n* {Configuration['Game']}\t*\n{'*' + ' ' * 31 +'*'}"f"\n{'*' * 33}")
                
                # Options provided
                print("\t1. Register as Player")
                print("\t2. Login as Player")
                print("\t3. Login as Staff")
                print("\t4. Quit")

                # Input choice for user
                choice = input("\nEnter your choice : ")

                # Choice options
                if choice == '1':
                    login_system.register(staff=False)
                elif choice == '2':

                    # Starting the game
                    if login_system.login(staff=False):
                        game.start() 

                # Starting game two here
                elif choice == '3':
                    if login_system.login(staff=True):
                        staff_menu.display_menu()

                # Ending the program here
                elif choice == '4':
                    print("Goodbye!")
                    break
                else:
                    print("Only values between 1 to 4 are available, please try again:")
        except Exception as e:
            print(e)