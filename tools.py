# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement program tools
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo , Bharathan Bhaskaran , Jonathan Leo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 4-Jan-2024
# Filename: tools.py
#
# ------------------------------------------------------------
'''
Reasons for static method here: the use of tools class are not correlated 
        so by putting it as a class function it is not suitable and does not make sense
'''


import os
from error import Error
class Tools:
    '''
    Set the split by equal file method here as static method
    '''
    @staticmethod
    def splitByEqual(statement):
        key, value = statement.split('=',1)
        return key.strip(), value.strip()

    '''
    Set the open file method here as static method
    '''
    @staticmethod
    def open_file( path):
        # If file has a wrong type
        if not path.endswith('.txt'):
            print(f'File with ".txt" are supported only.')
            return None
        
        # If file does not exist
        if not os.path.exists(path):
            print(f'File {path} does not exist')
            return None
        
        # If the file is empty, prompt the user again
        if os.stat(path).st_size == 0:
            print('File is empty. Please try again.')
            return None
        
        # Try opening the file
        try:
            with open(path, 'r') as f:
                return f.read()
        # Unexpected error handling
        except Exception as e:
            print('Unexpected error occured')
            return None
    
    '''
    Set the write file method here as static method
    '''
    @staticmethod
    def write_file(path, text):
        with open(path, 'w') as f:
            f.write(text)
    
    '''
    Set the get valid integer method here as static method
    '''
    @staticmethod
    def get_valid_integer(prompt):
        while True:
            user_input = input(prompt)
            valid = Error.validate_integerType(user_input)
            if valid is not None:
                return valid
