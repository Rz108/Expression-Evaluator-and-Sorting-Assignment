# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement parse tree
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo, Jonathan Leo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 4-Jan-2024
# Filename: parseTree.py
#
# To run: parseTree.py
# ------------------------------------------------------------

from .binaryTree import BinaryTree
from .stack import Stack
from .tokenizer import Tokenizer

# Creating the parse tree building here
class ParseTreeBuilder:
    '''Initialse the expression'''
    def __init__(self, exp):
        self.__exp = exp

    '''Building the parse tree method'''
    def build(self):

        # Initialise the tokenizer class here
        tokenizer = Tokenizer(self.__exp)

        # Get the tokens base on the get tokenize parse
        tokens = tokenizer.get_tokenize_parse()

        # If the tokens is a digit, character by itself, or a single variable
        if (len(tokens) == 3 and tokens[0] == '(' and tokens[2] == ')') or len(tokens) == 1:

            # Define a variable to hold the token value 
            token_value = tokens[1] if len(tokens) == 3 else tokens[0]

            # Try except block to handle if it is a float, integer, or a variable (string)
            try:
                # If token_value is a digit, convert it to int or float, else keep it as a string
                value = int(token_value) if token_value.isdigit() else float(token_value)
            except ValueError:
                # If it's not a digit or float, it might be a variable or a single character, so keep it as a string
                value = token_value

            # Return the binary tree with the value here
            return BinaryTree(value)
        
        # Define the stack here
        stack = Stack()

        # Define the binary tree here
        tree = BinaryTree('?')

        # Push the binary tree into the stack here
        stack.push(tree)

        # Set the current to the tree define above
        current = tree

        # Looping through the tokens
        for i in tokens:

            # IF the token is an opening paramthesis, insert left 
            if i == '(':
                current.insertLeft('?')

                # Push the current to the stack again
                stack.push(current)

                # Get the left key here
                current = current.get_left()
            
            # If it is an operation
            elif i in ['+', '-', '*', '/', '**']:

                # IF the current key here is set as '?'
                if current.get_key() == '?':

                    # Set the key here on the current
                    current.set_key(i)

                    # Proceed to insert the right side here 
                    current.insertRight('?')

                    # Push the current into the stack here
                    stack.push(current)

                    # Get the right key here
                    current = current.get_right()

                # Else if the current is empty
                else:

                    # Set a temporary binary tree here 
                    temp = BinaryTree(i)

                    # Insert left with the current 
                    temp.insertLeft(current)

                    # Proceed to insert right 
                    temp.insertRight('?')

                    # If the stack is still not empty
                    if stack:

                        # Get the last index here
                        parent = stack.get()

                        # If the parent left key is the current one
                        if parent.get_left() is current:

                            # Set the left child here to temp
                            parent.left = temp

                        # Set the right child here to temp
                        else:
                            parent.right = temp
                    stack.push(temp)
                    current = temp.get_right()
            
            # if it is not an operator
            elif i not in ['+', '-', '*', '/', '**', ')']:

                # Try except block to make sure the value are return in a correct format
                try:

                    # Integer
                    value = int(i)
                
                # Set for float or return the character
                except ValueError:
                    try:
                        value = float(i)
                    except ValueError:
                        value = i  

                # Set the value here to current
                current.set_key(value)

                # If the stack is still not empty set the current to thelast value of stack
                if stack:
                    current = stack.pop()
                
            # If it is the closing paramthesis here
            elif i == ')':

                # If the stack is still not emtpy pop the last element
                if stack:
                    current = stack.pop()
                

            # FInal check of invalid expression here
            else:
                return ("Invalid token in expression")
            
        # Return the tree here
        return tree
    
    '''
    Provide to get the level of parse tree here
    '''
    def get_level(self, root, target_value, current_level=0):

        # If the root is none return -1
        if root is None:
            return -1

        # Return the level here
        if root.get_key() == target_value:
            return current_level
        left_level = self.get_level(root.get_left(), target_value, current_level + 1)
        if left_level != -1:
            return left_level
        return self.get_level(root.get_right(), target_value, current_level + 1)




