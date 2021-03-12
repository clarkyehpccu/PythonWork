
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
from tkinter import *
win = Tk()
win.geometry("665x700")
win.title('主畫面')
win.config(bg='brown')

def goCourse():
    import course
def goDepartment():
    import department    
def goStudent():
    import student
def goQuery():
    import query as newWin
    newWin.winQuery()
    
def goRecord():
    import record
    #exec('student.py') 
    #os.system('python student.py')
btnGoStd=Button(win,text='學生資料維護', height=3,font='微軟正黑體20', command=goStudent)
btnGoStd.grid(row=0, column=0, stick=E+W+N+S)


btnGoCourse=Button(win,text='課程資料維護',height=3,font='微軟正黑體20', command=goCourse)
btnGoCourse.grid(row=0, column=1 , stick=E+W)


btnGoDepartment=Button(win,text='學系資料維護', height=3,font='微軟正黑體20', command=goDepartment)
btnGoDepartment.grid(row=0, column=2, stick=E+W)

btnGoRecord=Button(win,text='成績資料維護', height=3,font='微軟正黑體20', command=goRecord)
btnGoRecord.grid(row=0, column=3, stick=E+W)

btnGoQuery=Button(win,text='查詢', fg='blue', height=3,font='微軟正黑體20', command=goQuery)
btnGoQuery.grid(row=1, column=0, columnspan=2, stick=E+W)

btnGoReport=Button(win,text='統計圖表', fg='blue', height=3,font='微軟正黑體20')
btnGoReport.grid(row=1, column=2, columnspan=2, stick=E+W)

lblLogo=Label(win)
img = PhotoImage(file='D:\\Onedrive\OneDrive - Chinese Culture University\\2019基礎程式設計-Python\\py\\SQLiteProj\\intro_logo.png')
lblLogo.config(image=img) #設Button圖形案件
lblLogo.grid(row=2, column=0, columnspan=4, stick=E+W)



win.mainloop()