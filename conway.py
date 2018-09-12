"""
conway.py
Author: Rachel Matthew
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import RectangleAsset, Color, LineStyle, App, Sprite

class Conway(App):
    def __init__(self):
        super().__init__()
        blank=Color(0xffffff, 0.0)
        thin=LineStyle(1, black)
        bg=RectangleAsset(1000, 500, thin, blank)
        Sprite(bg,(8.5, 32))
        for x in range(50):
            for n in range(25):
                Cell((8.5+20*x, 32+20*n))
                
    def step(self):
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
       
white=Color(0xfff0ff, 1.0)
black=Color(0x000000, 1.0)
nl=LineStyle(0, black)

class Cell(Sprite):
    asset=RectangleAsset(20,20,nl,white)
    def __init__(self, position):
        super().__init__(Cell.asset, position)
        self.state=0
        Conway.listenKeyEvent("keydown", "space", self.on)
    
    def step(self):
        if self.state>0:
            print('k')
            self.fill=black
    def on(self, event):
        self.state=1
        
        
myapp=Conway()
myapp.run()