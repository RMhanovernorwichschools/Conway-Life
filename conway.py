"""
conway.py
Author: Rachel Matthew
Credit: <list sources used, if any>
Assignment:
Write and submit a program that plays Conway's Game of Life, per 
https://github.com/HHS-IntroProgramming/Conway-Life
"""
from ggame import RectangleAsset, Color, LineStyle, App, Sprite, ImageAsset
from time import time, wait
states=[]
xvals=[]
yvals=[]
index=[]

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
                Cell((8.5+100*x, 32+100*n), z, x, n)
        print('To increase the population of a tile by one, click on it. To decrease the population by one, hold shift while you click.')
        print('')
        print('Press "Enter" to start')
        Conway.listenKeyEvent("keydown", "enter", self.initiate)
                
    def refresh(self):
        for cell in self.getSpritesbyClass(Cell):
            cell.step()
            
    def initiate(self, event):
        time.wait(1)
        self.start()
    
    def start(self):
            global index
            index=[]
            xvals=[]
            yvals=[]
            states=[]
            for cell in self.getSpritesbyClass(Cell):
                xvals.append(cell.xval)
                yvals.append(cell.yval)
                states.append(cell.state)
                index=(list(zip(xvals, yvals, states)))
            for cell in self.getSpritesbyClass(Cell):
                cell.nextgen() 
            self.refresh()
            print('Cycle complete')
       
white=Color(0xfff0ff, 1.0)
black=Color(0x000000, 1.0)
nl=LineStyle(0, black)

class Cell(Sprite):
    asset=RectangleAsset(95,95,nl,white)
    def __init__(self, position, name, x, y):
        super().__init__(Cell.asset, position)
        self.name=name
        self.state=0
        self.shift=0
        self.statechange=0
        self.life=0
        self.xval=x
        self.yval=y
        Conway.listenKeyEvent("keydown", "shift", self.shiftheld)
        Conway.listenKeyEvent("keyup", "shift", self.shiftrel)
        Conway.listenMouseEvent("click", self.edit)
    
    def step(self):
        if self.statechange!=0 or self.life!=0:
            self.state+=(self.statechange+self.life)
            self.statechange=0
            self.life=0
            if self.state>0:
                LiveCell=RectangleAsset(95,95,nl,black)
                Sprite(LiveCell, (self.x, self.y))
            else:
                self.state=0
                DeadCell=RectangleAsset(95,95,nl,white)
                Sprite(DeadCell, (self.x, self.y))
    
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
        myapp.refresh()
        
    def nextgen(self):
        neighbors=0
        yval=int(self.yval)
        xval=int(self.xval)
        for x in index:
            if int(x[0])==xval and int(x[1])==(yval+1):
                neighbors+=x[2]
            if int(x[0])==xval and int(x[1])==(yval-1):
                neighbors+=x[2]
            if int(x[0])==(xval+1) and int(x[1])==(yval+1):
                neighbors+=x[2]
            if int(x[0])==(xval+1) and int(x[1])==(yval-1):
                neighbors+=x[2]
            if int(x[0])==(xval+1) and int(x[1])==(yval):
                neighbors+=x[2]
            if int(x[0])==(xval-1) and int(x[1])==(yval+1):
                neighbors+=x[2]
            if int(x[0])==(xval-1) and int(x[1])==(yval-1):
                neighbors+=x[2]
            if int(x[0])==(xval-1) and int(x[1])==(yval):
                neighbors+=x[2]
        if neighbors<2 or neighbors>3:
            self.life=-1
        elif neighbors==3:
            self.life=1

myapp=Conway()
myapp.run()
