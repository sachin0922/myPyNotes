# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:00:00 2019

@author: sachin0922
"""

class Greeter(object):
    
    lastName=""
    
    def __init__(self,name):
        self.name=name
        self.lastName=" Champ"
    
    def sayHi(self):
        print("Hi "+self.name+self.lastName)
    def sayBye(self):
        print("Bye "+self.name+self.lastName)
        
