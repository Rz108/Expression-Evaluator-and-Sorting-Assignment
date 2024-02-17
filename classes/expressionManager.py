# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement expressionManager
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: expressionManager.py
#
# To run: expressionManager.py
# ------------------------------------------------------------

from .dependency import DependencyGraph
# Creating the manager here basing on the dependency graph
class ExpressionManager(DependencyGraph):

    '''
    Create a inherittance with dependency graph here and getting the datas as the attribute
    '''
    def __init__(self, datas):
        super().__init__(datas)
    
    '''
    Utilising topological sort here because to prevent circular dependency as it is able to detect it
    '''
    def topologicalSort(self):

        # Creating a list to store the final sorted variale here
        sorted_variables = []

        # Building the dependency graph here
        dependency_graph = self.build()

        # While the dependency graph here is not empty
        while dependency_graph:

            # Setting acyclic to false to detect any form of cyclic later on
            acyclic = False

            # Looping through the dependency graph 
            for var in list(dependency_graph):

                # For the dependency in each variable if it is in it then break
                for dep in dependency_graph[var]:
                    if dep in dependency_graph:
                        break
                
                # Acyclic is set to true and deletion of variable from the graph here
                else:
                    acyclic = True
                    del dependency_graph[var]

                    # Sorted variables append the new varaiable to be sorted
                    sorted_variables.append(var)

                    # Looping throguh the values in dependency graph, 
                    for deps in dependency_graph.values():

                        # If the variable in depededncy graph values, remove it here before breakling
                        if var in deps:
                            deps.remove(var)
                    break
            
            # Here this will detect the cycic dependency
            if not acyclic:
                return ("A cyclic dependency occurred")

        # Return the sorted variables to be evaluated
        return sorted_variables

    '''
    Replace the variable for with values once it is defined
    '''
    def replaceVar(self, exp,var_dict):

        # Split using tokenizer here
        tokens = exp.split()

        # Storing the result in a list here
        result = []

        # Looping throguh the tokens here 
        for token in tokens:

            # IF the token is seen in the variables storage, it is then appended into the result with the values of it
            if token in var_dict:
                result.append(str(var_dict[token]))
            
            # Else it will just append the original token here
            else:
                result.append(token)
        
        # Form the replaced satement throguh here
        new_exp = ' '.join(result)
        return new_exp


