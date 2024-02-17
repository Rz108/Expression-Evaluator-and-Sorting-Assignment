# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to create the staff menu
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 10-Jan-2024
# Filename: staffMenu.py
#
# ------------------------------------------------------------


class StaffMenu:
    '''
    Creating the login system for login system defined
    '''
    def __init__(self, login_system):
        
        self.login_system = login_system

    '''Display the menu for staff'''
    def display_menu(self):
        while True:
            print("\nStaff Menu:")
            print("1. List All Players")
            print("2. Logout")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.login_system.list_players()
            elif choice == '2':
                self.login_system.logout()
                break
            else:
                print("Invalid choice. Please try again.")