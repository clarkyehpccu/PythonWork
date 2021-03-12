# -*- coding: utf-8 -*-
"""
賭盤:由骰子結果決定走幾步

@author: clark
"""
from tkinter import *
import random
import time
win=Tk()
win.geometry('600x600')
win.config(bg='darkgreen')
def moveSteps():
    global speed, step   
    if step == 0 :
       return
    global Merow, Mecolumn
    if (Merow ==0 and Mecolumn <4): #move right
        Mecolumn += 1
    elif (Mecolumn == 4  and Merow < 4 ):
        Merow += 1
    elif( Merow == 4   and Mecolumn >0 ):
        Mecolumn -= 1
    elif (Mecolumn == 0  and Merow > 0 ):
        Merow -= 1
    
    btnChess.grid(row=Merow, column=Mecolumn)
    step = step - 1
    
    win.after(1000,moveSteps)
    
def rolling():
    global diceImg , speed, circle_count , Merow, Mecolumn, step
    
    speed += 10
    circle_count += 1
    step = random.randint(1,6)
    Imagefile = r'D:\2020Python\我的範例\dice圖檔\dice' + str(step) +  '.png'
    
    diceImg= PhotoImage(file=Imagefile)
    dicebtn.config(image=diceImg)
    
    #print('count', circle_count, 'speed:', speed , 'Step:' , step)
    if circle_count == 20:
        #print('stepx', step)
        speed=10
        circle_count = 0 
        moveSteps()
        return
    win.after(speed,rolling)
 
              
def buildcircle():
    #-------
    for idx in range(5):
        btnh1 =Button(win,text=idx,width=15, height=7, bg='yellow')
        btnh1.grid(row=0, column=idx)
        #btnv1=Button(win,text=idx, width=15, height=7, bg='yellow')
        #btnv1.grid(row=idx, column=0)
        #btnv2=Button(win,text=idx, width=15, height=7, bg='yellow')
        #btnv2.grid(row=idx, column=4)
        btnh2 =Button(win,text=idx,width=15, height=7, bg='yellow')
        btnh2.grid(row=4, column=idx)
    for idx in range(1,5):
       
        btnv1=Button(win,text=idx, width=15, height=7, bg='yellow')
        btnv1.grid(row=idx, column=0)
        btnv2=Button(win,text=idx, width=15, height=7, bg='yellow')
        btnv2.grid(row=idx, column=4)
       
    #-------
   

def tick():
    global myrow, mycolumn
    if (myrow ==0 and mycolumn <4): #move right
        mycolumn += 1
    elif (mycolumn == 4  and myrow < 4 ):
        myrow += 1
    elif( myrow == 4   and mycolumn >0 ):
        mycolumn -= 1
    elif (mycolumn == 0  and myrow > 0 ):
        myrow -= 1
    btncursor.grid(row=myrow, column=mycolumn)
   
    win.after(100,tick)
myrow=mycolumn=0
buildcircle()
enter=0
Merow=Mecolumn=0
btnChess =Button(win,text="棋子",width=15,  height=7, bg='Brown', fg='White')
btnChess.grid(row=0, column=0)  

btncursor =Button(win,text="GO",width=15, height=7, bg='green', command=tick)
btncursor.grid(row=0, column=0)        

# place dice in the center
diceImg = PhotoImage(file=r'D:\2020Python\我的範例\dice圖檔\dice1.png')
step = 0
dicebtn = Button(win,  image=diceImg,  command=rolling)
dicebtn.grid(row=2, column=2)
speed=10
circle_count = 0    
win.mainloop()
