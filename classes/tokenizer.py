# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement tokenizer
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 27-Jan-2024
# Filename: tokenizer.py
#
# ------------------------------------------------------------

# Creating the tokenizer class here
class Tokenizer:

    '''Initialse the index to track the current position in th eexprerssion and the expression'''
    def __init__(self, exp):
        self.exp = exp  
        self.index = 0  

    '''
    Tokenizer 1 based on the alphabet characters
    '''
    def __tokenize1(self):
        
        # List to store the tokens
        tokens = []  

        # String to get the current token
        current_token = ''  

        # For loop to check for the accurate tokens
        for char in self.exp:

            #  if it is an alphabet characters add alphabetic characters 
            if char.isalpha():
                current_token += char  
            else:

                # if current token is still not empty adding the completed token to the list of tokens 
                if current_token:
                    tokens.append(current_token)  

                    # Reset current token
                    current_token = ''  

         # If current token still exist add the last token 
        if current_token:
            tokens.append(current_token) 

        # Return the list of tokens here
        return tokens  

    '''
    Tokenizer 1 based on alphanumeric characters and underscores, and special characters here
    '''
    def __tokenize2(self):

        # Set the tokens list, current tokens string and the set of special chracters
        tokens = []
        current_token = ''
        special_characters = {'+', '-', '*', '/', '(', ')', ' ', '**'} 
        
        # For loop to loop throguh the expression
        for char in self.exp:

            # If it is an alphanumeric characters or underscores, it appends to the current tokens string
            if char.isalnum() or char == '_':
                current_token += char  
            
            # Else 
            else:
                # if current token is still not empty adding the completed token to the list of tokens 
                if current_token:
                    tokens.append(current_token)  

                    # Reset current token
                    current_token = ''  
                
                # If character in special characters, just append the character
                if char in special_characters:
                    tokens.append(char)  
        
        # If current token still exist add the last token 
        if current_token:
            tokens.append(current_token) 

         # Return the list of tokens
        return tokens 

    '''
    Tokenizer 1 getter to get base on dependency for depedency graph here
    '''
    def get_tokenize_dep(self):
        return self.__tokenize1()
    
    '''
    Tokenizer 1 getter to get base on replace variable here
    '''
    def get_tokenize_rv(self):
        return self.__tokenize2()
    
    '''
    Tokenizer 1 getter to get base on parse tree here
    '''
    def get_tokenize_parse(self):
        # Public method to access __tokenize3
        return self.__tokenize3()
    
    '''
    Returns the next character in the expression and increment the index
    '''
    def __next_char(self):

        # If the current index is less than the length of expression
        if self.index < len(self.exp):

            # Getting the character base on the index
            char = self.exp[self.index]

            # Increment the index by 1
            self.index += 1

            # Return the character
            return char
        
        # Return none here if the end of the expression 
        return None  

    '''
    Returns the next character in the expression and without increasing the index
    '''
    def __peek_char(self):

        # If the current index is less than the length of expression
        if self.index < len(self.exp):
            return self.exp[self.index]
        
        # Return none here if the end of the expression 
        return None  

    '''
    Get the next token here by identifying the numbers, operators and variables
    '''
    def get_next_token(self):
        
        # While loop such that when the index is less than the length of expression to skip whitespace here
        while self.index < len(self.exp) and self.exp[self.index].isspace():

            # Increment the index by 1 here
            self.index += 1 

        # if the index is at the end here
        if self.index == len(self.exp):

            # Return none here
            return None  

        # Get the character base on the index
        char = self.exp[self.index]

        # If the exponenet character here, return ** and increment the index by 2
        if char == '*' and self.index + 1 < len(self.exp) and self.exp[self.index + 1] == '*':
            self.index += 2
            return '**'
        
        # If the character is the other chracters
        if char in '+-*/()':
            
            # Increment the index by 1 and return the chracter
            self.index += 1
            return char
        
        # If the character is a digit here or float here
        if char.isdigit() or (char == '-' and self.index + 1 < len(self.exp) and self.exp[self.index + 1].isdigit()):
            
            # Set the start index and increment the index by 1
            start_index = self.index
            self.index += 1

            # while the index is less than lemgth and it is still digits or floats
            while self.index < len(self.exp) and (self.exp[self.index].isdigit() or self.exp[self.index] == '.'):

                # Increment the index by 1
                self.index += 1
            
            # Return the expression from start index to the current index - 1
            return self.exp[start_index:self.index]

        # If the chracter is an alphabet
        if char.isalpha():
            
            # Set the start index here
            start_index = self.index

            # Increment the index by 1 here
            self.index += 1

            # while loop to check as long as it is a alphabet here
            while self.index < len(self.exp) and self.exp[self.index].isalnum():
                self.index += 1

            # Return the expression from start index to the current index - 1
            return self.exp[start_index:self.index]
        
        # Return the chracter if it is not a space and increment the index by 1
        if not char.isspace():
            
            self.index += 1
            return char
        
        # Return none if no valid token is found
        return None  

    '''
    Tokenizes the expression using the get method  
    '''  
    def __tokenize3(self):

        # Store the tokens in a list
        tokens = []

        # Looping through the possible tokens
        while True:
            token = self.get_next_token()

            # If no more tokens are found, break the loop
            if token is None:
                break  

            # Append it to the tokens list
            tokens.append(token)  

        # Return the list of tokens
        return tokens  
