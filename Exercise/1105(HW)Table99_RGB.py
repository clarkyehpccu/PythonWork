# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 18:41:42 2020

@author: Administrator
"""

from tkinter import *
win=Tk()
win.geometry('800x500')
win.config(bg='lightgreen')


def table99(self):
    outs = ""
    text.delete(0.0, END)
    for x in range(1,scalex.get()+1):
        for y in range(1,scaley.get()+1):
            outs += str(x) + " X " + str(y) + " = " + str(x*y) + '\n'
    text.insert(0.0, outs)


label1 = Label(win, text='x:')
label1.grid(row=0, column=0)

scalex = Scale(win, from_=1, to_=100, orient=HORIZONTAL, command=table99)
scalex.grid(row=0,column=1, sticky=W+E)

label2 = Label(win, text='y:')
label2.grid(row=1, column=0)

scaley = Scale(win, from_=1, to_=100, orient=HORIZONTAL, command=table99)
scaley.grid(row=1,column=1, sticky=E+W)

text = Text(win, width=50, height=20)
text.grid(row=2, column=0, columnspan=2)

scroll = Scrollbar(win, command=text.yview)
scroll.grid(row=2, column=2, sticky=N+S+W)

def rgbcolor(self):
    r = colorR.get()
    g = colorG.get()
    b = colorB.get()
    global rgb
    rgb=(r,g,b)
    colorBox.config(bg="#%02x%02x%02x" % rgb)
colorR = Scale(win, from_=0, to_=255, orient=HORIZONTAL, command=rgbcolor); colorR.grid(row=4, column=0)
colorG = Scale(win, from_=0, to_=255,  orient=HORIZONTAL,command=rgbcolor); colorG.grid(row=4, column=1)
colorB = Scale(win, from_=0, to_=255,  orient=HORIZONTAL,command=rgbcolor); colorB.grid(row=4, column=2)
colorBox=Button(win, width=15, height=5)
colorBox.grid(row=5, column=0, columnspan=3, sticky=W+E)

win.mainloop()