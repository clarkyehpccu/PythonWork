# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:48:55 2020

@author: Administrator
"""
from tkinter import *
import random
win=Tk()
win.geometry('500x500')
win.config(bg='darkgreen')

def changecolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    global rgb
    rgb=(r,g,b)
    btn.config(bg="#%02x%02x%02x" % rgb)
    win.after(200, changecolor)



diceimg = PhotoImage(file='dice\\dice1.png')
btn = Button(win, bg='red', image=diceimg,  text='Change Color',  command=changecolor)
btn.place(x=200, y=250)


win.mainloop()