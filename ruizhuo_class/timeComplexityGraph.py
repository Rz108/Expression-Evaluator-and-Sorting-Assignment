# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to create the time complexity menu
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 04-Feb-2024
# Filename: timeComplexityGraph.py
#
# ------------------------------------------------------------


import time

# Generate the time complexity graph here
class ExpressionComplexity:
    '''
    Creating the init here to define the attributes
    '''
    def __init__(self, times, max_time, exp):
        self.real_time = times
        self.times = [int(t * 25000) for t in times]
        self.max_time = int(max_time* 25000)
        self.exp = exp
        self.fixed_height = 40

    '''Scale time if the values are too large for the terminal to handle'''
    def scale_times(self):
        max_actual_time = max(self.times)
        return [int(time / max_actual_time * self.fixed_height) for time in self.times]

    '''Get the plot here'''
    def get_plot(self):
        return self.__plot()

    '''Plot the graph here for visualisation'''
    def __plot(self):
        self.times = self.scale_times() if max(self.times) > 40 else self.times
        max_actual_time = max(self.times)
        times = 25000 if max(self.times) <= 40 else int(max_actual_time / max_actual_time * self.fixed_height) * 25000
        height = self.max_time + 3 
        width = len(self.times) * 2 + 1
        grid = [[' ' for _ in range(width)] for _ in range(height)]

        # Plot points
        for i, time in enumerate(self.times):
            grid[height - time - 3][i * 2 + 2] = '*'

        # Y-axis
        for i in range(2, height):
            grid[height - i - 1][1] = '|'

        # X-axis
        for i in range(2, width - 1):
            grid[height - 2][i] = '─'
        
        # X-axis labels
        for i, time in enumerate(self.times):
            grid[height - 1][i * 2 + 2] = str(i + 1)  
        
        # Y-axis labels
        for i in range(0, self.max_time + 1):
            label = str(i + 1).ljust(2)
            grid[height - i - 3][0] = label  

        grid[height - 2][1] = '-'
        grid[height - 1][0] = ' '
        print(f'Time ({times} seconds units)')

        # Print the plot
        for row in grid[:-2]:
            print('  '.join(row))
        
        print('    |'+'__'*50, 'No. of statements')
        print(' '+'  '.join(grid[-1][:20]) +'  '+ ' '.join(grid[-1][20:]))


    ''' Display the table below for insights'''
    def display_table(self):

        # Getting the expressions and sorting the time values
        expressions = self.exp
        sorted_times = sorted(self.real_time)
        rounded_values = [round(val, 6) for val in self.real_time]
        title = ("Index\tExpression\t\t\tResult")
        print(title)
        index = 1
        print('_'*53)

        # Printing out each line here
        for exp, time, results in zip(expressions,rounded_values , sorted_times):
            # Ensuring the expression is not longer than 30 characters
            exp_display = (exp[:27] + '...') if len(exp) > 30 else exp
            print(f"|{str(index).ljust(6)}{exp_display.ljust(36)}{str(time).ljust(9)}", ' '*(4 - len(str(results))) + '|')  
            index += 1
        print('|' + '_'*52 + '|')