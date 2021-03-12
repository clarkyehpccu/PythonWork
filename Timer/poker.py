# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:06:45 2020

@author: clark
"""

from tkinter import *
import os
import random
#----存在否---
def ifExist(cardx):
    flag_exist = 0
    for idx in range(len(cardlist)):
        if cardx == cardlist[idx]:
            flag_exist = 1
            break
    return flag_exist
#----洗牌-----
def shuffle():
    count = 0
    while count < 52:
        cardtype = random.choice(['S', 'C' , 'D', 'H'])
        cardnum  = random.randint(1,13)
        cardx = cardtype+str(cardnum).strip()
        if ifExist(cardx) :
              continue
        else:
            cardlist.append(cardx)
            count += 1
    for idx in range(len(cardlist)):
        print(idx, cardlist[idx])
#--- 叫牌 -----
def calling(dir):
    global x_pos_l,y_pos_r,x_pos_r,y_pos_l
    filex = '\\2020Python\\我的範例\\poker圖檔\\' + cardlist[0]+'.png'
    global imgx
    imgx = PhotoImage(file=filex)
    imgbtn = Button(win, image=imgx)
    del cardlist[0] #pop
    if dir == 'L':
        imgbtn.place(x=x_pos_l, y = y_pos_l)
        #leftlist.append(imgbtn)
        y_pos_l += 50
    elif dir == 'R':
        imgbtn.place(x=x_pos_r,y=y_pos_r)
        #rightlist.append(imgbtn)
        y_pos_r += 50
   
    
win=Tk()
win.geometry('1000x500')
win.config(bg='darkgreen')

cardlist=[]
#leftlist=[]
#rightlist=[]
print(os.listdir('\\2020Python\\我的範例'))

#----- 中間的撲克牌 -------
filename="\\2020Python\\cover.PNG"
pokerCover = PhotoImage(file=filename)
cards = Button(win, image=pokerCover, command=shuffle)
cards.place(x=330, y=10)
#------ 左邊要牌 ---------
leftAsk=Button(win, text='Left Calling', width=20,command=lambda :calling('L'))
leftAsk.place(x=100, y=10)
#------ 右邊要牌 ---------
rightAsk=Button(win, text='Right Calling', width=20,command=lambda :calling('R'))
rightAsk.place(x=650, y=10)
#imgx = PhotoImage(file='\\2020Python\\我的範例\\poker圖檔\\c1.png')
x_pos_l = 100; y_pos_r = 40
x_pos_r = 650; y_pos_l = 40
win.mainloop()