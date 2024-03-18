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
    
    def __str__(self):
        return f'This User is: {self.name}'
        
    
    def __repr__(self):
        return f'User is: {self.name}'
    
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

if __name__ == '__main__':
    
    test = User('Test')
    bho = test.driver
    
    testUsers = generateUsers(['Rudy', 'Chiara'])
    
    for u in testUsers:
        print (u)



