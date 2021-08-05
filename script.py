# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 21:34:15 2021

@author: erina
"""
from menu_item import Menu_Item
from food import Food
from drink import Drink

menu_item1 = Food("からあげ", 540, "200g")
menu_item2 = Food("枝豆", 298, "100g")
menu_item3 = Food("ポテト", 350, "150g")
menu_item4 = Food("お刺身", 660, "100g")

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4] 


print("食べ物メニュー")

index = 0
for menu_item in menu_items:
    print(str(index) + ". " + menu_item.info())
    #menu_itemにはmenu_item1234が入る
    #menu_item1234はFood Classのインスタンスなので
    #menu_item.info()はfood.pyでオーバーライドしたものが使える
    #⇒読みにくいのでmenu_item...はfood...で書くべきだった
    index += 1

drink1 = Drink("ビール", 350, "5%")
drink2 = Drink("ハイボール", 450, "7%")
drink3 = Drink("レモンサワー", 350, "3%")
drink4 = Drink("チューハイ", 300, "3%")

drinks = [drink1, drink2, drink3, drink4]


print("飲み物メニュー")
for drink in drinks:
    #print(drink)
    print(str(index) + ". " + drink.info())
    index +=1


order = int(input("注文したいメニューの番号を入力してください"))
count = int(input("何個注文しますか?"))

if order < 4:
    pay = menu_items[order].total_price(count)
else:
    order -= 4
    pay = drinks[order].total_price(count)    


print("お会計は" + str(pay) + "円です")
