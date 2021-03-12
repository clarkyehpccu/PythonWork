# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:41:21 2020

@author: Administrator
"""

from tkinter import *
import sqlite3
def execSQLcommand(sqlstr):
    global myConn
    global myCursor
    try:
      myCursor = myConn.execute(sqlstr)
      myConn.commit()
      print("指令已成功執行:" + sqlstr)
      return myCursor
    except:
      print("指令有誤:", sqlstr)
myConn = sqlite3.connect("student.db")
myCursor = myConn.cursor()

win = Tk()
win.geometry('500x500')
lblcourse_id = Label(win, text='Course_id')
lblcourse_id.grid(row=0, column=0)
etycourse_id=Entry(win)
etycourse_id.grid(row=0, column=1)

lblcourse_name = Label(win, text='Course_Name')
lblcourse_name.grid(row=1, column=0)
etycourse_name=Entry(win)
etycourse_name.grid(row=1, column=1)

lblcredit = Label(win, text='Course_Name')
lblcredit.grid(row=2, column=0)
etycredit=Entry(win)
etycredit.grid(row=2, column=1)
def  qo(instr):
     return "'" + instr +"'"
def getAll():
    sqlstr = "select * from course "
    listx = execSQLcommand(sqlstr).fetchall()
    resultList.delete(0, END)
    for item in listx:
        resultList.insert(0, item)
def doInsert():
    sqlstr = "insert into course(course_id, course_name, credit)"
    sqlstr += "values(" + qo(etycourse_id.get()) + ","
    sqlstr +=  qo(etycourse_name.get()) + ","
    sqlstr +=  etycredit.get() + ")"
    execSQLcommand(sqlstr)
    getAll()
def doUpdate():
    sqlstr = " update course set"
    sqlstr += " course_name = " + qo(etycourse_name.get())
    sqlstr += ", credit = " + etycredit.get()
    sqlstr += " where course_id = " + qo(etycourse_id.get())
    execSQLcommand(sqlstr)
    getAll()
def doDelete():
    sqlstr = " delete from course"
    sqlstr += " where course_id = " + qo(etycourse_id.get())
    execSQLcommand(sqlstr)
    getAll()
btnInsert = Button(win, text='Insert', fg='blue', command=doInsert)
btnInsert.grid(row=0,column=2, sticky=W+E)
btnUpdate = Button(win, text='Update', fg='blue', command=doUpdate)
btnUpdate.grid(row=1,column=2, sticky=W+E)
btnDelete = Button(win, text='Delete', fg='blue', command=doDelete)
btnDelete.grid(row=2,column=2, sticky=W+E)

def onselect(evt):
    idx = resultList.curselection()[0]
    selecteditem = resultList.get(idx) #tuple selected
    print("點選內容", selecteditem)
    
    etycourse_id.delete(0, END);  
    etycourse_id.insert(0, selecteditem[0] )

    etycourse_name.delete(0, END); 
    etycourse_name.insert(0, selecteditem[1] )
    
    etycredit.delete(0, END); 
    etycredit.insert(0, selecteditem[2] )


resultList = Listbox(win)
resultList.grid(row=3, column=0, columnspan=3, sticky=W+E)
resultList.bind('<<ListboxSelect>>', onselect)

btnSelectAll = Button(win, text='Query', command=getAll)
btnSelectAll.grid(row=4, column=0, columnspan=3, sticky=W+E)

win.mainloop()