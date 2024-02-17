# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to create player object
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 10-Jan-2024
# Filename: player.py
#
# ------------------------------------------------------------

class Player:

    ''' Creating the init here'''
    def __init__(self, name, password, score = 0):

        # Player info with setting of name password and score
        self._name = name
        self.__password = password # Private variable
        self._score = score
    
    ''' Creating the update points system here'''
    def update(self, points):
        self._score += points

    ''' Getting the password here'''
    def get_password(self):
        return self.__password

    ''' Getting the score here'''
    def get_score(self):
        return self._score
    
    def get_name(self):
        return self._name