# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement abstract data type in stack
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

# Creating the stack class
class Stack:
    def __init__(self):
        self.__list = []

    '''Stack is empty'''
    def isEmpty(self):
        return self.__list == []

    '''Size of stack'''
    def size(self):
        return len(self.__list)

    '''Removing all the elements'''
    def clear(self):
        self.__list.clear()

    '''Pushing the elements'''
    def push(self, item):
        self.__list.append(item)

    
    ''' Poping the elements'''
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.__list.pop()
    '''Get the last element'''
    def get(self):
        if self.isEmpty():
            return None
        else:
            return self.__list[-1]
    '''Overaloding of print function'''
    def __str__(self):
        output = '<'
        for i in range(len(self.__list)):
            item = self.__list[i]
            if i < len(self.__list) - 1:
                output += f'{str(item)}, '
            else:
                output += f'{str(item)}'
        output += '>'
        return output