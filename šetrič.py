from time import sleep
import time 
import os
from tkinter import *
from PIL import ImageTk, Image

class Window(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.width = 196
        self.height = 300
        self.velx = 1
        self.vely = 1
        self.pos = (250,250)
        self.geometry(f"{self.width}x{self.height}+{self.pos[0]}+{self.pos[1]}")

    def moveWin(self):
        x = self.pos[0] + self.velx
        y = self.pos[1] + self.vely
        downx, downy = x+self.width, y+self.height
        sWidth = self.winfo_screenwidth() 
        sHeight = self.winfo_screenheight() 
        if x <= 0 or downx >= sWidth:
            self.velx = -self.velx
        if y <= 0 or downy >= sHeight:
            self.vely = -self.vely
        self.pos = (x,y)
        self.geometry(f"+{x}+{y}")
        return [x, y, downx, downy]
        
root = Window()
frames = [PhotoImage(file='lebka.gif',format = 'gif -index %i' %(i)) for i in range(2)]
def update(ind):
    frame = frames[ind]
    ind += 1
    print(ind)
    if ind>1:
            ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root, bg= "white")
root.overrideredirect(True)
root.geometry("+250+250")
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")
label.pack()
root.after(0, update, 0) 
root.bind('<Escape>', lambda e, w=root: w.destroy())

while True:
    root.update()
    pos = root.moveWin()
    print(pos)
    sleep(0.01)