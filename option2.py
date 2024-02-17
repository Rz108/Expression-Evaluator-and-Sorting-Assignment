# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement option 2
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: option2.py
#
#
# ------------------------------------------------------------

from tools import Tools
from classes.hashTable import hashTable
from classes.expressionEvaluator import ExpressionEvaluator
from classes.expressionManager import ExpressionManager
from classes.dependency import DependencyGraph
from classes.parseTree import ParseTreeBuilder
from classes.mergeSort import MergeSort
from classes.equationCleanup import EquationCleanup



# Creating Option Two
class OptionTwo:
    '''
    Creating the init with data call in init and also create an initialising an error
    '''
    def __init__(self,datas):
        self.datas = datas
    
    '''
    Creating the run funcion to run the code for option 1 with the checking of input statement 
    '''
    def run(self,  boolean=True):
        try:
            # Creating the expression manager that takes in the data
            m = ExpressionManager(self.datas)

            # Utilise topological sort to sort dependency graph to order the vertices such that every edge is ordered
            sorted_variables =   m.topologicalSort()
            
            # Getting the values
            variable_values = {}

            for var in sorted_variables:
                
                # Replacing the variables with values if it is already exist
                exp = m.replaceVar(self.datas[var], variable_values)

                # Cleanup the equation to include correct number of paramthesis
                exp = EquationCleanup(exp).get_cleanup()

                # Building the parse tree here to be able to evaluate next step
                tree = ParseTreeBuilder(exp).build()

                # Getting the results base on the expression evaluator class and get results methods
                value = ExpressionEvaluator().get_results(tree, variable_values)
            
                # Store the value here
                variable_values[var] = value
            
            # Use to provide inheritance for option 4
            if boolean:

                # Utilise merge sort to sort the values and items
                sorted_datas = MergeSort().sort( list(variable_values.items()))

                # Printing the results by looping through the sorted data
                for var, exp in sorted_datas:

                    # Printing out the statement here
                    print(f'{var}={self.datas[var]}=> {variable_values[var]}')
            
            # return of results here 
            return variable_values 
        
        except Exception as e:
            print(e)
            return