"""
conway.py
Author: Rachel Matthew
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import RectangleAsset, Color, LineStyle, App, Sprite, ImageAsset
import time
states=[]

class Conway(App):
    def __init__(self):
        super().__init__()
        blank=Color(0xffffff, 0.0)
        thin=LineStyle(1, black)
        bg=RectangleAsset(1000, 500, thin, blank)
        Sprite(bg,(8.5, 32))
        for x in range(10):
            for n in range(5):
                z=str(str(x)+'_'+str(n))
                Cell((8.5+100*x, 32+100*n), z)
        print('To increase the population of a tile by one, click on it. To decrease the population by one, hold shift while you click.')
        print('')
        print('Press "Enter" to start')
        Conway.listenKeyEvent("keydown", "enter", self.start)
                
    def step(self):
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
    
    def start(self, event):
        cells=[]
        states=[]
        for cell in self.getSpritesbyClass(Cell):
            cells.append(cell.name)
            cell.check()
        index=zip(cells,states)
        print(list(index))
       
white=Color(0xfff0ff, 1.0)
black=Color(0x000000, 1.0)
nl=LineStyle(0, black)

class Cell(Sprite):
    asset=RectangleAsset(95,95,nl,white)
    def __init__(self, position, name):
        super().__init__(Cell.asset, position)
        self.name=name
        self.state=0
        self.shift=0
        self.statechange=0
        Conway.listenKeyEvent("keydown", "shift", self.shiftheld)
        Conway.listenKeyEvent("keyup", "shift", self.shiftrel)
        Conway.listenMouseEvent("click", self.edit)
    
    def step(self):
        if self.statechange!=0:
            self.state+=self.statechange
            self.statechange=0
            if self.state>0:
                DeadCell=RectangleAsset(95,95,nl,black)
                Sprite(DeadCell, (self.x, self.y))
                self.state=1
            else:
                LiveCell=RectangleAsset(95,95,nl,white)
                Sprite(LiveCell, (self.x, self.y))
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
    
    def check(self):
        n=0
        for x in range(len(self.name)):
            if list(self.name)[x]=='_':
                n=x
        xval=''
        yval=''
        for x in range(n):
            xval+=self.name[x]
        for x in range(len(self.name)-(n+1)):
            yval+=self.name[x+n+1]
        states.append(self.state)

myapp=Conway()
myapp.run()