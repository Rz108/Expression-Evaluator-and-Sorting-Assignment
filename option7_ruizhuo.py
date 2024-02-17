# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement option 5
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: option5.py
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
from ruizhuo_class.timeComplexityGraph import ExpressionComplexity
from option2 import OptionTwo
from config import Configuration
from classes.equationCleanup import EquationCleanup
from ruizhuo_class.report import Report
from option1 import OptionOne
from classes.mergeSort import MergeSort
from timeit import default_timer as timer
import statistics

# Creating option seven here
class OptionSeven:

    '''Creating the init here with self.datas'''
    def __init__(self,datas):
        self.datas = datas

    '''Deleting the data function'''
    def delData(self):
        try:

            # Asking the users to select one assignment to delete here
            while True:
                print("Current assignments:\n")

                # Showing the users what are they
                for key, value in self.datas.items():
                    print(f"{key} = {value}")

                # Asking the users to input the variable
                userInput = input('Enter the variable to delete ("()") to return: ').strip()

                # Provdie return option here
                if userInput.lower() == '()':
                    return self.datas

                # If the user input is deleted and insight then deleted here
                if userInput in self.datas:
                    del self.datas[userInput]
                    print(f"Variable '{userInput}' has been deleted.")
                
                # Else it prompts the error message
                else:
                    print(f"Variable '{userInput}' not found.")

                # Ask the user whether they want to continue here
                cont = input('Do you want to continue deleting variables? (Y/N): ').lower()
                if cont in ['n', 'no']:
                    return self.datas

        except Exception as e:
            print(f"An error occurred: {e}")

    '''Creating the run function here'''
    def run(self,  boolean=True):

        # Creating the expression manager that takes in the data
        m = ExpressionManager(self.datas)

        # Utilise topological sort to sort dependency graph to order the vertices such that every edge is ordered
        sorted_variables =   m.topologicalSort()
        
        # Getting the values
        variable_values = {}
        
        # Getting the time taken here
        times = []
        ind_times = []
        time_taken = 0

        for var in sorted_variables:

            # Start the timer here
            start = timer()
            
            # Replacing the variables with values if it is already exist
            exp = m.replaceVar(self.datas[var], variable_values)

            # Cleanup the equation to include correct number of paramthesis
            exp = EquationCleanup(exp).get_cleanup()

            # Building the parse tree here to be able to evaluate next step
            tree = ParseTreeBuilder(exp).build()

            # Getting the results base on the expression evaluator class and get results methods
            value = ExpressionEvaluator().get_results(tree, variable_values)
            
            # End the timer here
            end = timer()
        
            # Store the value here
            variable_values[var] = value
            
            # Getting the time taken here
            elapsed = ( end - start)

            time_taken += elapsed 

            ind_times.append(elapsed)
            # Appending the time taken to the array here
            times.append((time_taken ))
        
        # Storing the time related information here
        time_var = {
            f'{key}={self.datas[key]}': val for key, val in zip(sorted_variables, times)
        }
        ind_time_var = {
            f'{key}={self.datas[key]}': val for key, val in zip(sorted_variables, ind_times)
        }
        # return of results here 
        return variable_values ,  time_var, ind_time_var

    ''' The full run here '''
    def full_run(self):
        try: 

            # Showing the menu here
            while True:
                print(f"\n{'*' * 33}\n* {Configuration['TimeComplexity']}\t*\n{'*' + ' ' * 31 +'*'}"
                      f"\n{'*' * 33}")

                print("\t1. Visualise the time complexity graph")
                print("\t2. Detailed Report")
                print("\t3. Add Data")
                print("\t4. Delete Data")
                print("\t5. Quit")

                # Getting the user option
                choice = input("\nEnter your choice: ")

                if choice in ['1', '2']:

                    # Check if data is not available
                    if len(list(set(self.datas.keys))) <= 6 or list(set(self.datas.keys))[0] is None:
                        print(f'\nNo enough data available ({len(list(set(self.datas.keys))) - 1}) Please add some more. Minimum 5')
                        continue
                    
                    # Check if too much data here
                    elif len(list(set(self.datas.keys))) > 16 or list(set(self.datas.keys))[0] is None:
                        print(f'\nToo much data here available ({len(list(set(self.datas.keys))) - 1}). Please remove some more. Maximum 15')
                        continue
                    
                    # Storing the overall reuslt here and individual result here
                    overall = []
                    idv_overall = []

                    # Computational times of 10000 here
                    print('In progress: a few seconds for computation')
                    for i in (range(10000)):

                        # Appending the info here
                        times = self.run(boolean=False)
                        overall.append(list(times[1].values()))
                        idv_overall.append(list(times[2].values()))

                    # Getting the statements here
                    statements = times[1].keys()

                    # Getting the key statistics here
                    mean_times = [(sum(times) / len(times)) for times in zip(*overall)]

                    idv_mean_times = [(sum(times) / len(times)) for times in zip(*idv_overall)]
                    idv_median_times = [(statistics.median(times)) for times in zip(*idv_overall)]
                    idv_std_dev_times = [(statistics.stdev(times)) for times in zip(*idv_overall)]

                    # Passing to the class here
                    expComp = ExpressionComplexity(mean_times, max(mean_times), statements)

                    # Visualisation of plot if option 1
                    if choice == '1':
                        print('\n**Visualisation Plot**')
                        expComp.get_plot()
                        print('\n\n**Table Data for reference**')
                        expComp.display_table()

                    # Visualisation of report for option 2
                    else:   
                        Report( list(statements) , idv_mean_times, idv_std_dev_times , idv_median_times).run_menu()

                # Running option one adding menu here
                elif choice == '3':
                    OptionOne(self.datas).run()

                # Running the deletion of data here
                elif choice == '4':
                    self.delData()

                elif choice == '5':
                    print("Goodbye!")
                    break

                else:
                    print("Please enter a valid option (1-5):")

        except Exception as e:
            print('Error:', e)




