# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement expression evaluator
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: expressionEvaluator.py
#
# ------------------------------------------------------------

# Create the expression evaluator class
class ExpressionEvaluator:

    '''
    creating the operations for evaluation
    '''
    def __init__(self):
        self.operations = {
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '**': lambda x, y: x ** y,
            '+': lambda x, y: x + y,
            '/': lambda x, y: None if y == 0 else x / y,
        }
    
    '''
   private function that evaluate and takes in node and variable values ehre
    '''
    def __evaluate(self,  node, variable_values):

        # If the not node.left and node.right  
        if not node.left and not node.right:

            # If int key ==  key mean that it is a integer
            # Define it to be an integer or else it is a float
            try:
                if int(node.key) == node.key:
                    return int(node.key)  
                return float(node.key)
            
            # Return none if none to be fond
            except ValueError:
                return variable_values.get(node.key, None)  

        # Evaluate the left and right node here using recursion as long as they exist
        left_val = self.__evaluate(node.left, variable_values) if node.left else None
        right_val = self.__evaluate(node.right, variable_values) if node.right else None

        # If the left and right are not none
        if left_val is not None and right_val is not None:

            # apply the operation
            operatorFunc = self.operations.get(node.key)

            # Return the operation result here
            return operatorFunc(left_val, right_val) if operatorFunc else None
        else:

            # Return none if does not exist
            return None
        
    '''
    creation of getter to get the results here
    '''
    def get_results(self ,  node, variable_values):
        return self.__evaluate( node, variable_values)
