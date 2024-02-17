# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: equationCleanup.py
#
#
# ------------------------------------------------------------

# Creating the equation clean up class here with the main use of inputing required paramthesis hgere
class EquationCleanup:

    '''
    Replacing all the space with empty space
    '''
    def __init__(self, exp):
        self.exp = exp[1:-1].replace(" ", "")

    '''
    Applying the operator here to aplly the last two operator to the last two values from the values stack
    '''
    def __applyOperator(self, ops, values):
        if ops:
            op = ops.pop()
            right = values.pop()
            left = values.pop()
            values.append(f'({left}{op}{right})')
    
    '''
    Checking the operator and encoding it to the value with the order of operation
    '''
    def __pre(self, op):
        if op == '**':
            return 3
        if op in ['*', '/']:
            return 2
        if op in ['+', '-']:
            return 1
        return 0
    
    '''
     Cleanup the equation here
    '''
    def evaluate(self):
        values = []
        ops = []
        i = 0

        # Handle negative or positive values at the start
        if self.exp[0] == '-':
            values.append('0')
        
        if self.exp[0] == '+':
            i += 1
        
        # While loop if the length is less than the length of expression
        while i < len(self.exp):

            # If the detected character is a digit or a float here and push to the stack
            if self.exp[i].isdigit() or (i > 0 and self.exp[i] == '.' and self.exp[i-1].isdigit()):
                j = i
                while j < len(self.exp) and (self.exp[j].isdigit() or self.exp[j] == '.'):
                    j += 1
                
                # This is to convert it to either a float or a integer depending on the type of it
                num_str = self.exp[i:j]
                num_val = float(num_str) if '.' in num_str else int(num_str)

                # Appending to the stack here
                values.append(str(num_val))
                i = j
            
            # IF the detected character is a exponent, then it will proceed to apply operator on the last two values with the use of apply operator 
            elif self.exp[i:i+2] == '**':
                while ops and self.__pre(ops[-1]) >= self.__pre(self.exp[i:i+2]):
                    self.__applyOperator(ops, values)
                
                # Appending it to the operations stack
                ops.append(self.exp[i:i+2])

                # Increment of 2 because of the operator ** containing two different characters
                i += 2
            
            # If the detected chracter is a usual operation it is also applied with apply operator here 
            elif self.exp[i] in ['+', '-', '*', '/']:
                while ops and self.__pre(ops[-1]) >= self.__pre(self.exp[i]):
                    self.__applyOperator(ops, values)

                # Appending it to the operations stack
                ops.append(self.exp[i])

                # Increment of 1 because of the operator containing only one character
                i += 1
            
            # If the detected character is a open paramthesis, it append the paramthesis into the operation stack
            elif self.exp[i] == '(':
                ops.append(self.exp[i])

                # Increment of 1 because of the operator containing only one character
                i += 1
            
             # If the detected character is a close paramthesis, it detects and until another opening paramthesis is seen, before applying the operator here
            elif self.exp[i] == ')':
                while ops and ops[-1] != '(':
                    self.__applyOperator(ops, values)
                
                ops.pop() 

                # Increment of 1 because of the operator containing only one character
                i += 1
            
            # IF the detected values is the others  such as it is a variable then it is appended into the values stack
            else:
                j = i
                while j < len(self.exp) and not self.exp[j] in ['+', '-', '*', '/', '(', ')', '.', ' ','**']:
                    j += 1
                word = self.exp[i:j]
                values.append(word)
                i = j 
        
        # If operation is not empty, apply last apply operation function to it
        while ops:
            self.__applyOperator(ops, values)
        return values[-1]

    '''
     Get clean up function as a getter 
    '''
    def get_cleanup(self):
        result = self.evaluate()
        return result
