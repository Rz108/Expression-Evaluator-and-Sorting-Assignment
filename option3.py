# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement option 3
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo, Jonathan Leo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: option3.py
#
#
# ------------------------------------------------------------

from tools import Tools
from classes.hashTable import hashTable
from classes.expressionEvaluator import ExpressionEvaluator
from classes.expressionManager import ExpressionManager
from classes.dependency import DependencyGraph
from classes.parseTree import ParseTreeBuilder

# Creating Option 3
class OptionThree:
    '''
    Creating the init with data call in init and also create an initialising an error
    '''
    def __init__(self,datas):
        self.datas = datas

    '''
    Creating the run funcion to run the code for option 1 with the checking of input statement 
    '''
    def run(self):

        # While loop  to check for error handling
        while True:

            # Get the user to key in the variable to evaluate
            variable = input('Please enter the variable you want to evaluate ("()" to return):\n')

            # If the user want to return
            if variable == '()':
                return

            # If the variable does not exist
            if variable not in self.datas.keys:
                print(f'\nNo variable of {variable} available.\n')
                continue
            
            # Creating the expression manager that takes in the data
            m = ExpressionManager(self.datas)

            # Utilise topological sort to sort dependency graph to order the vertices such that every edge is ordered
            sorted_variables =   m.topologicalSort()

            # replacing the variables with values if it exist
            variable_values = {}
            original_exp = m.replaceVar(self.datas[variable], variable_values)

            # Building the original parse tree
            original_tree = ParseTreeBuilder(original_exp).build()

            # Getting the values here
            for var in sorted_variables:
                
                # Replacing the variables with the values if defined
                exp = m.replaceVar(self.datas[var], variable_values)

                # Building the parse tree for evaluation
                tree = ParseTreeBuilder(exp).build()

                # Getting the value through the use of get results
                value = ExpressionEvaluator().get_results(tree, variable_values)

                # Storing the values here
                variable_values[var] = value

                # If the variable is the required variable, return
                if var == variable:

                    # Printint the expression tree
                    print(f'\nExpression Tree:')
                    original_tree.printInorder(0)

                    # Print the value heres
                    print(f'Value for "{variable}" is {value}')
                    return


