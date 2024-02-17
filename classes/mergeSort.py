# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement merge sort
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 6-Jan-2024
# Filename: mergeSort.py
#
# ------------------------------------------------------------

# Creation of merge sort file here
class MergeSort:
    ''' Setting the init here'''
    def __init__(self):
        self.count = 0
    
    def sort(self,l):
        # Checking that the array is indeed not empty
        if len(l) > 1:

            # Splitting the array into two different halves
            mid = len(l) // 2
            left = l[:mid]
            right = l[mid:]

            # sort both halves
            self.sort(left)
            self.sort(right)

            # Setting the index first
            l_index, r_index, m_index = 0, 0, 0

            # Setting a temporary copy here
            mergeList = l

            # While the left index and right index less than it respective array length
            while l_index < len(left) and r_index < len(right):

                # String both to covnert them to letters
                # COmpare the words base on uppering their case
                # If left less than right then the merge will input the left value and the left index increment by 1
                if type(left[l_index]) in (int,float):
                    if left[l_index] < right[r_index]:
                        mergeList[m_index] = (left[l_index])
                        l_index += 1
                    else:
                    # The right index will then increment by 1 and added to the merge list
                        mergeList[m_index] = right[r_index]
                        r_index += 1
                
                elif type(left[l_index][0]) == str or type(right[r_index][0]) == str :
                    if str(left[l_index][0].upper()) < str(right[r_index][0].upper()):
                        mergeList[m_index] = (left[l_index])
                        l_index += 1
                    else:
                    # The right index will then increment by 1 and added to the merge list
                        mergeList[m_index] = right[r_index]
                        r_index += 1


                
                # Increment of merge list index
                m_index += 1
            
            # Handle of remaing values in the left list 
            while l_index < len(left):
                # insert to the merge list base on the left index
                mergeList[m_index] = left[l_index]
                l_index += 1
                m_index += 1
            
            while r_index < len(right):
                # insert to the merge list base on the right index
                mergeList[m_index] = right[r_index]
                r_index += 1
                m_index += 1
        return l