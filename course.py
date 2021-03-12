# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:01:45 2019

@author: clark
"""
import sys
from tkinter import *
import myDB
db = myDB.DBclass("student.db")

def getAllData():
    sqlstr = " select course_id, course_name, credit "
    sqlstr += "  from course "
    
    #myset = list()
    myset = db.getSQLresult(sqlstr)
    datalist.delete(0,END)
    for idx, item in enumerate(myset, 0):
        #datalist.insert(END,"{0}-{1}-{2}".format(item[0],item[1], item[2]))
        datalist.insert(END, item)
def getitem(evt):
    selecteditem = datalist.get(datalist.curselection()[0])
    #selectedlist = selecteditem.split('-')
    #=== std_id ===
    course_id = selecteditem[0]
    course_name = selecteditem[1]
    credit = selecteditem[2]
    
    ecourse_id.delete(0,END)
    ecourse_name.delete(0,END)
    ecredit.delete(0,END)
    ecourse_id.insert(END, course_id)
    ecourse_name.insert(END, course_name)
    ecredit.insert(END,credit)
    
    
win = Tk()
win.geometry("600x520")
win.title('課程資料維護畫面')
win.config(background="lightyellow")
#-------
   
    

    
queryAll = Button(win)
queryAll.config(text="全部資料", bg="gray", fg="white", width=10, height=2, font="標楷體14", command=getAllData)
queryAll.grid(row=0, column=0, stick=W)
#--------
datalist = Listbox(win)
datalist.bind('<<ListboxSelect>>', getitem)
datalist.config(width=80, height=15)
datalist.grid(row=1, column=0, columnspan=4)

#------
myScrollbar = Scrollbar(win)
myScrollbar.grid(row=1, column=4, stick=N+S)
myScrollbar.config(command=datalist.yview)
#====================================================
#課號--------------------------
lcourse_id = Label(win, text="Course_Id")
lcourse_id.grid(row=2, column=0)
ecourse_id = Entry(win)
ecourse_id.grid(row=2, column=1, stick=W+E)
#課名----------------------------
lcourse_name = Label(win, text="Std Name")
lcourse_name.grid(row=2, column=2)
ecourse_name = Entry(win)
ecourse_name.grid(row=2, column=3, stick=W+E)
#---學分----
lcredit = Label(win, text="學分")
lcredit.grid(row=4, column=0)
ecredit = Entry(win)
ecredit.grid(row=4, column=1, stick=W+E)

#=====================
opFrame = Frame(win)
opFrame.grid(row=6, column=0, columnspan=4, stick=W+E)
#
def InsertCourse():
    sqlstr = " insert into course (course_Id, course_Name, credit)values("
    sqlstr +=db.Qo(ecourse_id.get()) + ","
    sqlstr +=db.Qo(ecourse_name.get()) + ","
    sqlstr += ecredit.get() + ")"
    db.execSQLcommand(sqlstr)
    getAllData()
    
opInsert = Button(opFrame)
opInsert.config(text="新增", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=InsertCourse)
opInsert.grid(row=0, column=0, stick=W+E)
def UpdateCourse():
    sqlstr = " update course set " # (Std_Id, Std_Name, sex, dep_id, Birth_Place, Birthday, Religion)values("
    sqlstr += "course_name = " + db.Qo(ecourse_name.get()) + ","
    sqlstr += "credit = " +  ecredit.get() 
    sqlstr += " where course_id = " +db.Qo(ecourse_id.get())
    db.execSQLcommand(sqlstr)
    getAllData()
opUpdate = Button(opFrame)
opUpdate.config(text="修改", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=UpdateCourse)
opUpdate.grid(row=0, column=1, stick=W+E)
#
def DeleteCourse():
    sqlstr = "delete from course where course_id = " +db.Qo(ecourse_id.get())
    db.execSQLcommand(sqlstr)
    getAllData()

opDelete = Button(opFrame)
opDelete.config(text="刪除", bg="gray", fg="blue", width=10, height=2, font="標楷體14", command=DeleteCourse)
opDelete.grid(row=0, column=2, stick=W+E)

import test
win.mainloop() 