# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 21:34:15 2021

@author: erina
"""
from menu_item import Menu_Item

menu_item1 = Menu_Item("からあげ", 540)
menu_item2 = Menu_Item("枝豆", 298)
menu_item3 = Menu_Item("ポテト", 350)
menu_item4 = Menu_Item("お刺身", 660)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4] 

print("食べ物メニュー")

index = 0
for menu_item in menu_items:
    print(str(index) + ". " + menu_item.info())
    index += 1

order = int(input("注文したいメニューの番号を入力してください"))
count = int(input("何個注文しますか?"))

pay = menu_items[order].total_price(count)

print("お会計は" + str(pay) + "円です")
