# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement the node
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 4-Jan-2024
# Filename: stack.py
#
# ------------------------------------------------------------

# Creation of merge sort file here
class Node:

    ''' Setting the value left and right attribute'''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    ''' Check if its leaf'''
    def is_leaf(self):
        return self.left is None and self.right is None
    
    '''Overloading the print function'''
    def __str__(self):
        return self.value