# ------------------------------------------------------------
# ST1507 DSAA
# CA2 Assignment
#
# Write a Python program to create the user system class
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: userSystem.py
#
# ------------------------------------------------------------

import json
from .player import Player
from .staff import Staff
import random

class UserSystem:
    def __init__(self):
        self._users = self.__get_users()
        self._staff = self.__get_staff()
    
    ''' Store user'''
    def store_user(self):
        return self.__store_user()
    
    '''
     Store staff
     '''
    def store_staff(self):
        return self.__store_staff()

    ''' Get all the users'''
    def __get_users(self):
        try:
            with open('./ruizhuo_class/registered_players.json','r') as f:
                datas = json.load(f)
                dictionary_data = {}
                for data in datas:
                    dictionary_data[data['name']] = Player(data['name'], data['password'], data.get('score', 0))
                return dictionary_data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            return {}
    
    '''Get the staff'''
    def __get_staff(self):
        try:
            with open('./ruizhuo_class/registered_staff.json', 'r') as f:
                datas = json.load(f)
                dictionary_data = {}
                for data in datas:
                    dictionary_data[data['name']] = Staff(data['name'], data['password'], data.get('score', 0), data.get('access_level'))
                return dictionary_data
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    '''Private function for storing user'''
    def __store_user(self):
        with  open('./ruizhuo_class/registered_players.json','w') as f:
            players_data_dictionay = [{
                'name': user.get_name(), 'password':user.get_password(), 
                'score':user.get_score()
                
            } for user in self._users.values()]
            json.dump(players_data_dictionay,f, indent = 4)
    
    '''Private function for storing staff'''
    def __store_staff(self):
        with open('./ruizhuo_class/registered_staff.json', 'w') as file:
            staff_data = [
                {'name': staff.get_name(), 'password': staff.get_password(), 'score': staff.get_score(), 'access_level': staff.level}
                for staff in self._staff.values()
            ]
            json.dump(staff_data, file, indent=4)
    
    ''' List players'''
    def list_players(self):
        for user in self._users.values():
            print(f"{user.get_name()}: {user.get_score()} points")



