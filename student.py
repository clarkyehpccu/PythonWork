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
lblstd_id = Label(win, text='Student id')
lblstd_id.grid(row=0, column=0)
etystd_id=Entry(win)
etystd_id.grid(row=0, column=1)

lblstd_name = Label(win, text='Student Name')
lblstd_name.grid(row=1, column=0)
etystd_name=Entry(win)
etystd_name.grid(row=1, column=1)

lblsex = Label(win, text='Sex')
lblsex.grid(row=2, column=0)

sexFrame = Frame(win)
sexFrame.grid(row=2, column=1)
def getSexValue():
    pass 
sexVar = StringVar()
radioM = Radiobutton(sexFrame,text="男",  variable=sexVar, value = "M" , command=getSexValue)
radioM.grid(row=0, column=0, sticky=W) #座標以frame為準
radioF = Radiobutton(sexFrame,text="女", variable=sexVar, value = "F" , command=getSexValue)
radioF.grid(row=0, column=1, sticky=W) #座標以frame為準
sexVar.set('M')
def  qo(instr):
     return "'" + instr +"'"
def getAll():
    sqlstr = "select * from student "
    listx = execSQLcommand(sqlstr).fetchall()
    resultList.delete(0, END)
    for item in listx:
        resultList.insert(0, item)
def doInsert():
    sqlstr = "insert into student(std_id, std_name, sex)"
    sqlstr += "values(" + qo(etystd_id.get()) + ","
    sqlstr +=  qo(etystd_name.get()) + ","
    if sexVar.get() == 'M':
        sqlstr +=  "'M')"
    else:
        sqlstr +=  "'F')"
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
    
    etystd_id.delete(0, END);  
    etystd_id.insert(0, selecteditem[0] )

    etystd_name.delete(0, END); 
    etystd_name.insert(0, selecteditem[1] )
    
    if selecteditem[2] == 'M':
        sexVar.set('M')
    else:
        sexVar.set('F')


resultList = Listbox(win)
resultList.grid(row=3, column=0, columnspan=3, sticky=W+E)
resultList.bind('<<ListboxSelect>>', onselect)

btnSelectAll = Button(win, text='Query', command=getAll)
btnSelectAll.grid(row=4, column=0, columnspan=3, sticky=W+E)

def goMain():
    win.destroy()

btnExit = Button(win, text='Exit', command=goMain)
btnExit.grid(row=5, column=0, columnspan=3, sticky=W+E)
win.mainloop()