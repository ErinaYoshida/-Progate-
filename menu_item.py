# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:42:52 2021

@author: erina
"""

class Menu_Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def info(self):
        return self.name + ": " + str(self.price) + "円"
        
    def total_price(self, count):
        result = int(self.price) * count
        return result