# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to implement User Class
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 4-Jan-2024
# Filename: user.py
#
# ------------------------------------------------------------


class User:
    def __init__(self):
        # Setting the name and other infomation variable for start menu
        self.__name = None
        self.__admin_no = None
        self.__module_code = None
        self.__class = None
        self.__info = None
    
    '''
    Settting the name of the user
    '''
    def set_name(self, name):
        self.__name = name
    
    '''
    Setting the admin number of the user
    '''
    def set_adminNo(self, admin_no):
        self.__admin_no = admin_no
    
    '''
    Setting the module code of this project
    '''
    def set_moduleCode(self, module_code):
        self.__module_code = module_code

    '''
    Setting the class
    '''
    def set_class(self, className):
        self.__class = className

    '''
    Setting the infomation
    '''
    def set_info(self, info):
        self.__info = info

    '''
    Get the name of ther user
    '''
    def get_names(self):
        return self.__name
    
    '''
    Get the admin Number
    '''
    def get_adminNos(self):
        return self.__admin_no

    '''
    Get the module code
    '''
    def get_moduleCode(self):
        return self.__module_code
    
    '''
    Get the class
    '''
    def get_class(self):
        return self.__class
    
    '''
    Get the info
    '''
    def get_info(self):
        return self.__info

    '''
    Setting the overloading print function
    '''
    def __str__(self):

        # Setting the style of name when displaying it here

        namePairs = " &                     *\n*             ".join(
            f"{name}({admin_no})" for name, admin_no in zip(self.get_names(), self.get_adminNos())
        )

        namePairs = namePairs[:90] + namePairs[97:]
        
        # Return the the final style here
        return (f"\n{'*' * 59}\n* {self.get_info()} *\n{'*' + '-' * 57 + '*'}\n"
                f"{'*' + ' ' * 57 + '*'}\n"
                f"*  - Done by: {namePairs}{' ' * (23)}*\n"
                f"*  - Class: {self.get_class()}{' ' * (56 - len(self.get_class()) - 10)}*\n"
                f"{'*' + ' ' * 57 + '*'}\n"
                f"{'*' * 59}\n")

    

    

    
    

    

