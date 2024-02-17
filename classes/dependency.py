# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement the depency graph
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: dependency.py
#
#
# ------------------------------------------------------------

from .tokenizer import Tokenizer

# Creating the dependency graph here
class DependencyGraph:
    '''
    Creating the initialiser here of data and the graph
    '''
    def __init__(self, datas):
        self.datas = datas
        self.graph = {var: [] for var, exp in self.datas.items() if var is not None}
    

    '''
    Creating the adding of var and experience here
    '''
    def add(self, var, exp):
        self.graph[var] = self.__findDependency(exp)

    '''
    Creating the find dependency here 
    '''
    def __findDependency(self, exp):
        tokenizer = Tokenizer(exp)
        t = tokenizer.get_tokenize_dep()
        return t

    '''
    Creating the get here to get varaible from the graph
    '''
    def get(self,var):
        return self.graph.get(var, None)
    
    '''
    Creating the building of dependency graph here
    '''
    def build(self):

        # For each variable and expression
        for var, exp in self.datas.items():

            # Find each dependcy here depending on the expression
            tokens = self.__findDependency(exp)
            for token in tokens:

                # If the token is a alphabet and not the same as var append it to the dependency array
                if token.isalpha() and token != var:
                    self.graph[var].append(token)
        return self.graph

    # Overwriting print function here
    def __str__(self):
        return str(self.graph)