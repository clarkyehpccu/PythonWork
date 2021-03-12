# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 19:42:03 2020

@author: Administrator
"""
from tkinter import *
finalmain = Tk()
finalmain.geometry('300x150')
finalmain.title("主畫面")
finalmain.config(bg='lightgreen')
def goJson():
    import water_read
def goEdit():
    import water_edit
   
def goRecord():
    pass
btnCourse = Button(finalmain, width=30, text='讀取網站資料', command=goJson)
btnCourse.grid(row=0, column=0, sticky=W+E)

btnStudent = Button(finalmain, text='單筆資料編修', command=goEdit)
btnStudent.grid(row=1, column=0, sticky=W+E)

btnRecord = Button(finalmain,fg = 'red',  text='統計圖表', command=goRecord)
btnRecord.grid(row=3, column=0, sticky=W+E)

finalmain.mainloop()
