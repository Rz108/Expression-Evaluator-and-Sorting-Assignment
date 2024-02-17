# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement error class
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo , Bharathan Bhaskaran , Jonathan Leo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 4-Jan-2024
# Filename: error.py
#
# ------------------------------------------------------------

from classes.expressionManager import ExpressionManager
class Error:
    
    '''
    Validate the choices
    '''
    @staticmethod
    def validate_integer(inputs, minimum, maximum):
        try:
            value = int(inputs)
            # Check whether value input is within the range
            if not int(minimum) <= int(value) <= int(maximum):
                print(f'\nOnly values between {minimum} to {maximum} are available, please try again:\n')
                return None
            return value
        # Print other errors
        except Exception as e:
            print(f'\nOnly values between {minimum} to {maximum} are available, please try again:\n')
            return None
        
    '''
    Validate whether the encrypt or decrypt option is press
    '''
    @staticmethod
    def validate_option(self, option, valid):
        if option.lower() not in valid:
            print('Invalid option.')
            return False
        return True

    '''
    Set the option to validate whether integer is press
    '''
    @staticmethod
    def validate_integerType(num):
        try:
            num = int(num)
            return num
        except Exception as e:
            print("Invalid input. Please enter a valid integer.")
            return None
    
    '''
    check user input
    '''
    @staticmethod
    def validate_text(text):
        if len(text) == 0:
            return None
        else:
            return text
    
    '''
    Set the option to validate assignment is press
    '''
    @staticmethod
    def validateAssignment(exp):
        
        if exp == '':
            return '\nAssignment given is empty\n', False
        # If equal is not in the expression return the error message here
        if '=' not in exp:
            return '\nThe assignment given did not contain an equal sign here\n', False
        
        # If the expresssion count of equal more than 1 and return the error message here 
        if exp.count('=') > 1:
            return '\nThe assignment contains multiple equal sign, system does not support it \n',False

        # Split the equation after checking the statement is correct input
        var , eqn = exp.split('=',1)

        # If the left side is not a valid variable here 
        if '/0' in eqn:
            return '\nDivision by zero error will occur\n', False
        
        if not var.isalpha():
            return '\nThe left side of = must be a valid variable name here\n', False
        
        # If the variable is an integer here 
        if  var[0].isdigit():
            return '\nVariable name cannot begin with a value\n', False

        # If the equation is not starting or ending with a proper paramthesis
        if not(eqn.startswith('(') and eqn.endswith(')')):
            return '\nThe equation is not fully enclose in the paramthesis here.\n', False
        
        # If the count of paramthesis of left side and right side 
        if eqn.count('(') != eqn.count(')'):
            return '\nThe equation provided are not balance\n', False

        # The equation is empty here 
        if '()' in eqn:
            return '\nThe equation given is empty.\n', False
        
        # If double consective operation here is spotted , return the error message here
        for op in ['--','++','****','//']:
            if op in eqn:
                return '\nConsecutive operations are not allowed.\n', False
        
        # If the equation is started with an operator here
        if eqn[1] in '*/' or eqn[-2] in '+-*/' or  eqn[1:3] == '**' or eqn[-3:-1] == '**':
            return "\nEquation cannot start or end with an operator.\n",False
        
        # If the character is not valid here
        for char in eqn:
            if char.lower() not in '0123456789abcdefghilmnopqrstuvwxyz+-*/(). ':
                return  "\nInvalid character in equation\n", False
        
        # Handle equation where there is a=(a+2) for eg
        if var.strip() in eqn.replace(' ', ''):
                return f"\nVariable '{var.strip()}' cannot reference itself in the equation.\n", False

        # return no error message if good here
        return '',True

    
    '''
    Validate input paramthesis
    '''
    @staticmethod
    def validateInputParams(user_input):
        stack = []
        operators = set("+-*/**")

        for i, char in enumerate(user_input):
            if char == '(':
                # Push the index of '(' onto the stack along with an empty content list and a count of root-level operators
                # Use a list instead of a tuple to allow item assignment
                stack.append([i, [], 0, False])  # index, content list, operator count, flag for **
            elif char == ')':
                if not stack:
                    return False  # Unbalanced parentheses

                start_index, content, operator_count, prev_char_star = stack.pop()
                # Ensure there's exactly one root-level operator
                if operator_count != 1:
                    return False

            elif char in operators:
                if stack:
                    # Check if the operator is at the root level (not inside nested parentheses)
                    if char == '*' and stack[-1][3]:  # Handle ** operator
                        stack[-1][1].append(char)
                        stack[-1][2] += 1  # Increment root-level operator count
                        stack[-1][3] = False  # Reset flag for **
                    elif char != '*' or (char == '*' and not stack[-1][3]):  # Other operators or single *
                        stack[-1][1].append(char)
                        stack[-1][2] += 1  # Increment root-level operator count
                        stack[-1][3] = (char == '*')  # Set flag for ** if current char is *
            else:
                if stack:
                    # Append non-operator characters to the current content list
                    stack[-1][1].append(char)
                    stack[-1][3] = False  # Reset flag for ** if char is not an operator

        # If stack is not empty, parentheses are not balanced
        if stack:
            return False

        return True

    '''
    Validate circular dependency here to check
    '''
    @staticmethod
    def validateCircular(datas):
        m = ExpressionManager(datas)
        sorted_variables =   m.topologicalSort()

        # If circular dependency is detected 
        if type(sorted_variables) == str:
            return '\nCircular Dependency Occur\n', False
        
        # If no error here return no error
        return '',True



