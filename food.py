# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 19:44:03 2021

@author: erina
"""

from menu_item import Menu_Item

class Food(Menu_Item):              #継承したい親クラスを()に入れる
    def __init__(self, name, price, amount):
        super().__init__(name, price)       #親クラスと同じことをするならsuper.()変数名(引数)
        self.amount = amount
        
    def info(self):
        return self.name + ": " + str(self.price) + "円(" + self.amount + ")"