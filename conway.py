"""
conway.py
Author: Rachel Matthew
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import RectangleAsset, Color, LineStyle, App

class Conway(App):
    def __init__(self):
        super().__init__()
        white=Color(0xfff0ff, 1.0)
        black=Color(0x000000, 1.0)
        nl=LineStyle(0, black)
        
myapp=Conway()
myapp.run()