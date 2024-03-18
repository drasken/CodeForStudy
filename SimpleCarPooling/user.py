#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:40:13 2024

@author: drasken
"""

class User:
    
    def __init__(self,name):
            self.name = name
            self.passenger = 0
            self.driver = 0
            
    
    def isDriver(self):
        self.driver += 1
    
    def isPassenger(self):
        self.passenger += 1
    
    def calculateBalance(self):
        return self.passenger - self.driver



def generateUsers(names:list[str]) -> list[User]:
    list_of_users = []
    for name in names:
        new_user = User(name)
        list_of_users.append(new_user)
    return list_of_users

if __name__ == 'main':
    
    test = User()
    bho = test.driver
    
    provaUsers = generateUsers(['Rudy', 'Chiara'])
    



