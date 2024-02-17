# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to create a game with evaluting and understanding the binary tree level
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 10-Jan-2024
# Filename: games.py
#
# ------------------------------------------------------------


from .login import Login
from .player import Player
from .staff import Staff
from .playerMenu import PlayerMenu
from .staffMenu import StaffMenu


import json
import re
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'error')))
from error import Error
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'tools')))
from tools import Tools
import threading
import random
import time

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from classes.parseTree import ParseTreeBuilder

# Create the option game

class Game(Login):  
    '''
    Create a init with different attributes here and an inheritance to login here
    '''
    def __init__(self, login_system):
        super().__init__()
        self.time_limit = 60
        self.time_left = self.time_limit
        self.over = False
        self.level = 1
        self.login_system = login_system
        self._hints_given = 0
        self._hints_given_two = 0
    
    '''
    Create a get hint function here
    '''
    def get_hint(self):

        # Increment the hint given by 1 here
        self._hints_given += 1

        # If the hint is one give the first hint
        if self._hints_given == 1:
            return f"\nThe Expression Tree is a way to tell the level\n", 1
        
        # If the hint is two give the second hint
        elif self._hints_given == 2:
            return f"\nEach level is determine by a dot\n", 1
        
        # If the hint is three give the third hint
        elif self._hints_given == 3:
            return f"\nCount the number of dots for the target value\n", 1

    '''
    Create a get hint function here for second game
    '''
    def get_hint_two(self):
        
        # Increment the hint given by 1 here
        self._hints_given_two += 1

        # If the hint is one give the first hint
        if self._hints_given_two == 1:
            return f"\nThe Expression Tree is a way to tell the level, which leads to the paramthesis\n", 1
        
        # If the hint is two give the second hint
        elif self._hints_given_two == 2:
            return f"\nEach level is determine by a dot, which leads to the paramthesis\n", 1
        
        # If the hint is three give the third hint
        elif self._hints_given_two == 3:
            return f"\nCount the number of dots for the target value and therefore determine number of paramthesis\n", 1
    
    '''Select the count here'''
    def select(self):
        idx = random.randint(0, 19)  
        self.time_limit = max(60 - 5 * (self.level - 1), 10)
        self.time_left = self.time_limit
        return idx
    '''
    Get the json file that stores assigment
    '''
    def getjson(self):

        # Create an list here to store the assignments here
        arr = []

        # Try except block for different errors here
        try:

            # Open the assignment json file here
            with open('./ruizhuo_class/assignments.json', 'r') as json_file:

                # Load the data here
                data = json.load(json_file)

                # For each item here it is appended to the list
                for item in data:
                    arr.append(item)

            # Return the list
            return arr
        
        # Except block to check for file not fond error
        except FileNotFoundError:
            print(f"File not found")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    
    '''
    List all the players here but only staff can
    '''
    def list_all_players(self):

        # If they are a staff
        if isinstance(self.login_system.current_player, Staff):

            # List the players
            self.login_system.list_players()
        
        # Only staff level can read this
        else:
            print("Only staff members can view all players.")
    
    '''
    Show the scores of the current player
    '''
    def show_score(self):

        # This is the show score of the current player
        if self.login_system.current_player:
            print(f"{self.login_system.current_player.name}'s current score: {self.login_system.current_player.get_score()}")

        # This is where no player is logged in here
        else:
            print("No player is currently logged in.")

    '''
    Counting down the clock
    '''
    def count(self):

        # Starting from 60s it decreases everytime it runs
        for i in range(self.time_limit, -1 , -1):
            self.time_left = i
            if self.over:
                return
            
            # Here is to take note of the time
            time.sleep(1)
        
        # If the time is up here
        self.over = True

        # Reduce the score by 5
        print('\n Unfortunately, the time is up!')
        self.login_system.current_player.update(-5)

        # Show the score for the players now
        print(f'Score will be reduced. Your current score is: {self.login_system.current_player.get_score()}')

    '''
    Selecting the type of game they want to play
    '''
    def get_types(self, number):

        # Setting the over as false here
        self.over = False

        # Getting the data here
        data = self.getjson()

        # Setting the operations that we have
        operations = ['+','-','*','/','**']

        # Getting the data of statements
        statement = data[self.select()]

        # Split the data by key and value
        key , val = Tools.splitByEqual(statement)

        # Getting the values here
        values = re.findall(r'\*\*|[+\-*/()]|-?\d+\.\d+|-?\d+|[A-Za-z]+|\S', val)

        # Setting the values here
        f_vals = []
        for i in values:
            try:
                if '.' not in i:
                    f_vals.append(int(i))
                    continue
                f_vals.append(float(i))
                
            except ValueError:
                pass
        
        # If the selected option is game number 1
        if number == 1: 

            # Building the trees and setting the target value and level here
            x = ParseTreeBuilder(f'({val})')
            tree = x.build()
            tree.printInorder(0)
            target = f_vals[random.randint(0,len(f_vals) - 1)]
            level = x.get_level(tree, target)
            self.level = level
            return target, level

        # If the selected option is number 2
        else:

            # Setting the value and getting the required value here
            val = ''.join([i for i in val if i != ' '])
            x = ParseTreeBuilder(f'({val})')
            tree = x.build()
            tree.printInorder(0)
            return val

    '''
    Game one for user to play
    '''
    def play(self):

        # Setting the target and level
        target, level = self.get_types(1)
        while True:

            # Setting the amount of time here
            print(f'\nYou have {self.time_limit} seconds to solve this.')
            self.timer_thread = threading.Thread(target = self.count)
            self.timer_thread.start()
            hint_count = 0

            # The while loop for when the game is not over
            while not self.over:

                # Getting the user to input their answers
                user = input(f"Time left: {self.time_left}s. Enter your answer for this value: {target}, 'hint' for a hint, or 'answer' to reveal the answer: ")

                if self.time_left <= 0:
                    self.over=True
                    self.login_system.current_player.update(-5)
                    return
                # If user wants a hint
                if user == 'hint':

                    # If the hint count is more than or equal three, the game ends here
                    if hint_count >= 3:
                        print('Hint used up answer is level:', level)
                        self.login_system.current_player.update(-1)
                        self.login_system.store_user()
                        self.over = True
                    
                    # If the hint count still within three then it proceeds to get hint base on the hint count here and updates the score
                    else:
                        hint_message, penalty = self.get_hint()
                        print(hint_message)
                        self.login_system.current_player.update(-penalty)
                        self.login_system.store_user()
                        self.over = False

                        # Increment the hint count by 1 here
                        hint_count += 1
                        continue
                
                # User gives up in answeing
                elif user == 'answer':

                    # Showing user the answer and subtracting the remaining score of the quesion
                    print('Answer is level:', level)
                    self.login_system.current_player.update(-5 + hint_count )
                    self.login_system.store_user()
                    self.over = True
                    return
                
                else:

                    # Telling the user he scored corectly here
                    if  int(user) == level:
                        print(f'Correct! You solved the question in {self.time_limit - self.time_left} seconds. 10 points gained')
                        self.login_system.current_player.update(10)
                        self.login_system.store_user()
                        self.over = True
                        return

                    # If the user score inccorect it here it will prompt it to ansswer again
                    else:
                        print('Incorrect. Try Again!')
                        self.over = False
                        continue

                    # If time is up
                    if self.time_left <= 0:
                        print('The time is up. ')
                        self.over = True
                        break
                    
                self.timer_thread.join()
                return
        # Game for user to play
    

    def play_two(self):

        # Setting the required val here
        val = self.get_types(2)

        # Telling the user and starting the game here
        while True:
            print(f'\nYou have {self.time_limit} seconds to solve this.')
            self.timer_thread = threading.Thread(target = self.count)
            self.timer_thread.start()
            hint_count = 0

            # The while loop for when the game is not over
            while not self.over:

                # Telling the user their time and for their input
                user = input(f"Time left: {self.time_left}s. Convert this to an assignment (eg: a=(1+2)), 'hint' for a hint, or 'answer' to reveal the answer: ")
                
                # Checking when time left is less than 0
                if self.time_left <= 0:
                    self.over=True
                    self.login_system.current_player.update(-5)
                    return
                # If user wants a hint
                if user == 'hint':

                    # If the hint count is more than or equal three, the game ends here
                    if hint_count >= 3:
                        print(f'Hint used up answer is value:', {val})
                        self.login_system.current_player.update(-1)
                        self.login_system.store_user()
                        self.over = True
                    
                    # If the hint count still within three then it proceeds to get hint base on the hint count here and updates the score
                    else:
                        hint_message, penalty = self.get_hint_two()
                        print(hint_message)
                        self.login_system.current_player.update(-penalty)
                        self.login_system.store_user()
                        self.over = False
                        hint_count += 1
                        continue
                
                # User gives up in answeing
                elif user == 'answer':
                    print('Answer is :', f'({val})')
                    self.login_system.current_player.update(-5 + hint_count)
                    self.login_system.store_user()
                    self.over = True
                

                else:

                    # If the user score inccorect it here it will prompt it to ansswer again
                    if str(user) == f'({val})':
                        print(f'Correct! You solved the question in {self.time_limit - self.time_left} seconds. 10 points gained')
                        self.login_system.current_player.update(10)
                        self.login_system.store_user()
                        self.over = True
                    
                    # If the user score inccorect it here it will prompt it to ansswer again
                    else:
                        print('Incorrect. Try Again!')
                        self.over = False
                        continue
                    
                    # If time is up
                    if self.time_left <= 0:
                        print('The time is up. ')
                        self.over = True
                        break
                    
                self.timer_thread.join()
                return

    # Start the menu for player
    def start(self):
        player_menu = PlayerMenu(self)
        player_menu.display_menu()
    
