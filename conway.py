"""
conway.py
Author: Rachel Matthew
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import RectangleAsset, Color, LineStyle, App, Sprite, ImageAsset

class Conway(App):
    def __init__(self):
        super().__init__()
        blank=Color(0xffffff, 0.0)
        thin=LineStyle(1, black)
        bg=RectangleAsset(1000, 500, thin, blank)
        Sprite(bg,(8.5, 32))
        for x in range(10):
            for n in range(5):
                Cell((8.5+100*x, 32+100*n))
                
    def step(self):
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
       
white=Color(0xfff0ff, 1.0)
black=Color(0x000000, 1.0)
nl=LineStyle(0, black)

class Cell(Sprite):
    asset=RectangleAsset(95,95,nl,white)
    def __init__(self, position):
        super().__init__(Cell.asset, position)
        self.state=0
        self.shift=0
        self.statechange=0
        DeadCell=RectangleAsset(95,95,nl,black)
        LiveCell=RectangleAsset(95,95,nl,white)
        Conway.listenKeyEvent("keydown", "shift", self.shiftheld)
        Conway.listenKeyEvent("keyup", "shift", self.shiftrel)
        Conway.listenMouseEvent("click", self.edit)
    
    def step(self):
        self.state+=self.statechange
        self.statechange=0
        if self.state>0:
            print(self.x)
        else:
            self.fill=white
            self.state=0
    
    def shiftheld(self, event):
        self.shift=1
    def shiftrel(self, event):
        self.shift=0
    
    def edit(self, event):
        if event.x>self.x and event.x<(self.x+95) and event.y>self.y and event.y<(self.y+95):
            if self.shift==0:
                self.statechange=1
            else:
                self.statechange=-1
        
myapp=Conway()
myapp.run()