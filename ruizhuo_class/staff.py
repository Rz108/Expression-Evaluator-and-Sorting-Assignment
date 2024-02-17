# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program for staff object
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: staff.py
#
# ------------------------------------------------------------

from .player import Player

class Staff(Player):
    '''
    Staff object that inherits from player but with higher level
    '''
    def __init__(self, name, password, score=0, level='staff'):
        
        super().__init__(name, password, score)
        self.level = level
    
