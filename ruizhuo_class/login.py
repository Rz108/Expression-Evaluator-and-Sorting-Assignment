# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to create the login system
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 10-Jan-2024
# Filename: login.py
#
# ------------------------------------------------------------

from .userSystem import UserSystem
from .player import Player
from .staff import Staff
import hashlib
import getpass
import random

class Login(UserSystem):

    ''' Setting the init here with inheritance to user system here'''
    def __init__(self):
        # Inheritance with usersystem
        super().__init__()
        self.current_player = None
    
    '''Registration for users'''
    def register(self, staff=False):

        # Input their credentials
        name = input('\nEnter your name: ')
        password = input('\nEnter your password: ')
        confirm  = input('Enter password agin: ')

        # Check whether password matches

        if password != confirm or name == '' or password == '' or confirm == '':
            print('Registration not successful')
            return False

        # Hasing of password for storage
        hashed_password = self.hashing(password)

        # IF the staff is registering
        if staff:

            # If staff in the data
            if name in self._staff:
                print("A staff member with that name already exists.")
                return False
            
            # Creating a new staff
            new_staff = Staff(name, hashed_password)
            self._staff[name] = new_staff

            # Store the staff
            self.store_staff()
            print(f"Staff member {name} registered successfully.")
            return True
        
        # If registration for players
        else:
            if name in self._users:
                print("A player with that name already exists.")
                return False

            # New player object created
            new_player = Player(name, hashed_password)
            self._users[name] = new_player

            # Stored successfully
            self.store_user()
            print(f"Player {name} registered successfully.")
            return True
    

    '''Create the login function here'''
    def login(self, staff=False): 

        # Input credentials
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        # Get the user dictionaiory
        user_dict = self._staff if staff else self._users

        # Get the nasme
        user = user_dict.get(name)
        hashed_password = self.hashing(password)
        # Set the current player / staff
        if user and user.get_password() == hashed_password:
            self.current_player = user
            print(f"Welcome back, {'staff' if staff else 'player'} {name}!")
            return True
        else:
            print("Invalid credentials.")
            return False

    '''Create the show points function here'''
    def show_points(self):
        if self.current_player:
            print(f"Your current points are: {self.current_player.get_score()}")

    '''Create the logout function here'''
    def logout(self):
        if self.current_player:
            print(f"{self.current_player.get_name()} has been logged out.")
            self.current_player = None
        else:
            print("No user is currently logged in.")
    
    '''method for hashing here '''
    def hashing(self, pwd):
        hash = hashlib.sha256()
        hash.update(pwd.encode('utf-8'))
        return hash.hexdigest()

