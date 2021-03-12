# -*- coding: utf-8 -*-
"""
期中考:2020-11-11
"""
import random
from tkinter import *
win = Tk()
win.geometry("1000x500")
win.config(bg='lightgreen')



#-----------------------------------------------------


displayShuffle = Button(win, text='(1)顯示洗牌結果')
displayShuffle.grid(row=0, column=0, sticky=W)

result = Text(win, width=20, height=20)
result.grid(row=1, column=0,  columnspan=3, sticky=E+W)
scroll1 = Scrollbar(win, command=result.yview)
scroll1.grid(row=1, column=3, sticky=N+S)

#-------------------------------------------------------

displayQueue = Button(win, text='(2)顯示2入5出排隊結果')
displayQueue.grid(row=0, column=1, sticky=W)
#-----------------------------------------------------


readFile = Button(win, text='(3讀取成績檔)')
readFile.grid(row=0, column=2, sticky=W)

win.mainloop()