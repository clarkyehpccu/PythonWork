# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 19:42:03 2020

@author: Administrator
"""
from tkinter import *
wincampus = Tk()
wincampus.geometry('300x150')
wincampus.config(bg='lightgreen')
def goCourse():
    import course
def goStudent():
    import student
   
def goRecord():
    pass
btnCourse = Button(wincampus, width=30, text='課程編修', command=goCourse)
btnCourse.grid(row=0, column=0, sticky=W+E)

btnStudent = Button(wincampus, text='學生資料編修', command=goStudent)
btnStudent.grid(row=1, column=0, sticky=W+E)

btnRecord = Button(wincampus,fg = 'red',  text='成績編修', command=goRecord)
btnRecord.grid(row=3, column=0, sticky=W+E)

wincampus.mainloop()
