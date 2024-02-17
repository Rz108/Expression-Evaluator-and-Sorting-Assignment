# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to create player menu
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 10-Jan-2024
# Filename: playerMenu.py
#
# ------------------------------------------------------------

# Creating the player menu class
class PlayerMenu:

    '''Create init here to define the game here'''
    def __init__(self, game):
        self.game = game
    
    ''' Display the menu for players '''
    def display_menu(self):

        # Inner menu here
        while True:
            print("\nPlayer Menu:")
            print("1. Display Points")
            print("2. Play Binary Level Game")
            print("3. Conversion to Assignment")
            print("4. Logout")
            choice = input("Enter your choice: ")

            # Input options here
            if choice == '1':
                self.show_score()
            elif choice == '2':
                self.game.play()
            elif choice == '3':
                self.game.play_two()
            elif choice == '4':
                self.game.login_system.logout()
                break
            else:
                print("Invalid choice. Please try again.")
    
    ''' Show the scores of the players '''
    def show_score(self):

        # Getting the scores of the current player
        player = self.game.login_system.current_player
        if player:
            print(f"{player.get_name()}'s current score: {player.get_score()}")
        else:
            print("No player is currently logged in.")
